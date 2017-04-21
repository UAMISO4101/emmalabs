from django.conf.urls import url
from . import views

urlpatterns = [
    #url para crear una solicitud
    url(r'^crearSolicitud/$', views.crear_solicitud, name='crearSolicitud'),
    #url para el menu de solicitudes
    url(r'^menuSolicitud/$', views.menu_solicitud, name='menuSolicitud'),
    #url para ver lista de solicitudes
    url(r'^solicitudes/$', views.listar_solicitudes, name='solicitudes'),
]