from django import forms
from . import models

class DatosGeneralesForm (forms.ModelForm):
    # class to store all the model form fields from models.py
    class Meta:
        model = models.DatosGenerales
        fields = ["id", "nombres", "dni", "apellido_paterno", "apellido_materno", "correo", "fecha_nacimiento", "num_celular", "sexo", "edad", "domicilio"]

class Tarjeta (forms.ModelForm):
    class Meta:
        model = models.Tarjeta
        fields = ["persona", "num_tarjeta", "fecha_vencimiento", "ccv"]

class SesionWeb (forms.ModelForm):
    class Meta:
        model = models.SesionWeb
        fields = ["persona", "web_password"]

class Transferencias(forms.ModelForm):
    class Meta:
        model = models.Transferencias
        fields = ["ingresar_usuario", "ingresar_cuenta_destino", "ingresar_monto"]
