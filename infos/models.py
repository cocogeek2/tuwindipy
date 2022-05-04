import email
import imp
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
   
class Info(models.Model):
    idInfo = models.AutoField(db_column="idInfo",primary_key=True)
    about = models.TextField()
    logo = models.ImageField(upload_to="static/medias")
    slogan = models.TextField()
    nom = models.TextField()