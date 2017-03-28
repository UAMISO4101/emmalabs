# -*- coding: utf-8 -*-
import datetime
from django import forms
from functools import partial
from .models import Protocolo, ClasificacionProtocolo


class MyModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.nombre_clasificacion


class ProtocoloForm(forms.ModelForm):
    # Elemento para inicializar el selector de fechas
    DateInput = partial(forms.DateInput, {'class': 'datepicker'})
    # Campos de búsqueda
    fecha_creacion = forms.DateField(widget=DateInput(), required=False, label='Fecha de creacion')
    clasificacion = MyModelChoiceField(queryset=ClasificacionProtocolo.objects.all(),
                                       empty_label='Seleccione una clasificacion...',
                                       to_field_name='nombre_clasificacion',
                                       label='Clasificacion',
                                       required=False)
    codigo = forms.CharField(max_length=50, label='Codigo', required=False)

    class Meta:
        model = Protocolo
        fields = ('nombre',)
        labels = {
            'nombre': 'Nombre:',
        }
