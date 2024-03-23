from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from authentication.models import userprofile

# Create your views here.

def donation_request(request):
    if request.user.is_authenticated:
        try:
            profile = request.user.userprofile

            if profile.phone:
                return render(request, "donationrequest.html")
            else:
                messages.warning(request, "YOU ARE NOT REGISTERED AS DONOR YET!")
                return redirect('/')

        except ObjectDoesNotExist:
            messages.warning(request, "YOU ARE NOT REGISTERED AS DONOR YET!")
            return redirect('/')
    
    else: 
        messages.warning(request, "LOGIN TO DONATE!")
        return redirect('/') 
    
    
def donor_registration(request):
    return render(request, "donorregistration.html")

def registered_donors(request):
    return render(request, "registereddonors.html")

def donor_details(request, user_id):
    donor = get_object_or_404(userprofile, user_id=user_id)
    return render(request, "donordetails.html", {"donor": donor})

def ami_eligible(request):
    return  render(request,"eligibility.html") 
