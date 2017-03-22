from django.conf.urls import url
from django.contrib.contenttypes import views

from . import views

urlpatterns = [
    url(r'^crearSolicitud/$', views.crear_solicitud, name='crearSolicitud'),
]