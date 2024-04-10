from django.contrib import admin
from Recipient.models import recipient, donationCamp

class recipientAdmin(admin.ModelAdmin):
    list_display = ('recipientname', 'recipientphone', 'recipientemail','recipientlocation', 'recipientage', 'recipientgender', 'recipientblood', 'recipientdonationtype', 'recipientdonationquantity', 'recipientcondition', 'recipientdate', 'recipienttime')
admin.site.register(recipient, recipientAdmin)


class donation_campAdmin(admin.ModelAdmin):
    list_display = ('campname', 'campdate', 'camptime', 'campaddress', 'campcontact', 'camporganizer')
admin.site.register(donationCamp, donation_campAdmin)

# Register your models here.   