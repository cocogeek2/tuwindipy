from dataclasses import fields
from rest_framework import serializers
from missions.models import Mission

class MissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = ('idMission','label', 'description', 'icon')
        depth = 1