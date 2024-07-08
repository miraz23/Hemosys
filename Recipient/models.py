from django.db import models
from django.contrib.auth.models import User

class recipient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    recipientname = models.CharField(max_length=150, verbose_name="Name")
    recipientphone = models.CharField(max_length=150, verbose_name="Contact")
    recipientemail = models.CharField(max_length=150, verbose_name="Email")
    recipientlocation = models.TextField(verbose_name="Location") 
    recipientage = models.CharField(max_length=150, verbose_name="Age") 
    recipientgender = models.CharField(max_length=150, verbose_name="Gender") 
    recipientblood = models.CharField(max_length=150, verbose_name="Blood Group")
    recipientdonationtype = models.CharField(max_length=150, null=True, verbose_name="Type")
    recipientdonationquantity = models.CharField(max_length=150, verbose_name="Quantity")
    recipientcondition = models.TextField(verbose_name="Condition")
    recipientdate = models.DateField(max_length=150, verbose_name="Date")
    recipienttime = models.TimeField(max_length=150, default = None, verbose_name="Time")

    class Meta:
        verbose_name = "Requested Blood"
        verbose_name_plural = "Requested Blood"
    

class donationCamp(models.Model):
    campname = models.CharField(max_length=150, verbose_name="Name")
    campdate = models.DateField(max_length=150, verbose_name="Date")
    camptime = models.TimeField(max_length=150, verbose_name="Time")
    campaddress = models.TextField(verbose_name="Location")
    campcontact = models.CharField(max_length=150, verbose_name="Contact")
    camporganizer = models.TextField(verbose_name="Organizer")

    class Meta:
        verbose_name = "Organized Camp"
        verbose_name_plural = "Organized Camp"
    
# Create your models here.