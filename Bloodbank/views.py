from django.shortcuts import render, redirect
# from authentication.models import bloodbank

#Create your views here.

# def registered_blood_banks(request):
#     bankdata = bloodbank.objects.all()
#     if request.method == "GET":   
#             st=request.GET.get('search')
#             if st != None:
#                 bankdata=bloodbank.objects.filter(bloodbankname__icontains = st)

#     getbankdata = {
#             'bankdata' : bankdata,
#     }
#     return render(request, "registeredbloodbanks.html", getbankdata)