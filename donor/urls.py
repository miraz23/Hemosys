from django.urls import path
from donor import views
from django.conf import settings
from django.conf.urls.static import static
from donor.views import donation_camp

urlpatterns = [
    path('donation-request/', views.donation_request, name="donationrequest"),
    path('donor-details/<int:user_id>/', views.donor_details, name="donordetails"), 
    path('blood-donation-camp/', donation_camp, name="donationcamp"), 
    path('am-i-eligible/', views.ami_eligible, name="amieligible"),
    path('confirm-donation/<int:request_id>/', views.donation, name="donation"),
    path('delete-donation-request/<int:request_id>/', views.delete_request, name="delete_request"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 