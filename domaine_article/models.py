from operator import mod
from pydoc import describe
from django.db import models

# Create your models here.
class Domaine(models.Model):
    idDomaine = models.AutoField(db_column="idDomaine",primary_key=True)
    label = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.ImageField(upload_to="static/medias/icons")

    def __str__(self):
        return self.label