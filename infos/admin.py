from django.contrib import admin
from infos.models import Info
# Register your models here.

class InfoFilter(admin.ModelAdmin):
    list_display=['nom', 'slogan']

admin.site.register(Info, InfoFilter)