from django.db import models
# Create your models here.
   
class Bureau(models.Model):
    idBureau = models.AutoField(db_column="idBureau",primary_key=True)
    pays = models.TextField()
    adresse = models.TextField()
    tel = models.TextField()
    email = models.EmailField()
    focus = models.TextField()