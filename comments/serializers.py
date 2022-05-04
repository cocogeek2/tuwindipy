from dataclasses import fields
from rest_framework import serializers
from comments.models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('idComment','content', 'status', 'idUser', 'idArticle')
        depth = 1