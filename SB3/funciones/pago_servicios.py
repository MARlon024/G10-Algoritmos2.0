from consultas.db_validar_num_cuenta import Db_validar_num_cuenta
from consultas.db_actualizar_dinero import Db_actualizar_dinero
from consultas.db_validar_codigo_deuda import Db_validar_codigo_deuda
from consultas.db_actualizar_servicios import Db_actualizar_servicios
from consultas.db_devolver_servicios import Db_devolver_servicios
from validaciones.validar_num_cuenta import Validar_num_cuenta
from validaciones.validar_codigo_deuda import Validar_codigo_deuda
from validaciones.validar_pago_servicios import Validar_pago_servicios


class Pago_servicios:
    def __init__(self):
        self.num_cuenta= input("Introducir cuenta bancaria: ")
        self.pago_servicios_cuenta()

    def pago_servicios_cuenta(self):
        validar_cuenta = Validar_num_cuenta(self.num_cuenta)
        if validar_cuenta.convalidar_num_cuenta():
            validar_existe_cuenta=Db_validar_num_cuenta(self.num_cuenta,"cuentas_bancarias")
            if validar_existe_cuenta.existe_cuenta():
                mostrar_servicios = Db_devolver_servicios(self.num_cuenta)
                mostrar_servicios.imprimir_deudas()
                cod_deuda = input("Introducir código de deuda: ")
                validar_deuda = Validar_codigo_deuda(cod_deuda)
                if validar_deuda.convalidar_codigo_deuda():
                    validar_codigo_deuda = Db_validar_codigo_deuda(cod_deuda)
                    if validar_codigo_deuda.existe_codigo_deuda():
                        saldo = validar_existe_cuenta.obtener_saldo()
                        monto = validar_codigo_deuda.monto_deuda()
                        validar_pago = Validar_pago_servicios(saldo, monto)
                        if validar_pago.validar_pago():
                            saldo = saldo - float(monto)
                            actualiza = Db_actualizar_dinero(self.num_cuenta, saldo, "pago_servicios")
                            actualizar_servicios = Db_actualizar_servicios(cod_deuda)
                            actualizar_servicios.actualizar_servicios()
                            actualiza.mandar_datos()
                            actualiza.mostrar_comprobante(monto, "cancelado su deuda")
                        else:
                            print("No dispone del saldo suficiente para cancelar su deuda . . . \n \n")
                    else:
                        print("El código introducido no existe . . . \n \n")
                else:
                    print("Número de deuda no válido . . . \n \n")
            else:
                print("Esta cuenta bancaria no existe . . .\n \n")
        else:
            print("Número de cuenta no válido . . .\n \n")