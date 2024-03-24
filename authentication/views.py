from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import View
from .forms import signupForm, userprofileForm, bloodbankForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from .utils import generate_token
from django.utils.encoding import force_bytes,force_str
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
    if request.method=="POST":
        form = signupForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()


            email_subject="Activate Your Account"
            message=render_to_string('activate.html',{
                'user':user,
                'domain':'127.0.0.1:8000',
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':generate_token.make_token(user)

            })

            email_message = EmailMessage(email_subject,message,settings.EMAIL_HOST_USER,[user.email])
            email_message.send()
            messages.success(request,"ACTIVATE YOUR ACCOUNT BY CLICKING THE LINK IN YOUR GMAIL")
            return redirect('/auth/login/')
        
        else:
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')

            if password1 != password2:
                messages.warning(request,"PASSWORD NOT MATCHED")
                return redirect('/auth/signup/')
            else:
                messages.warning(request,"EMAIL IS ALREADY REGISTERED")
                return redirect('/auth/signup/')
            
    else:
        form = signupForm()
    
    context={"form":form}
    
    return render(request,'signup.html',context)


class ActivateAccountView(View):
    def get(self,request,uidb64,token):
        try:
            uid=force_str(urlsafe_base64_decode(uidb64))
            user=User.objects.get(pk=uid)
        except Exception as identifier:
            user=None
        if user is not None and generate_token.check_token(user,token):
            user.is_active=True
            user.save()
            messages.info(request,"ACCOUNT ACTIVATED SUCCESSFULLY")
            return redirect('/auth/login')
        return render(request,'activatefail.html')


def handlelogin(request):
    if request.method=="POST":

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username =  form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request,user)
                messages.success(request,"LOG IN SUCCESS")
                return redirect('/')
            else:
                messages.error(request,"INVALID CREDENTIALS")
                return redirect('/auth/login')

    
    form = AuthenticationForm()
    return render(request,'login.html')


def handlelogout(request):
    logout(request)
    messages.info(request,"LOG OUT SUCCESS")
    return redirect('/auth/login')


def user_profile(request):
    if request.user.is_authenticated:
        return render(request, "profile.html")
    else:
        messages.warning(request,"PLEASE LOG IN TO ACCESS YOUR PROFILE")
        redirect('/')

    return redirect('/')

def complete_profile(request):
    if request.method == "POST":
        profile_form = userprofileForm(request.POST, request.FILES)

        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('/auth/profile/')
    
    else:
        profile_form = userprofileForm()

    context = {"profile_form": profile_form}

    return render(request, 'completeprofile.html', context)


@login_required
def edit_profile(request):
    user_profile = request.user.userprofile
    if request.method == 'POST':
        form = userprofileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('/auth/profile/')
    else:
        form = userprofileForm(instance=user_profile)
    return render(request, 'editprofile.html', {'form': form})


def add_blood_bank(request):
    if request.method == "POST":
        bank_form = bloodbankForm(request.POST, request.FILES)

        if bank_form.is_valid():
            bloodbank = bank_form.save(commit=False)
            bloodbank.user = request.user
            bloodbank.save()
            return redirect('/auth/profile/')
    
    else:
        bank_form = bloodbankForm()

    context = {"bank_form": bank_form}

    return render(request, 'addbloodbank.html', context)
        
