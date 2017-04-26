# coding=utf-8
from django.shortcuts import render
from django.contrib import messages
from experimento.models import Experimento
from proyecto.models import Proyecto
from protocolo.models import Protocolo

def registrarMezcla(request, id):
    if(request.method == "POST"):

        resultados = request.POST['resultados']
        satisfactorio = request.POST['satisfactorio']
        obrevaciones = request.POST['obrevaciones']
        fecha = request.POST['fecha']
        proyecto = request.POST['proyecto']
        experimento = request.POST['experimento']
        protocolo = request.POST['protocolo']
        messages.success(request, "Resultado guardado", extra_tags="alert-success")

    experimento = Experimento.objects.all()
    proyectos = Proyecto.objects.all()
    protocolos = Protocolo.objects.all()
    context = {
        'experimento': experimento,
        'proyectos' : proyectos,
        'protocolos' : protocolos
    }
    return render(request, 'registrar_mezcla.html', context)