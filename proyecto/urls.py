from django.conf.urls import url
from django.contrib.contenttypes import views

from . import views

urlpatterns = [
    url(r'^proyectos/$', views.proyectos, name='proyectos'),
]