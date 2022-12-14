from django.db import models

class DatosGenerales(models.Model):
    id = models.CharField(max_length = 10, primary_key=True)
    nombres = models.CharField(max_length=50)
    dni = models.IntegerField()
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    correo = models.EmailField()
    fecha_nacimiento = models.DateField()
    num_celular = models.IntegerField()
    sexo = models.CharField(max_length=10)
    edad = models.IntegerField()
    domicilio = models.TextField()

class Tarjeta(models.Model):
    #null = True -> permite los casilleros vacíos
    #on_delete = si se borra una persona, se borra la info de la tarjeta
    persona = models.ForeignKey(DatosGenerales, null = True, blank = True, on_delete = models.CASCADE)
    num_tarjeta = models.IntegerField()
    fecha_vencimiento = models.DateField()
    ccv = models.IntegerField()

class SesionWeb(models.Model):
    persona = models.OneToOneField(DatosGenerales, null = True, blank = True, on_delete = models.CASCADE)
    web_password = models.CharField(max_length = 6)
#   contador
#   boleta

class Transferencias(models.Model):
    ingresar_usuario = models.CharField(max_length = 150, default = None)
    ingresar_cuenta_destino = models.IntegerField()
    ingresar_monto = models.IntegerField()
