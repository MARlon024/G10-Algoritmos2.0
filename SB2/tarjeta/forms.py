from django import forms
from . import models

class TarjetaForm(forms.ModelForm):
    class Meta:
        model = models.Tarjeta
        fields = [
            "persona",
            "num_tarjeta", 
            "fecha_vencimiento", 
            "ccv",
            ]

