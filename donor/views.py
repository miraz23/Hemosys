from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from authentication.models import userprofile
from Recipient.models import recipient

# Create your views here.


def donation_request(request):
    if request.user.is_authenticated:
        reqdata = recipient.objects.all()
        return render(request, "donationrequest.html", {"reqdata": reqdata})

    else:
        messages.warning(request, "PLEASE LOG IN TO DONATE")
        return redirect("/")


def donor_details(request, user_id):
    donor = get_object_or_404(userprofile, user_id=user_id)
    return render(request, "donordetails.html", {"donor": donor})


def ami_eligible(request):
    return render(request, "eligibility.html")
