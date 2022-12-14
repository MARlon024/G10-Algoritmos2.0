from validaciones.validar_registro_cliente import Validar_registro_cliente

class Bloquear_tarjeta:
    def __init__(self):
        self.dni = input("DNI: ")
        self.clave_tarjeta = input("Clave tarjeta: ")

    def bloquear(self):
        validar = Validar_registro_cliente.convalidar_dni(self.dni)
        pass