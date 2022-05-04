from dataclasses import fields
from rest_framework import serializers
from category.models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('idCategory','libelle', 'idParent')
        depth = 1