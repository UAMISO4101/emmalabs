# -*- coding: utf-8 -*-
from django import forms

from models import Protocolo


class ProtocoloForm(forms.ModelForm):
    class Meta:
        model = Protocolo
        fields = ('nombre', 'descripcion', 'clasificacion')
        labels = {
            'nombre': 'Nombre del protocolo',
            'descripcion': 'Descripción del protocolo',
            'clasificacion': 'Clasificación del protocolo'
        }
        widgets = {
            'descripcion': forms.Textarea
        }
