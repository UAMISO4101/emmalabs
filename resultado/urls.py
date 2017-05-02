from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^registrar_resultado/(\d+)/$', views.registrarResultado)
]