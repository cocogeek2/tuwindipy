from django.urls import re_path as url
from category import views

urlpatterns = [
    url(r'^category$', views.CategoryApi),
    url(r'^category/([0-9]+)', views.CategoryApi)
]