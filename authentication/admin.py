from django.contrib import admin
from .models import userprofile
from .models import bloodbank
# Register your models here.

admin.site.register(bloodbank)
admin.site.register(userprofile)