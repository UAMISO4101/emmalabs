from django.shortcuts import render
from .models import Insumo

# Metodo para ver el detalle de un insumo
def ver_Insumo(request, id):
    insumo=Insumo.objects.get(id=id)
    context = {
        'insumo': insumo
    }
    return render(request, 'verInsumo.html', context)