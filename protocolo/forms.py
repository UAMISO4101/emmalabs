# -*- coding: utf-8 -*-
from django import forms

from .models import Protocolo, ClasificacionProtocolo


class MyModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.nombre_clasificacion


class ProtocoloForm(forms.ModelForm):
    # Campos de búsqueda
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


class CrearProtocoloForm(forms.ModelForm):
    class Meta:
        model = Protocolo

        fields = [
            'nombre',
            'descripcion',
            'insumos',
            'codigo',
            'clasificacion',
            'observaciones',
        ]
        labels = {
            'nombre': 'Nombre',
            'codigo': 'Código',
            'clasificacion': 'Clasificación',
            'descripcion': 'Lista de pasos',
            'insumos': 'Insumos',
            'observaciones': 'Observaciones',
        }
        widgets = {
            'descripcion': forms.Textarea,
            'observaciones': forms.Textarea,
        }


class ActualizarProtocoloForm(forms.ModelForm):
    class Meta:
        model = Protocolo

        fields = [
            'descripcion',
            'insumos',
            'clasificacion',
            'observaciones',
        ]
        labels = {
            'clasificacion': 'Clasificacion',
            'descripcion': 'Lista de pasos',
            'insumos': 'Insumos',
            'observaciones': 'Observaciones',
        }
        widgets = {
            'descripcion': forms.Textarea,
            'observaciones': forms.Textarea,
        }
