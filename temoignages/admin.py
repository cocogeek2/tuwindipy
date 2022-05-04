from django.contrib import admin
from temoignages.models import Temoignage
# Register your models here.

class TemoignageFilter(admin.ModelAdmin):
    list_display=['idUser', 'content', 'status']

admin.site.register(Temoignage, TemoignageFilter)