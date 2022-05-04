from django.urls import re_path as url
from message import views

urlpatterns = [
    url(r'^message$', views.MessageApi),
    url(r'^message/([0-9]+)', views.MessageApi)
]