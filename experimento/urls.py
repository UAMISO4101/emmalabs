from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^proyectos/(\d+)/$', views.detalleProyecto),
    url(r'^crearExperimento/$', views.crear_experimento, name='crearExperimento'),
]