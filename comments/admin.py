from django.contrib import admin
from django.db import models
from comments.models import Comment
# Register your models here.

class CommentFilter(admin.ModelAdmin):
    list_display=['idUser', 'content', 'idArticle', 'status']

admin.site.register(Comment, CommentFilter)