from persona import Persona


class Cliente(Persona):
    def __init__(self, __nom, __dni, __ape_pa, __ape_ma, __correo, __fecha, __cel, __cel_ope,__codigo_recep,__clave_recep,__status):
        super().__init__(__nom, __dni, __ape_pa, __ape_ma, __correo, __fecha, __cel, __cel_ope)
        self.codigo_recep=__codigo_recep
        self.clave_recep=__clave_recep
        self.status=__status
        