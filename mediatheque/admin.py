from django.contrib import admin
from mediatheque.models import Mediatheque
# Register your models here.

class MediathequeFilter(admin.ModelAdmin):
    list_display=['label', 'media']

admin.site.register(Mediatheque, MediathequeFilter)