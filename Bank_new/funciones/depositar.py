from consultas.db_validar_num_cuenta import Db_validar_num_cuenta
from consultas.db_actualizar_dinero import Db_actualizar_dinero
from validaciones.validar_num_cuenta import Validar_num_cuenta
from validaciones.validar_dinero import Validar_dinero

class Depositar:
    def __init__(self):
        self.num_cuenta = input("Intoducir cuenta bancaria: ")
        self.deposito_cuenta()
    def deposito_cuenta(self):
        validar = Validar_num_cuenta(self.num_cuenta)
        if validar.convalidar_num_cuenta() == True:
            validar_exis=Db_validar_num_cuenta(self.num_cuenta, "cuentas_bancarias")
            if validar_exis.existe_cuenta() == True:
                saldo = validar_exis.obtener_saldo()
                monto = input("Ingrese el monto a depositar: ")
                validar_monto = Validar_dinero(monto)
                if validar_monto.convalidar_monto() == True:
                    saldo=saldo+float(monto)
                    actualiza=Db_actualizar_dinero(self.num_cuenta,saldo,"depositos")
                    actualiza.mandar_datos()
                    actualiza.mostrar_comprobante(monto,"depositado")
                else:
                    print("EL MONTO NO ES VALIDO")
            else:
                print("LA CUENTA BANCARIA NO EXISTE")
        else:
            print("NUMERO DE CUENTA NO VALIDO")