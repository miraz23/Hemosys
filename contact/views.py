from django.shortcuts import render
from django.contrib import messages
from .models import Contact

# Create your views here.


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
    
    return render(request, 'contact.html')