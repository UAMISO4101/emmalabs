from django import forms

from .models import Solicitud

class SolicitudForm(forms.ModelForm):

    class Meta:
        model = Solicitud

        fields = [
            'titulo',
            'texto',
            'asistente',
            'cientifico',
        ]
        labels = {
            'titulo' : 'Titulo',
            'texto' : 'Texto',
            'asistente' : 'Asistente',
            'cientifico' : 'Cientifico',
        }
        widgets = {
            'texto': forms.Textarea,
        }