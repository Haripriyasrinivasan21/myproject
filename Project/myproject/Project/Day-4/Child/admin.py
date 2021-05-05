from django.contrib import admin
from Child.models import User
# Register your models here.

# class DonateAdmin(admin.ModelAdmin):
#  	list_display=['username','email','Mobile_Number','waystodonate','sponsorway','occdate','Pan']

admin.site.register(User)
# admin.site.register(Donate)
