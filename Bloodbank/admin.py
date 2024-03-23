from django.contrib import admin
from Bloodbank.models import bloodbank

class bloodbankAdmin(admin.ModelAdmin):
    list_display = ('bloodbankname', 'bloodbankemail', 'bloodbankphone', 'bloodbanklink', 'bloodbanklocation', 'bloodbankgroups')
admin.site.register(bloodbank, bloodbankAdmin)
# Register your models here. 
