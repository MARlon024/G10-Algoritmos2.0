import funciones
from SQL.transaccion import pago_servicios
from SQL.cuenta import Cuenta

def pagos_servicios():
    num_cuenta = input("Ingrese la cuenta deudora: \n")
    num_cuenta = num_cuenta.strip()
    num_cuenta = funciones.comprobar_ingreso(num_cuenta, 14)
    cuenta = Cuenta(num_cuenta)
    if cuenta.existe_cuenta():
        saldo = cuenta.obtener_saldo()
        pago_servicio = pago_servicios(num_cuenta, saldo)
        deudas = pago_servicio.devolver_deudas()
        if funciones.existe_lista(deudas):
            funciones.mostrar_deudas(deudas)
            try:
                codigo_deuda = funciones.ingreso_deuda()
                pago_servicio.set_cod_deuda(codigo_deuda)
                if not pago_servicio.existe_deuda():
                    print("\n Este codigo no existe...\n \n")
                else:
                    monto = pago_servicio.deuda_monto()
                    pago_servicio.set_monto(monto)
                    if pago_servicio.monto_valido():
                        pago_servicio.operacion()
                        print("¡Servicio cancelado! \n")
                        fecha, hora = funciones.obtener_tiempo()
                        ID = "3" + funciones.generar_numero(9)
                        pago_servicio.set_id(ID)
                        while pago_servicio.existe_id():
                            ID = "3" + funciones.generar_numero(9)
                            pago_servicio.set_id(ID)
                        funciones.mostrar_servicio(ID, fecha, hora)
                        lista = funciones.exportar_servicio(ID, codigo_deuda, num_cuenta, monto, fecha, hora)
                        pago_servicio.set_lista(lista)
                        pago_servicio.mandar_datos()
                        pago_servicio.cerrar_conexion()
            except ValueError:
                print("ERROR. No puede ingresar un monto que no sea un número.\n\n")
        else:
            print("\n ¡Felicitaciones! Usted no tiene ninguna deuda... \n \n")