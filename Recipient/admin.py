from django.contrib import admin
from Recipient.models import recipient

class recipientAdmin(admin.ModelAdmin):
    list_display = ('recipientname', 'recipientphone', 'recipientemail','recipientlocation', 'recipientage', 'recipientgender', 'recipientblood', 'recipientdonationtype', 'recipientdonationquantity', 'recipientcondition', 'recipientdate', 'recipienttime')
admin.site.register(recipient, recipientAdmin)
# Register your models here.   