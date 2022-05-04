from django.contrib import admin
from message.models import Message
# Register your models here.

class MessageFilter(admin.ModelAdmin):
    list_display=['idUser', 'content', 'answer']

admin.site.register(Message, MessageFilter)