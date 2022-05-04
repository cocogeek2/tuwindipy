from django.contrib import admin
from category.models import Category
# Register your models here.

class CategoryFilter(admin.ModelAdmin):
    list_display=['libelle']

admin.site.register(Category, CategoryFilter)