"""tuwindiPy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path,re_path as url,include
from blog import urls as blog
from home import urls as home
from bureau import urls as bureau
from category import urls as category
from chiffres import urls as chiffre
from comments import urls as comment
from domaine_article import urls as domaine
from infos import urls as info
from message import urls as message
from social_network import urls as rs
from temoignages import urls as tem
from missions import urls as mission
urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin', admin.site.urls),
    url(r'^', include(home)),
    url(r'^', include(blog)),
    url(r'^', include(bureau)),
    url(r'^', include(category)),
    url(r'^', include(chiffre)),
    url(r'^', include(comment)),
    url(r'^', include(domaine)),
    url(r'^', include(info)),
    url(r'^', include(message)),
    url(r'^', include(rs)),
    url(r'^', include(tem)),
    url(r'^', include(mission)),


    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 

]