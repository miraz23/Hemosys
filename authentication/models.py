from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta
# Create your models here.

class userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    phone = models.CharField(max_length=100)
    location = models.CharField(max_length=5000)
    bloodgroup = models.CharField(max_length=100, verbose_name="Blood Group")
    age = models.CharField(max_length=3)
    gender = models.CharField(max_length=10)
    image = models.FileField(upload_to='profile-picture', blank=True, null=True)
    donor_donationcount = models.IntegerField(default = 0, verbose_name="Dontion Count")
    last_donation = models.DateTimeField(null=True, blank=True)

    @property
    def next_eligible_date(self):
        if self.last_donation:
            return self.last_donation + timedelta(weeks=12)
        return None

    def __str__(self):
        return self.user.first_name

    class Meta:
        verbose_name = "Donor"
        verbose_name_plural = "Donor"

class bloodbank(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    bloodbankname = models.CharField(max_length=150, verbose_name="Name")
    bloodbankemail = models.CharField(max_length=150, verbose_name="Email")
    bloodbankphone = models.CharField(max_length=150, verbose_name="Contact")
    bloodbanklink = models.CharField(max_length=5000, verbose_name="Website Link")
    bloodbanklocation = models.CharField(max_length=5000, verbose_name="Location")
    bloodbanktypes = models.CharField(max_length=150, verbose_name="Types")
    bloodbankgroups = models.CharField(max_length=150, verbose_name="Available Groups")
    bloodbankaccreditations = models.CharField(max_length=2000, verbose_name="Accreditaions")
    image = models.FileField(upload_to='Bloodbank-picture', blank=True, null=True, verbose_name="Image")

    def __str__(self):
        return self.bloodbankname
    
    class Meta:
        verbose_name = "Blood Bank"
        verbose_name_plural = "Blood Bank"