import imp
from django.db import models
from django.contrib.auth.models import User
from blog.models import Article
# Create your models here.
   
class Comment(models.Model):
    idComment = models.AutoField(db_column="idComment",primary_key=True)
    content = models.TextField()
    status = models.BooleanField(default=True)
    idUser = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    idArticle = models.ForeignKey(Article, on_delete=models.DO_NOTHING)