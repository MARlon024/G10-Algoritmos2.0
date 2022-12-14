from django import forms
from . import models

class DatosGeneralesForm(forms.ModelForm):
    class Meta:
        model = models.DatosGenerales
        fields = [
            "id",
            "nombres",
            "dni", 
            "apellido_paterno", 
            "apellido_materno", 
            "correo", 
            "fecha_nacimiento", 
            "num_celular", 
            "sexo", 
            "edad", 
            "domicilio",
            ]
