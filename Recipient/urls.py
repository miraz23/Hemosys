from django.urls import path
from Recipient import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('request-blood/', views.request_blood, name="requestblood"),
    path('blood-availability/', views.blood_availability, name="bloodavailability"),
    path('organize-donation-camp/', views.organize_camp, name="organizecamp"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)