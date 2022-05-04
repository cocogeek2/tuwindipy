from django.urls import re_path as url
from domaine_article import views

urlpatterns = [
    url(r'^domaine$', views.DomaineApi),
    url(r'^domaine/([0-9]+)', views.DomaineApi)
]