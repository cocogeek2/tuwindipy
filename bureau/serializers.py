from dataclasses import fields
from rest_framework import serializers
from bureau.models import Bureau

class BureauSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bureau
        fields = ('idBureau','pays', 'adresse', 'tel', 'email',  'focus')
        depth = 1