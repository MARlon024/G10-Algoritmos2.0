from validaciones.validar_num_cuenta import Validar_num_cuenta
from validaciones.validar_dinero import Validar_dinero
from consultas.db_transferencias import Db_transferencias
from consultas.db_validar_num_cuenta import Db_validar_num_cuenta

class Transferencias:
    def __init__(self):
        self.num_cuenta_desde = input("Intoducir cuenta bancaria: ")
        self.num_cuenta_hasta = input("Intoducir cuenta bancaria a transferir: ")
        self.retiro_cuenta()
    def retiro_cuenta(self):
        validar_desde = Validar_num_cuenta(self.num_cuenta_desde)
        validar_hasta = Validar_num_cuenta(self.num_cuenta_hasta)
        if validar_desde.convalidar_num_cuenta() == True and validar_hasta.convalidar_num_cuenta():
            validar_exis_desde=Db_validar_num_cuenta(self.num_cuenta_desde, "cuentas_bancarias")
            validar_exis_hasta=Db_validar_num_cuenta(self.num_cuenta_hasta, "cuentas_bancarias")
            if validar_exis_desde.existe_cuenta() == True and validar_exis_hasta.existe_cuenta() == True:
                saldo = validar_exis_desde.obtener_saldo()
                monto = input("Ingrese el monto a retirar: ")
                validar_monto = Validar_dinero(monto)
                if validar_monto.convalidar_monto() == True:
                    validar_retiro= Validar_dinero(saldo)
                    if validar_retiro.convalidar_operacion(float(monto)) == True:
                        actualiza=Db_transferencias(self.num_cuenta_desde,self.num_cuenta_hasta,float(monto),"transferencias")
                        actualiza.mandar_datos()
                        actualiza.mostrar_comprobante("transferido")
                    else:
                        print("Saldo insuficiente")
                else:
                    print("EL MONTO NO ES VALIDO")
            else:
                print("ERROR EN LAS CUENTAS BANCARIAS")
        else:
            print("NUMERO DE CUENTA NO VALIDO")