from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^proyectos/(\d+)/$', views.detalleProyecto, name='proyectos'),
    url(r'^proyectos/(\d+)/crearExperimento/$', views.crear_experimento, name='crearExperimento'),
]