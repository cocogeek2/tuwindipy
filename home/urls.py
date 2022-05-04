from django.urls import re_path as url
from home import views

urlpatterns = [
    url(r'^home$', views.home),
    url(r'^about$', views.about),
    url(r'^contact$', views.contact),
    url(r'^opportinutes$', views.opportinutes)
]