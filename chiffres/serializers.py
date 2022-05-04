from dataclasses import fields
from rest_framework import serializers
from chiffres.models import Chiffre

class ChiffreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chiffre
        fields = ('idChiffre','label', 'value', 'icon')
        depth = 1