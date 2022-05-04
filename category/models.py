from django.db import models

# Create your models here.

class Category(models.Model):
    idCategory = models.AutoField(db_column="idCategory",primary_key=True)
    libelle = models.CharField(max_length=255)
    idParent =  models.ForeignKey('self', on_delete=models.DO_NOTHING, related_name='children')

    def __str__(self):
        return self.libelle