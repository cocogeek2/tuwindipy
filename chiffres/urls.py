from django.urls import re_path as url
from chiffres import views

urlpatterns = [
    url(r'^chiffre$', views.ChiffreApi),
    url(r'^chiffre/([0-9]+)', views.ChiffreApi)
]