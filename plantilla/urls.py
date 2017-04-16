from django.conf.urls import url

from usuario.views import login, logout
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^index.html/$', views.index),
    url(r'^about.html/$', views.about),
    url(r'^contact.html/$', views.contact),
    url(r'^post.html/$', views.post),
    url(r'^login$', login),
    url(r'^logout$', logout)
]
