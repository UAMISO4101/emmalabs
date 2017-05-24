from django import forms

from proyecto.models import Proyecto

# Formulario de una solicitud
class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto

        fields = [
            'nombre',
            'descripcion',
            'estado',
            'asistentes',
        ]
        labels = {
            'nombre' : 'Nombre del proyecto',
            'descripcion' : 'Describa el proyecto',
            'estado' : 'Defina un estado inicial',
            'asistentes' : 'Asignado a:',
        }
        widgets = {
            'texto': forms.Textarea,
        }