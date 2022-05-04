from dataclasses import fields
from rest_framework import serializers
from temoignages.models import Temoignage

class TemoignageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temoignage
        fields = ('idTemoignage','content', 'status', 'idUser')
        depth = 1