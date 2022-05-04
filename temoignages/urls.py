from django.urls import re_path as url
from temoignages import views

urlpatterns = [
    url(r'^temoignage$', views.temoignages),
    url(r'^temoignage/([0-9]+)', views.TemoignageApi)
]
