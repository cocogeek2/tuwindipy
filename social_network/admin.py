from django.contrib import admin
from social_network.models import SocialNetwork
# Register your models here.

class SocialNetworkFilter(admin.ModelAdmin):
    list_display=['name', 'url', 'icon']

admin.site.register(SocialNetwork, SocialNetworkFilter)