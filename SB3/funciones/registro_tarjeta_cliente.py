import uuid
from generador.generar import Generar
from validaciones.validar_num_cuenta import Validar_num_cuenta
from consultas.db_validar_num_cuenta import Db_validar_num_cuenta
from consultas.db_registrar_tarjeta import Db_registrar_tarjeta

class Registro_tarjeta_cliente:
    def __init__(self):
        self.id_tarjeta = str(uuid.uuid1())
        self.num_cuenta = input("Introducir numero de cuenta: ")
        tarjeta = Generar(self.num_cuenta)
        self.datos_tarjeta = tarjeta.generar_tarjeta()
        return self.registrar_tarjeta()

    def registrar_tarjeta(self):
        validar = Validar_num_cuenta(self.num_cuenta)
        if validar.convalidar_num_cuenta() == True:
            db_validar = Db_validar_num_cuenta(self.num_cuenta, "tarjeta")
            if db_validar.existe_cuenta() == False:
                registrar =  Db_registrar_tarjeta(self.datos_tarjeta)
                return registrar.registrar_tarjeta()
            else:
                print("LA CUENTA YA ESTA ASOCIADA A UNA TARJETA") 
        else:
            print("EL NUMERO DE CUENTA NO ES VALIDO")
        