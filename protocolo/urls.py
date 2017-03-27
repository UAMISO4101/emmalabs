from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^buscarProtocolo/$', views.buscar_protocolo_vista, name='buscarProtocolo'),
]