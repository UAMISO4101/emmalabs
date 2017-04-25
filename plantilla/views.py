from django.shortcuts import render

import usuario.views as UsuarioView
from usuario.models import LoginForm


# Create your views here.

def index(request):
    form_login = LoginForm()
    lista_permisos = []

    if request.user.is_authenticated:
        lista_permisos = UsuarioView.crearMenu(request.user)

    context = {'form_login': form_login,
               'lista_permisos': lista_permisos
               }

    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def post(request):
    return render(request, 'post.html')
