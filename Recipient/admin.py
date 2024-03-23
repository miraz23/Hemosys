from django.contrib import admin
from Recipient.models import recipient

class recipientAdmin(admin.ModelAdmin):
    list_display = ('recipientname', 'recipientphone', 'recipientlocation', 'recipientage', 'recipientgender', 'recipientblood', 'recipientdonationtype', 'recipientdonationquantity', 'recipientcondition', 'recipientdate')
admin.site.register(recipient, recipientAdmin)
# Register your models here.   