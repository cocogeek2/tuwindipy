from django.urls import re_path as url
from infos import views

urlpatterns = [
    url(r'^info$', views.InfoApi),
    url(r'^info/([0-9]+)', views.InfoApi)
]