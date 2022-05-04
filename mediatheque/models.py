from django.db import models

# Create your models here.
class Mediatheque(models.Model):
    idMediatheque = models.AutoField(db_column="idMediatheque",primary_key=True)
    label = models.CharField(max_length=255)
    description = models.TextField()
    media = models.FileField(upload_to="static/medias/videos")

    def __str__(self):
        return self.label