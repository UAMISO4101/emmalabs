from django.conf.urls import url
from . import views

urlpatterns = [
    #url para ver detalle de un insumo
    url(r'^insumos/(\d+)/$', views.ver_Insumo, name='verInsumo')
]