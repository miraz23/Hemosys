from django.db import models

class donationCamp(models.Model):
    campname = models.CharField(max_length=150)
    campdate = models.CharField(max_length=150)
    camptime = models.CharField(max_length=150)
    campaddress = models.CharField(max_length=150)
    campcontact = models.CharField(max_length=150)
    camporganizer = models.CharField(max_length=150)
    
# Create your models here.