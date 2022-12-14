from django.db import models

class Transferencias(models.Model):
    ingresar_usuario = models.CharField(max_length = 150, default = None)
    ingresar_numero_cuenta_destino = models.IntegerField()
    ingresar_monto = models.IntegerField()

class Depositos_Retiros(models.Model):
    ingresar_usuario = models.CharField(max_length = 150, default = None)
    ingresar_monto = models.IntegerField()