from django.shortcuts import render, get_object_or_404
from authentication.models import bloodbank
#Create your views here.

def bloodbank_details(request, user_id):
    bank = get_object_or_404(bloodbank, user_id=user_id)
    return render(request, "bloodbankdetails.html", {"bank": bank})