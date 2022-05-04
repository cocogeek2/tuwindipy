from dataclasses import fields
from rest_framework import serializers
from message.models import Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('idMessage','about', 'logo', 'slogan', 'nom')
        depth = 1