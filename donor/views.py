from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from authentication.models import userprofile
from Recipient.models import recipient, donationCamp
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.core.paginator import Paginator
from django.utils import timezone

# Create your views here.


def donation_request(request):
    if request.user.is_authenticated:
        reqdata = recipient.objects.all()

        #-------------------------- Searching Functionality --------------------------#

        if request.method == "GET":
            search_blood_group = request.GET.get('searchBloodGroup', None)
            search_location = request.GET.get('searchAddress', None)

            if search_blood_group or search_location:
                if search_blood_group:
                    reqdata = recipient.objects.filter(recipientblood__icontains=search_blood_group)
                
                if search_location:
                    search_parts = search_location.split()
                    for part in search_parts:
                        reqdata = [req for req in reqdata if part.lower() in req.recipientlocation.lower()]
            


        #-------------------------- Pagination --------------------------#
        paginator=Paginator(reqdata, 90)
        page_number=request.GET.get('page')
        page_obj=paginator.get_page(page_number)
    
    
        
        return render(request, "donationrequest.html", {"page_obj": page_obj})

    else:
        messages.warning(request, "PLEASE LOG IN TO DONATE")
        return redirect("/")


def donor_details(request, user_id):
    donor = get_object_or_404(userprofile, user_id=user_id)
    return render(request, "donordetails.html", {"donor": donor})


def ami_eligible(request):
    return render(request, "eligibility.html")


def donation(request, request_id):
    if request.method == 'POST':
        try:
            user_profile = request.user.userprofile
            recipient_obj = get_object_or_404(recipient, pk=request_id)

            if request.user.userprofile.bloodgroup == recipient_obj.recipientblood:

                if user_profile.next_eligible_date:

                    if timezone.now() < user_profile.next_eligible_date:
                        messages.warning(request, 'YOU NEED TO WAIT FOR 12 WEEKS AFTER YOUR LAST DONATION.')
                        return redirect('profile')

                    else:
                        user_profile.donor_donationcount += 1
                        user_profile.last_donation = timezone.now()
                        user_profile.save()
                        
                else:
                    user_profile.donor_donationcount += 1
                    user_profile.last_donation = timezone.now()
                    user_profile.save()


                recipient_name = recipient_obj.recipientname
                recipient_email = recipient_obj.recipientemail

                recipient_email_subject = "Request Confirmation"
                recipient_message = render_to_string('recipientemail.html', {
                    'donor_name': request.user.first_name,
                    'donor_phone': request.user.userprofile.phone,
                    'donor_email': request.user.email,
                    'donor_location': request.user.userprofile.location,
                    'donor_bloodgroup': request.user.userprofile.bloodgroup,
                    'donor_age': request.user.userprofile.age,
                    'donor_gender': request.user.userprofile.gender,
                    'recipient_name' : recipient_name,
                    'domain': '127.0.0.1:8000',
                })

                recipient_email_message = EmailMessage(
                    recipient_email_subject,
                    recipient_message,
                    settings.EMAIL_HOST_USER,
                    [recipient_email]
                )
                recipient_email_message.send()


                recipient_obj.delete()

                messages.success(request, 'THANK YOU FOR YOUR DONATION')
                return redirect('profile')
            else:
                messages.error(request, 'BLOOD GROUP NOT MATCHED.')
                return redirect('/donor/donation-request/')
        
        except userprofile.DoesNotExist:
            messages.error(request, 'REGISTER AS DONOR TO DONATE BLOOD.')
            return redirect('profile')
    else:
        redirect('/')


def delete_request(request, request_id):
    if request.method == 'POST':
        recipient_obj = get_object_or_404(recipient, pk=request_id)
        recipient_obj.delete()
        messages.success(request, 'DONATION REQUEST DELETED SUCCESSFULLY')
        return redirect('/')
    else:
        redirect('/')

def donation_camp(request):
    campdata = donationCamp.objects.all()

    if request.method == "GET":   
            st=request.GET.get('search')
            if st != None:
                campdata=donationCamp.objects.filter(campaddress__icontains = st)
    data={
        'campdata' : campdata,
    }
    return render(request, 'donationcamp.html', data)