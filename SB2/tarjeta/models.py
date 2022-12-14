from django.db import models
from profiles.models import DatosGenerales

class Tarjeta(models.Model):
    persona = models.ForeignKey(DatosGenerales, null = True, blank = True, on_delete = models.CASCADE)
    num_tarjeta = models.IntegerField()
    fecha_vencimiento = models.DateField()
    ccv = models.IntegerField()