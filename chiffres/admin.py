from django.contrib import admin
from django.db import models
from chiffres.models import Chiffre
# Register your models here.

class ChiffreFilter(admin.ModelAdmin):
    list_display=['label', 'value', 'icon']

admin.site.register(Chiffre, ChiffreFilter)