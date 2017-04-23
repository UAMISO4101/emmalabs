from django.shortcuts import render

# Create your views here.
from .models import Orden


def ordenes(request):
    lista_ordenes = Orden.objects.all()

    context = {'lista_ordenes': lista_ordenes}
    return render(request, 'ordenes.html', context)

def aprobar_orden(request, id):
    orden = Orden.objects.get(id=id)
    orden.estado = 1
    orden.save()

    orden = Orden.objects.get(id=id)

    context = {
        'orden': orden
    }
    return render(request, 'detalle_orden.html', context)

def detalleOrden(request, id):
    """if(request.method == "POST"):
        resultado = request.POST['resultado']
        id = request.POST['orden_id']
        orden = Orden.objects.get(id=id)
        orden.resultado = resultado
        orden.save()"""
    orden = Orden.objects.get(id=id)
    context = {
        'orden': orden
    }
    return render(request, 'detalle_orden.html', context)