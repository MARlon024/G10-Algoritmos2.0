from django.db import models

class DatosGenerales(models.Model):
    nombres = models.CharField(max_length=50)
    dni = models.IntegerField()
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    correo = models.EmailField()
    fecha_nacimiento = models.DateField()
    num_celular = models.IntegerField()
    sexo = models.CharField(max_length=10)
    edad = models.IntegerField()
    domicilio = models.CharField(max_length=50)

class Estado(models.Model):
    numero_cuenta = models.IntegerField()        
    nombre_usuario = models.CharField(max_length = 10, primary_key=True)
    dinero = models.IntegerField()

class SesionWeb(models.Model):
    persona = models.OneToOneField(DatosGenerales, null = True, blank = True, on_delete = models.CASCADE)
    web_password = models.CharField(max_length = 6)
#   contador
#   boleta