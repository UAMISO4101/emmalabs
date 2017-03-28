from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^proyectos/(\d+)/$', views.detalleProyecto),
]