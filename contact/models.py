from django.db import models

# Create your models here.

class Contact(models.Model):
    contact_name= models.CharField(max_length = 150, verbose_name="Name")
    contact_email=models.CharField(max_length=150, verbose_name="Email")
    contact_subject=models.CharField(max_length=200, verbose_name="Subject")
    contact_message=models.TextField(verbose_name="Message")

    def __str__(self):
        return self.contact_subject