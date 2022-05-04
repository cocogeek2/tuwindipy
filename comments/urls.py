from django.urls import re_path as url
from comments import views

urlpatterns = [
    url(r'^comment$', views.CommentApi),
    url(r'^comment/([0-9]+)', views.CommentApi)
]