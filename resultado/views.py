# coding=utf-8
from datetime import datetime

from django.contrib import messages
from django.shortcuts import render

import usuario.views as UsuarioView
from experimento.models import Experimento
from protocolo.models import Protocolo
from proyecto.models import Proyecto
from resultado.models import Resultado
from usuario.models import Usuario


def registrarResultado(request, id):
    # Crear el menu del usuario
    lista_menu = UsuarioView.crearMenu(request.user)
    # Cargar el usuario activo
    usuario_parametro = Usuario.objects.get(user_id=request.user.id)

    if (request.method == "POST"):

        resultados = request.POST['resultados']
        satisfactorio = request.POST['satisfactorio']
        observaciones = request.POST['observaciones']
        fecha = datetime.strptime(request.POST['fecha'], "%m/%d/%Y")
        proyecto = request.POST['proyecto']
        experimento = request.POST['experimento']
        protocolo = request.POST['protocolo']

        resultado = Resultado()
        resultado.detalle_resultado = resultados
        resultado.satisfactorio = satisfactorio
        resultado.observaciones = observaciones
        resultado.fecha_resultado = fecha
        resultado.proyecto = Proyecto.objects.get(id=proyecto)
        resultado.experimento = Experimento.objects.get(id=experimento)
        resultado.protocolo = Protocolo.objects.get(id=protocolo)
        resultado.save()
        messages.success(request, "Resultado guardado", extra_tags="alert-success")

    experimento = Experimento.objects.get(id=id)
    resultados = Resultado.objects.filter(experimento=experimento)
    proyectos = Proyecto.objects.all()
    sqlProtocolos = "SELECT * FROM public.protocolo_protocolo pro2 INNER JOIN(SELECT MAX(pro.version) as version, pro.nombre as nombre FROM public.protocolo_protocolo pro GROUP BY pro.nombre)  sq ON (pro2.nombre = sq.nombre AND pro2.version = sq.version)"
    protocolos = Protocolo.objects.raw(sqlProtocolos)  # Protocolo.objects.all().values('nombre', 'version').annotate(Max('version'))

    context = {
        'experimento': experimento,
        'proyectos': proyectos,
        'protocolos': protocolos,
        'resultados': resultados,
        'usuario_parametro': usuario_parametro,
        'lista_menu': lista_menu,
    }

    return render(request, 'registrar_resultado.html', context)
