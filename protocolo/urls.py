from django.conf.urls import url

from . import views

urlpatterns = [
    # url para buscar un protocolo
    url(r'^buscarProtocolo/$', views.buscar_protocolo_vista, name='buscarProtocolo'),
    # url para ver detalle de un protocolo
    url(r'^protocolos/(?P<id_protocolo>\d+)/$', views.detalle_protocolo_vista, name='protocolos'),
    # url para crear un Protocolo
    url(r'^crearProtocolo/$', views.crear_protocolo, name='crearProtocolo'),
    # url para actualizar un protocolo
    url(r'^actualizarProtocolo/(?P<id_protocolo>\d+)/$', views.actualizar_protocolo, name='actualizarProtocolo'),
]
