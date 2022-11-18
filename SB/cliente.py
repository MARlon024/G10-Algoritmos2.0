from persona import *


class Cliente(Persona):
    def __init__(self, dni, nom, ape_pa, ape_ma, correo, fecha, cel, cel_ope, num_cuenta, status):
        super().__init__(dni, nom, ape_pa, ape_ma,
                         correo, fecha, cel, cel_ope)
        self.num_cuenta = num_cuenta
        self.status = status

    def iniciar_sesion():
        pass

    def __operaciones(self):
        pass
