from django.contrib import admin
from django.db import models

# Create your models here.
class SocialNetwork(models.Model):
    idSocialNetwork = models.AutoField(db_column="idSocialNetwork",primary_key=True)
    url = models.CharField(max_length=255)
    icon = models.ImageField(upload_to="medias/icons")
    name = models.TextField(max_length=50)