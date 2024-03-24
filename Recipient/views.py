from django.shortcuts import render, redirect
from .models import recipient
from authentication.models import bloodbank
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here. 
def request_blood(request): 
    if request.user.is_authenticated:
        if request.method == 'POST':
            data = recipient(
                recipientname=request.POST.get('recipientname'),
                recipientphone=request.POST.get('recipientphone'),
                recipientlocation=request.POST.get('recipientlocation'),
                recipientage=request.POST.get('recipientage'),
                recipientgender=request.POST.get('recipientgender'),
                recipientblood=request.POST.get('recipientblood'),
                recipientdonationtype=request.POST.get('recipientdonationtype'),
                recipientdonationquantity=request.POST.get('recipientdonationquantity'),
                recipientcondition=request.POST.get('recipientcondition'),
                recipientdate=request.POST.get('recipientdate')
            )
            data.save()
            return redirect("/donor/donation-request/")
        return render(request, "requestblood.html") 
    else:
        messages.warning(request, "PLEASE LOG IN TO REQUEST")
        return redirect('/')

def blood_availability(request):

    bankdata = bloodbank.objects.all()
    users_with_profiles = User.objects.filter(userprofile__isnull=False).select_related('userprofile')

    if request.method == "GET":   
        st=request.GET.get('searchBloodGroup')
        if st != None:
            bankdata=bloodbank.objects.filter(bloodbankgroups__icontains = st)
    data={
        'bankdata' : bankdata,
        'users' : users_with_profiles,
    }
    return render(request, "bloodavailability.html", data)