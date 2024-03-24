from django.shortcuts import render
from FAQ.models import faq
from django.contrib.auth.models import User
from authentication.models import bloodbank
from Donationcamp.views import donationCamp
from authentication.models import userprofile
# Create your views here.
def index(request):
    user_count = User.objects.all().count()
    donor_count = userprofile.objects.count()
    bank_count = bloodbank.objects.all().count()
    camp_count = donationCamp.objects.all().count
    
    faqdet= faq.objects.all()

    data={
        'faqdet' : faqdet,
        'user_count' : user_count,
        'donor_count' : donor_count,
        'bank_count' : bank_count,
        'camp_count' : camp_count
    }
    return render(request, "index.html", data)

def contact(request):
    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")