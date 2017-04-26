# coding=utf-8
from django.shortcuts import render
from django.contrib import messages
from experimento.models import Experimento
from proyecto.models import Proyecto
from protocolo.models import Protocolo
from resultado.models import Resultado
from insumo.models import Insumo
from maquina.models import Maquina
from mezcla.models import Mezcla

def registrarMezcla(request, id):
    if(request.method == "POST"):

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
        'maquinas': maquinas
    }
    return render(request, 'registrar_mezcla.html', context)