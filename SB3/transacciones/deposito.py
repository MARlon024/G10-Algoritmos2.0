import funciones_banco
from transacciones_SQL.transaccion import Deposito
from transacciones_SQL.cuenta import Cuenta
from consultas.db_obtener_frame import obtener_frame
from PDF.crear_pdf import crear_pdf
# Chequear las variables


def deposito():
    num_cuenta = input("Ingrese la cuenta a depositar \n")
    num_cuenta = num_cuenta.strip()
    num_cuenta = funciones_banco.comprobar_ingreso(num_cuenta, 14)
    cuenta = Cuenta(num_cuenta)
    if cuenta.existe_cuenta():
        saldo = cuenta.obtener_saldo()
        try:
            monto = float(input("Ingrese el monto a depositar \n"))
            deposito = Deposito(num_cuenta, saldo)
            deposito.set_monto(monto)
            deposito.operacion()
            print("¡Depósito completado! \n")
            fecha, hora = funciones_banco.obtener_tiempo()
            id = "0" + funciones_banco.generar_numero(9)
            deposito.set_id(id)
            while deposito.existe_id():
                id = "0" + funciones_banco.generar_numero(9)
                deposito.set_id(id)
            funciones_banco.mostrar_deposito(id, monto, fecha, hora)
            lista = funciones_banco.exportar_deposito(
                id, num_cuenta, monto, fecha, hora)
            deposito.set_lista(lista)
            deposito.mandar_datos()
            deposito.cerrar_conexion()
            # Si quiere crear pdf:
            frame = obtener_frame('depositos',id)
            data_frame = frame.obtener_data_frame()
            pdf = crear_pdf(data_frame)
            pdf.proceso_creacion_pdf()
        except ValueError:
            print("ERROR. No puede ingresar un monto que no sea un número.\n\n")
    else:
        print("Esta cuenta no existe...\n\n")

deposito()
