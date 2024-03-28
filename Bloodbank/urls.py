from django.urls import path
from Bloodbank import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('bloodbank-details/<int:user_id>/', views.bloodbank_details, name="bloodbankdetails"), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 