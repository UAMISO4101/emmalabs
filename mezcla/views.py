# coding=utf-8
from django.contrib import messages
from django.shortcuts import render

import usuario.views as UsuarioView
from insumo.models import Insumo
from maquina.models import Maquina
from mezcla.models import Mezcla
from resultado.models import Resultado
from usuario.models import Usuario


def registrarMezcla(request, id):
    # Crear el menu del usuario
    lista_menu = UsuarioView.crearMenu(request.user)
    # Cargar el usuario activo
    usuario_parametro = Usuario.objects.get(user_id=request.user.id)

    if (request.method == "POST"):
        resultado = request.POST['resultado']
        insumo = request.POST['insumo']
        descripcion = request.POST['descripcion']
        maquina = request.POST['maquina']

        mezcla = Mezcla()
        mezcla.descripcion = descripcion
        mezcla.resultado = Resultado.objects.get(id=resultado)
        mezcla.maquina = Maquina.objects.get(id=maquina)
        mezcla.save()
        mezcla.insumos.add(Insumo.objects.get(id=insumo))
        mezcla.save()

        messages.success(request, "Resultado guardado", extra_tags="alert-success")

    resultado = Resultado.objects.get(id=id)
    insumos = Insumo.objects.all()
    maquinas = Maquina.objects.all()

    context = {
        'resultado': resultado,
        'insumos': insumos,
        'maquinas': maquinas,
        'lista_menu': lista_menu,
        'usuario_parametro': usuario_parametro,
    }

    return render(request, 'registrar_mezcla.html', context)
