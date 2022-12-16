import getpass
from validaciones.validar_registro_cliente import Validar_registro_cliente
from consultas.db_validar_cliente import Db_validar_cliente
from consultas.db_buscar_num_cuenta import Db_buscar_num_cuenta
from consultas.db_validar_tarjeta import Db_validar_tarjeta
from consultas.db_devolver_num_cuenta import Db_devolver_num_cuenta
from consultas.db_bloquear_tarjeta import Db_bloquear_tarjeta
class Bloquear_tarjeta:
    def __init__(self):
        self.dni = input("DNI: ")
        self.clave_tarjeta = getpass(input("Clave tarjeta: "))
        self.bloquear()

    def bloquear(self):
        validar = Validar_registro_cliente(self.dni)
        if validar.convalidar_dni() == True:
            db_validar = Db_validar_cliente(self.dni)
            if db_validar.existe_cuenta_cliente() == True:
                db_buscar = Db_buscar_num_cuenta(self.dni)
                if db_buscar.buscar() == True:
                    db_devolver_cuenta = Db_devolver_num_cuenta(self.dni)
                    num_cuenta = db_devolver_cuenta.devolver_num_cuenta()
                    db_tarjeta = Db_validar_tarjeta(num_cuenta)
                    if db_tarjeta.existe_tarjeta() == True:
                        db_bloquear = Db_bloquear_tarjeta(num_cuenta)
                        return db_bloquear.bloquear()
                    else:
                        return "NO EXISTE TARJETA"
        else:
            print("DNI INVALIDO")