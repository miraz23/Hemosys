from django.db import models

class recipient(models.Model):

    recipientname = models.CharField(max_length=150, verbose_name="Name")
    recipientphone = models.CharField(max_length=150, verbose_name="Contact")
    recipientemail = models.CharField(max_length=150, verbose_name="Email")
    recipientlocation = models.CharField(max_length=150, verbose_name="Location") 
    recipientage = models.CharField(max_length=150, verbose_name="Age") 
    recipientgender = models.CharField(max_length=150, verbose_name="Gender") 
    recipientblood = models.CharField(max_length=150, verbose_name="Blood Group")
    recipientdonationtype = models.CharField(max_length=150, null=True, verbose_name="Type")
    recipientdonationquantity = models.CharField(max_length=150, verbose_name="Quantity")
    recipientcondition = models.CharField(max_length=150, verbose_name="Condition")
    recipientdate = models.CharField(max_length=150, verbose_name="Date")
    recipienttime = models.CharField(max_length=150, default = None, verbose_name="Time")

    class Meta:
        verbose_name = "Requested Blood"
        verbose_name_plural = "Requested Blood"
    

class donationCamp(models.Model):
    campname = models.CharField(max_length=150, verbose_name="Name")
    campdate = models.CharField(max_length=150, verbose_name="Date")
    camptime = models.CharField(max_length=150, verbose_name="Time")
    campaddress = models.CharField(max_length=150, verbose_name="Location")
    campcontact = models.CharField(max_length=150, verbose_name="Contact")
    camporganizer = models.CharField(max_length=150, verbose_name="Organizer")

    class Meta:
        verbose_name = "Organized Camp"
        verbose_name_plural = "Organized Camp"
    
# Create your models here.