from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    phone = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    bloodgroup = models.CharField(max_length=100)
    age = models.CharField(max_length=3)
    gender = models.CharField(max_length=10)
    image = models.FileField(upload_to='profile-picture', blank=True, null=True)
    donor_donationcount = models.IntegerField(default = 0)

    def __str__(self):
        return self.user.username

class bloodbank(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    bloodbankname = models.CharField(max_length=150)
    bloodbankemail = models.CharField(max_length=150)
    bloodbankphone = models.CharField(max_length=150)
    bloodbanklink = models.CharField(max_length=150)
    bloodbanklocation = models.CharField(max_length=150)
    bloodbanktypes = models.CharField(max_length=150)
    bloodbankgroups = models.CharField(max_length=150)
    bloodbankaccreditations = models.CharField(max_length=150)
    image = models.FileField(upload_to='Bloodbank-picture', blank=True, null=True)

    def __str__(self):
        return self.user.username