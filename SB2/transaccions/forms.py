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
            
class Depositos_RetirosForm(forms.ModelForm):
    class Meta:
        model = models.Depositos_Retiros
        fields = [
            "ingresar_usuario",
            "ingresar_monto"
            ]
