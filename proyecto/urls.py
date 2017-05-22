from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^proyectos/$', views.proyectos),
    url(r'^crearProyecto/$', views.crear_proyecto, name='crearProyecto'),
]