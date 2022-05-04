from tkinter.messagebox import YES
from django.db import models
from django.contrib.auth.models import User
from category.models import Category
from domaine_article.models import Domaine
# Create your models here.

class Article(models.Model):
    idArticle = models.AutoField(db_column="idArticle",primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    img = models.ImageField(upload_to="static/medias")
    status = models.BooleanField(default=True)
    createDate = models.DateField()
    updateDate = models.DateField()
    idUser = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    idCategory = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    idDomaine = models.ForeignKey(Domaine, null=True, on_delete=models.DO_NOTHING)