from django.conf.urls import url

from plantilla_nueva import views
from usuario.views import login, logout

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^index$', views.index, name='index'),
    url(r'^login$', login, name='login'),
    url(r'^logout$', logout, name='logout')
]
