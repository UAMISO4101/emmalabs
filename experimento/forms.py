from django import forms

from experimento.models import Experimento

# Formulario de una solicitud
class ExperimentoForm(forms.ModelForm):
    class Meta:
        model = Experimento

        fields = [
            'nombre',
            'descripcion',
            'estado',
            'resultado',
            'protocolos',
        ]
        labels = {
            'nombre' : 'Nombre del experimento',
            'descripcion' : 'Describa el experimento',
            'estado' : 'Defina un estado inicial',
            'resultado' : 'Resultado del experimento (si aplica estado inicial):',
            'protocolos' : 'Protocolos a utilizar:',
        }
        widgets = {
            'texto': forms.Textarea,
        }