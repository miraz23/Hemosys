from django.db import models

class bloodbank(models.Model):
    
    bloodbankname = models.CharField(max_length=150)
    bloodbankemail = models.CharField(max_length=150)
    bloodbankphone = models.CharField(max_length=150)
    bloodbanklink = models.CharField(max_length=150)
    bloodbanklocation = models.CharField(max_length=150)
    bloodbankgroups = models.CharField(max_length=150) 
    
# Create your models here. 