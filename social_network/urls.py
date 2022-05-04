from django.urls import re_path as url
from social_network import views

urlpatterns = [
    url(r'^social_network$', views.SocialNetworkApi),
    url(r'^social_network/([0-9]+)', views.SocialNetworkApi)
]