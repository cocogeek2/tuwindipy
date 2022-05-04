from django.contrib import admin
from bureau.models import Bureau
# Register your models here.

class BureauxFilter(admin.ModelAdmin):
    list_display=['pays', 'adresse', 'tel', 'email']

admin.site.register(Bureau, BureauxFilter)