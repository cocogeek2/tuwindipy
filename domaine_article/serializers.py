from dataclasses import fields
from rest_framework import serializers
from domaine_article.models import Domaine

class DomaineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domaine
        fields = ('idDomaine','label', 'description', 'icon')
        depth = 1