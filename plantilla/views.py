from django.shortcuts import render

import usuario.views as UsuarioView
from usuario.models import LoginForm, Usuario

# Create your views here.

def index(request):
    form_login = LoginForm()
    lista_menu = []
    usuario_parametro = ''

    if request.user.is_authenticated:
        lista_menu = UsuarioView.crearMenu(request.user)
        # Cargar el usuario activo
        usuario_parametro = Usuario.objects.get(user_id=request.user.id)

    context = {'form_login': form_login,
               'lista_menu': lista_menu,
               'usuario_parametro': usuario_parametro
               }

    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def post(request):
    return render(request, 'post.html')
