from dataclasses import fields
from rest_framework import serializers
from social_network.models import SocialNetwork

class SocialNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialNetwork
        fields = ('idSocialNetwork','url', 'icon', 'name')
        depth = 1