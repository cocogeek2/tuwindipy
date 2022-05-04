from unicodedata import name
from django.urls import path, re_path as url
from blog import views

urlpatterns = [
    url(r'^article$', views.ArticleApi),
    url(r'^article/([0-9]+)', views.ArticleApi),
    url(r'^article/details', views.articleDetails),
    url(r'^blog', views.blog),
    url(r'^opportinuties', views.opportinuties),
    url(r'^projects', views.projets),
    url(r'^project/details', views.projetDetails),
    url(r'^reports', views.reports),
    url(r'^reports/details', views.reportDetails),
]