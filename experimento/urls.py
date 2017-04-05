from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^proyectos/(\d+)/$', views.detalleProyecto),
    url(r'^prueba_plantilla/$', views.prueba_plantilla),
]