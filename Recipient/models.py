from django.db import models

class recipient(models.Model):

    recipientname = models.CharField(max_length=150)
    recipientphone = models.CharField(max_length=150)
    recipientemail = models.CharField(max_length=150)
    recipientlocation = models.CharField(max_length=150) 
    recipientage = models.CharField(max_length=150) 
    recipientgender = models.CharField(max_length=150) 
    recipientblood = models.CharField(max_length=150)
    recipientdonationtype = models.CharField(max_length=150, null=True)
    recipientdonationquantity = models.CharField(max_length=150)
    recipientcondition = models.CharField(max_length=150)
    recipientdate = models.CharField(max_length=150)
    recipienttime = models.CharField(max_length=150, default = None)
    

class donationCamp(models.Model):
    campname = models.CharField(max_length=150)
    campdate = models.CharField(max_length=150)
    camptime = models.CharField(max_length=150)
    campaddress = models.CharField(max_length=150)
    campcontact = models.CharField(max_length=150)
    camporganizer = models.CharField(max_length=150)
    
# Create your models here.