from django.db import models

# Create your models here.

class Contact(models.Model):
    contact_name= models.CharField(max_length = 150)
    contact_email=models.CharField(max_length=150)
    contact_subject=models.CharField(max_length=200)
    contact_message=models.TextField()

    def __str__(self):
        return self.contact_subject