# coding=utf-8
from django.shortcuts import render

import usuario.views as UsuarioView
from experimento.models import Experimento
from proyecto.models import Proyecto
from usuario.models import Usuario


def detalleProyecto(request, id):
    # Inicializar variables
    lista_menu = UsuarioView.crearMenu(request.user)
    # Cargar el usuario activo
    usuario_parametro = Usuario.objects.get(user_id=request.user.id)

    if (request.method == "POST"):
        resultado = request.POST['resultado']
        id = request.POST['experimento_id']
        experimento = Experimento.objects.get(id=id)
        experimento.resultado = resultado
        experimento.save()

    proyecto = Proyecto.objects.get(id=id)

    context = {
        'proyecto': proyecto,
        'lista_menu': lista_menu,
        'usuario_parametro': usuario_parametro,
    }
    return render(request, 'detalle_proyecto.html', context)
