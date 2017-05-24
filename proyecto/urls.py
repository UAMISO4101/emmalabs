from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^proyectos/$', views.proyectos, name='proyectos'),
]