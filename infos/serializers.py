from dataclasses import fields
from rest_framework import serializers
from infos.models import Info

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = ('idInfo','about', 'logo', 'slogan', 'nom')
        depth = 1