from django.shortcuts import render, redirect
from FAQ.models import faq
from django.contrib.auth.models import User
from authentication.models import bloodbank
from Donationcamp.views import donationCamp
from authentication.models import userprofile
from django.contrib import messages
from contact.models import Contact

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
    if request.method == 'POST':
       
        data = Contact(
            contact_name = request.POST.get('contact_name'),
            contact_email = request.POST.get('contact_email'),
            contact_subject = request.POST.get('contact_subject'),
            contact_message = request.POST.get('contact_message'),
        )
        data.save()
        messages.success(request, "YOUR MESSAGE HAS BEEN SUBMITTED. THANK YOU")
        return redirect('/')
    
    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")