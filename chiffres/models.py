from django.db import models

# Create your models here.
class Chiffre(models.Model):
    idChiffre = models.AutoField(db_column="idChiffre",primary_key=True)
    label = models.CharField(max_length=255)
    value = models.IntegerField()
    icon = models.ImageField(upload_to="medias/icons")
   