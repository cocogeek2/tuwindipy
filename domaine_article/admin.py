from django.contrib import admin
from django.db import models
from domaine_article.models import Domaine
# Register your models here.

class DomaineFilter(admin.ModelAdmin):
    list_display=['label', 'icon']

admin.site.register(Domaine, DomaineFilter)