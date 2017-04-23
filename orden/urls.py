from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^ordenes/$', views.ordenes),
    url(r'^ordenes/(\d+)/$', views.detalleOrden),
    url(r'^ordenes/actualizar/(\d+)/$', views.aprobar_orden)
]