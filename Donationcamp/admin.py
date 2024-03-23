from django.contrib import admin
from Donationcamp.models import donationCamp

class donation_campAdmin(admin.ModelAdmin):
    list_display = ('campname', 'campdate', 'camptime', 'campaddress', 'campcontact', 'camporganizer')
admin.site.register(donationCamp, donation_campAdmin)
# Register your models here.
