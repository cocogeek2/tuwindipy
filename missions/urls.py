from django.urls import re_path as url
from missions import views

urlpatterns = [
    url(r'^mission$', views.MissionApi),
    url(r'^mission/([0-9]+)', views.MissionApi)
]