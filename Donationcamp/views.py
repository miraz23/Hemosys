from django.shortcuts import render
from Donationcamp.models import donationCamp
# Create your views here.


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
 