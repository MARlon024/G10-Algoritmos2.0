from persona import Persona

class Cliente(Persona):
    def __init__(self, __nom, __dni, __ape_pa, __ape_ma, __correo, __fecha, __cel, __cel_ope,__ncuenta,__clave):
        super().__init__(__nom, __dni, __ape_pa, __ape_ma, __correo, __fecha, __cel, __cel_ope)
        self.ncuenta=__ncuenta
        self.clave=__clave