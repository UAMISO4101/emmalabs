# coding=utf-8
from django.contrib import auth
from django.contrib import messages
from django.http import HttpResponseRedirect

from usuario.models import LoginForm, Usuario, MenuPorRol


# Create your views here.
def login(request):
    form_login = LoginForm()

    if request.method == 'POST':

        form_login = LoginForm(request.POST)

        username = request.POST.get('username_login')
        password = request.POST.get('password_login')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "Bienvenido al sistema: {}".format(username), extra_tags="alert-success")
            #  return HttpResponseRedirect('/')
        else:
            messages.error(request, "¡El usuario o la contraseña son incorrectos!", extra_tags="alert-danger")
            # return HttpResponseRedirect('/')

    context = {'form_login': form_login,
               'username': username}

    return HttpResponseRedirect('/', context)


def crearMenu(user_param):
    # Inicializa variable temporal
    lista_opciones = []

    # Cargar el usuario activo
    usuario_parametro = Usuario.objects.get(user_id=user_param.id)
    print "Usuario= ", user_param.username, " rol= ", usuario_parametro.rol_usuario.rol

    # Consultar el menu segun el rol del usuario
    consulta_roles = MenuPorRol.objects.filter(rol=usuario_parametro.rol_usuario.id)

    # Agregar opciones al meni
    for i in consulta_roles:
        lista_opciones.append(i.menu)

    return list(set(lista_opciones))


def logout(request):
    auth.logout(request)
    messages.info(request, "Cerraste sesión exitosamente", extra_tags="alert-info")
    return HttpResponseRedirect('/')
