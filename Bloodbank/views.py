from django.shortcuts import render, redirect
from .models import bloodbank
# Create your views here.

def add_blood_bank(request):
    bloodbankgroups = request.POST.getlist('bloodbankgroups')
    if request.method == 'POST':
        data = bloodbank(
            bloodbankname=request.POST.get('bloodbankname'),
            bloodbankemail=request.POST.get('bloodbankemail'),
            bloodbankphone=request.POST.get('bloodbankphone'),
            bloodbanklink=request.POST.get('bloodbanklink'),
            bloodbanklocation=request.POST.get('bloodbanklocation'),
            bloodbankgroups = ', '.join(bloodbankgroups)
        )
        data.save()
        
        return redirect("/blood-bank/registered-blood-banks/") 
    return render(request, "addbloodbank.html")

def registered_blood_banks(request):
    bankdata = bloodbank.objects.all()
    if request.method == "GET":   
            st=request.GET.get('search')
            if st != None:
                bankdata=bloodbank.objects.filter(bloodbankname__icontains = st)

    getbankdata = {
            'bankdata' : bankdata,
    }
    return render(request, "registeredbloodbanks.html", getbankdata)