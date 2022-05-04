from django.db import models
from django.contrib.auth.models import User
# Create your models here.
   
class Temoignage(models.Model):
    idTemoignage = models.AutoField(db_column="idTemoignage",primary_key=True)
    content = models.TextField()
    img = models.ImageField(upload_to="static/medias")
    status = models.BooleanField(default=True)
    idUser = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING)