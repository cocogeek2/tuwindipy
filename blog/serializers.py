from dataclasses import field, fields
from rest_framework import serializers
from blog.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('idArticle','title', 'content', 'img', 'status',  'createDate', 'updateDate','idUser','idCategory', 'idDomaine')
        depth = 1
