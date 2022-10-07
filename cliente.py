import persona

Persona = persona.Persona


class Cliente(Persona):  # ID_CLIENTE = DNI
    def __init__(self, id, dni, nombres, apellidos, correo_cliente, edad, sexo, status):
        super().__init__(id, dni, nombres, apellidos, edad, sexo)
        self.correo = correo_cliente
        self.edad = edad
        self.sexo = sexo
        self.status = status

    def transacciones():
        pass
    def iniciarSesion():
        pass
    def actualizarDatos():
        pass
    def bloqueoTarjeta():
        pass
    
