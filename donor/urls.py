from django.urls import path
from donor import views
from django.conf import settings
from django.conf.urls.static import static
from Donationcamp.views import donation_camp

urlpatterns = [
    path('donation-request/', views.donation_request, name="donationrequest"),
    path('donor-registration/', views.donor_registration, name="donorregistration"),
    path('registered-donors/', views.registered_donors, name="registereddonors"),
    path('donor-details/<int:user_id>/', views.donor_details, name="donordetails"), 
    path('blood-donation-camp/', donation_camp, name="donationcamp"), 
    path('am-i-eligible/', views.ami_eligible, name="amieligible"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)