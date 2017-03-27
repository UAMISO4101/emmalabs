from django import forms

from solicitud.models import Solicitud

# Formulario de una solicitud
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