import imp
from django.db import models
from django.contrib.auth.models import User
from blog.models import Article
# Create your models here.
   
class Message(models.Model):
    idMessage = models.AutoField(db_column="idMessage",primary_key=True)
    content = models.TextField()
    answer = models.TextField()
    idUser = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING, related_name='auteur')
    idResponder = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING, related_name='moderateur')