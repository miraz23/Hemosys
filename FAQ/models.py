from django.db import models
from tinymce.models import HTMLField

class faq(models.Model):
    ques = models.CharField(max_length=150)
    ans = HTMLField()
    
# Create your models here.
