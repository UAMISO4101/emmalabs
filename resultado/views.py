# coding=utf-8
from django.shortcuts import render
from experimento.models import Experimento
from proyecto.models import Proyecto
from protocolo.models import Protocolo

def registrarResultado(request, id):
    if(request.method == "POST"):
        resultado = request.POST['resultado']
        id = request.POST['experimento_id']
        experimento = Experimento.objects.get(id=id)
        experimento.resultado = resultado
        experimento.save()
    experimento = Experimento.objects.get(id=id)
    proyectos = Proyecto.objects.all()
    protocolos = Protocolo.objects.all()
    context = {
        'experimento': experimento,
        'proyectos' : proyectos,
        'protocolos' : protocolos
    }
    return render(request, 'registrar_resultado.html', context)