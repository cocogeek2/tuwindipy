from django.urls import re_path as url
from bureau import views

urlpatterns = [
    url(r'^bureau$', views.BureauApi),
    url(r'^bureau/([0-9]+)', views.BureauApi)
]