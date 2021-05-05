from django.contrib import admin
from Child.models import Newuser
# Register your models here.

class NewuserAdmin(admin.ModelAdmin):
	list_display=['First_Name','Last_Name','Email_ID','Dob','Mobile_Number','PAN','Address','Country','Postal_code','City']

admin.site.register(Newuser,NewuserAdmin)