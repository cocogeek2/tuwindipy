from django.contrib import admin
from missions.models import Mission
# Register your models here.

class MissionFilter(admin.ModelAdmin):
    list_display=['label', 'icon']

admin.site.register(Mission, MissionFilter)