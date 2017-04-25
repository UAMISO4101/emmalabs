# coding=utf-8
from django.shortcuts import render
from django.contrib import messages
from experimento.models import Experimento
from proyecto.models import Proyecto
from protocolo.models import Protocolo
from resultado.models import Resultado

def registrarMezcla(request, id):
    if(request.method == "POST"):

        resultados = request.POST['resultados']
        satisfactorio = request.POST['satisfactorio']
        obrevaciones = request.POST['obrevaciones']
        fecha = request.POST['fecha']
        proyecto = request.POST['proyecto']
        experimento = request.POST['experimento']
        protocolo = request.POST['protocolo']

        resultado = Resultado()
        resultado.resultado = resultados
        resultado.satisfactorio = satisfactorio
        resultado.observaciones = obrevaciones
        resultado.fecha_resultado = fecha
        resultado.proyecto = Proyecto.objects.get(id=proyecto)
        resultado.experimento = Experimento.objects.get(id=experimento)
        resultado.protocolo = Protocolo.objects.get(id=protocolo)
        resultado.save()
        messages.success(request, "Resultado guardado", extra_tags="alert-success")

    experimento = Experimento.objects.get(id=id)
    proyectos = Proyecto.objects.all()
    protocolos = Protocolo.objects.all()
    context = {
        'experimento': experimento,
        'proyectos' : proyectos,
        'protocolos' : protocolos
    }
    return render(request, 'registrar_mezcla.html', context)