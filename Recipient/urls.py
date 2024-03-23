from django.urls import path
from Recipient import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('request-blood/', views.request_blood, name="requestblood"),
    path('blood-availability/', views.blood_availability, name="bloodavailability"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)