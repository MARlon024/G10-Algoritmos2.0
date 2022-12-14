from django import forms
from . import models

class TransferenciasForm(forms.ModelForm):
    class Meta:
        model = models.Transferencias
        fields = [
            "ingresar_usuario",
            "ingresar_numero_cuenta_destino",
            "ingresar_monto",
            ]
