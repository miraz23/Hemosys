from django.shortcuts import render, redirect
from .models import recipient, donationCamp
from authentication.models import bloodbank, userprofile
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

# Create your views here. 
def request_blood(request): 
    if request.user.is_authenticated:
        if request.method == 'POST':
            if recipient.objects.filter(user_id=request.user.id).exists():
                messages.warning(request, "YOU HAVE ALREADY SUBMITTED A BLOOD REQUEST. PLEASE WAIT FOR A RESPONSE.")
                return redirect("/donor/donation-request/")
            else:
                data = recipient(
                    user_id=request.user.id,
                    recipientname=request.POST.get('recipientname'),
                    recipientphone=request.POST.get('recipientphone'),
                    recipientemail=request.POST.get('recipientemail'),
                    recipientlocation=request.POST.get('recipientlocation'),
                    recipientage=request.POST.get('recipientage'),
                    recipientgender=request.POST.get('recipientgender'),
                    recipientblood=request.POST.get('recipientblood'),
                    recipientdonationtype=request.POST.get('recipientdonationtype'),
                    recipientdonationquantity=request.POST.get('recipientdonationquantity'),
                    recipientcondition=request.POST.get('recipientcondition'),
                    recipientdate=request.POST.get('recipientdate'),
                    recipienttime=request.POST.get('recipienttime'),
                )
                data.save()
                try:
                    blood_banks = bloodbank.objects.all()
                    for bank in blood_banks:
                        email_subject = "Donation Request"
                        message = render_to_string('bankemail.html', {
                            'recipient_name': data.recipientname,
                            'recipient_phone': data.recipientphone,
                            'recipient_email': data.recipientemail,
                            'recipient_location': data.recipientlocation,
                            'recipient_age': data.recipientage,
                            'recipient_gender': data.recipientgender,
                            'recipient_blood': data.recipientblood,
                            'recipient_donationtype': data.recipientdonationtype,
                            'recipient_donationquantity': data.recipientdonationquantity,
                            'recipient_condition': data.recipientcondition,
                            'recipient_date': data.recipientdate,
                            'recipient_time': data.recipienttime,
                            'bank_name': bank.bloodbankname,
                            'domain': '127.0.0.1:8000',
                        })
    
                    email_message = EmailMessage(
                        email_subject,
                        message,
                        settings.EMAIL_HOST_USER,
                        [bank.bloodbankemail]
                    )
                    email_message.send()
                
                except:
                    pass
                
                try:
                    donors = User.objects.filter(userprofile__isnull=False)
                    for donor in donors:
                        donor_email_subject = "Donation Request"
                        donor_message = render_to_string('donoremail.html', {
                            'recipient_name': data.recipientname,
                            'recipient_phone': data.recipientphone,
                            'recipient_email': data.recipientemail,
                            'recipient_location': data.recipientlocation,
                            'recipient_age': data.recipientage,
                            'recipient_gender': data.recipientgender,
                            'recipient_blood': data.recipientblood,
                            'recipient_donationtype': data.recipientdonationtype,
                            'recipient_donationquantity': data.recipientdonationquantity,
                            'recipient_condition': data.recipientcondition,
                            'recipient_date': data.recipientdate,
                            'recipient_time': data.recipienttime,
                            'donor_name': donor.first_name,
                            'domain': '127.0.0.1:8000',
                        })
                    donor_email_message = EmailMessage(
                        donor_email_subject,
                        donor_message,
                        settings.EMAIL_HOST_USER,
                        [donor.email]
                    )
                    donor_email_message.send()
                except:
                    pass
                
                return redirect("/donor/donation-request/")
        return render(request, "requestblood.html") 
    else:
        messages.warning(request, "PLEASE LOG IN TO REQUEST")
        return redirect('/')

def blood_availability(request): 

    bankdata = bloodbank.objects.all()
    donors = User.objects.filter(userprofile__isnull=False).select_related('userprofile')

    #------ ====== Searching Functionality ===== -----#

    if request.method == "GET":
        search_blood_group = request.GET.get('searchBloodGroup', None)
        search_location = request.GET.get('searchAddress', None)
        search_type = request.GET.get('searchType', None)


        if search_blood_group or search_location:
            
            if search_blood_group:

                bankdata=bloodbank.objects.filter(bloodbankgroups__icontains = search_blood_group)
                donors = [user for user in donors if user.userprofile.bloodgroup == search_blood_group]

            if search_location:

                search_parts = search_location.split()
                for part in search_parts:
                    donors = [user for user in donors if part.lower() in user.userprofile.location.lower()]
                    bankdata = [bank for bank in bankdata if part.lower() in bank.bloodbanklocation.lower()]



        if search_type == 'Donor':
            bankdata = ""
            if search_blood_group:
                donors = [user for user in donors if user.userprofile.bloodgroup == search_blood_group]
            if search_location:
                search_parts = search_location.split()
                for part in search_parts:
                    donors = [user for user in donors if part.lower() in user.userprofile.location.lower()]

        if search_type == 'BloodBank':
            donors = ""
            if search_blood_group:
                bankdata=bloodbank.objects.filter(bloodbankgroups__icontains = search_blood_group)
            if search_location:
                search_parts = search_location.split()
                for part in search_parts:
                    bankdata = [bank for bank in bankdata if part.lower() in bank.bloodbanklocation.lower()]




    data={
        'bankdata' : bankdata,
        'users' : donors,
    }
    return render(request, "bloodavailability.html", data)



def organize_camp(request):
    if request.user.is_authenticated:

        if request.method == "POST":   

            data = donationCamp(
                campname = request.POST.get('campname'), 
                campdate = request.POST.get('campdate'), 
                camptime = request.POST.get('camptime'), 
                campaddress = request.POST.get('campaddress'), 
                campcontact = request.POST.get('campcontact'), 
                camporganizer = request.POST.get('camporganizer'), 
            )
            data.save()
            messages.success(request, "DONATION CAMP ORGANIZED SUCCESSFULLY")
            return redirect('/')
        else:
            return render(request, 'organizecamp.html')
        
    else:
        messages.warning(request, "PLEASE LOGIN TO ORGANIZE BLOOD DONATION CAMP")
        return render(request, 'index.html')