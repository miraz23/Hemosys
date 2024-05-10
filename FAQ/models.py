from django.db import models
from tinymce.models import HTMLField

class faq(models.Model):
    ques = models.TextField(verbose_name="Question")
    ans = HTMLField(verbose_name="Answer")

    class Meta:
        verbose_name = "FAQs"
        verbose_name_plural = "FAQs"
    
# Create your models here.
