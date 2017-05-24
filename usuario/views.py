# coding=utf-8
from django.contrib import auth
from django.contrib import messages
from django.http import HttpResponseRedirect

from usuario.models import LoginForm, Usuario, MenuPorRol, ItemMenu, OpcionMenu


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
            #  return HttpResponseRedirect('/')
        else:
            messages.error(request, "¡El usuario o la contraseña son incorrectos!", extra_tags="alert-danger")
            # return HttpResponseRedirect('/')

    context = {
        'form_login': form_login,
        'username': username,
    }

    return HttpResponseRedirect('/', context)


def crearMenu(user_param):
    # Inicializa variables temporales
    lista_encabezados = []
    lista_menu = []

    # Cargar el usuario activo
    usuario_parametro = Usuario.objects.get(user_id=user_param.id)
    # print("ID Usuario=", user_param.id, "Rol_id=", usuario_parametro.rol_usuario.id)

    # Consultar encabezados del menu segun el rol del usuario
    consulta_encabezados = MenuPorRol.objects.filter(rol=usuario_parametro.rol_usuario.id)

    # Agregar encabezados del menu
    for i in consulta_encabezados:
        lista_encabezados.append(i.menu)

    # Inicializa los objetos del menu con encabezados
    for j in set(lista_encabezados):
        item = ItemMenu()
        item.menu = j
        lista_menu.append(item)

    # Consultar opciones del menu
    consulta_opciones = MenuPorRol.objects.filter(rol_id=usuario_parametro.rol_usuario.id)

    # Agregar opcion al encabezado
    for j in lista_menu:
        temp = []
        for k in consulta_opciones:
            if k.menu == j.menu:
                opcion = OpcionMenu()
                opcion.opcion = k.opcion
                opcion.template = k.template
                temp.append(opcion)
        j.opciones = temp

    return lista_menu


def logout(request):
    auth.logout(request)
    messages.info(request, "Cerraste sesión exitosamente", extra_tags="alert-info")
    return HttpResponseRedirect('/')
