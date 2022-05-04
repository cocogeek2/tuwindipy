from django.contrib import admin
from blog.models import Article
# Register your models here.

class ArticlesFilter(admin.ModelAdmin):
    list_display=['title', 'status', 'createDate', 'updateDate']

admin.site.register(Article, ArticlesFilter)