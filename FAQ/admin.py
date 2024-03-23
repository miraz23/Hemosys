from django.contrib import admin
from FAQ.models import faq

class FAQAdmin(admin.ModelAdmin):
    list_display=('ques', 'ans')
admin.site.register(faq, FAQAdmin)
# Register your models here.
