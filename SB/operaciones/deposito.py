import funciones
from SQL.transaccion import Deposito
from SQL.cuenta import Cuenta

def deposito():
    num_cuenta = input("Ingrese la cuenta a depositar \n")
    num_cuenta = num_cuenta.strip()
    num_cuenta = funciones.comprobar_ingreso(num_cuenta, 14)
    cuenta = Cuenta(num_cuenta)
    if cuenta.existe_cuenta():
        saldo = cuenta.obtener_saldo()
        try:
            monto = float(input("Ingrese el monto a depositar \n"))
            deposito = Deposito(num_cuenta, saldo)
            deposito.set_monto(monto)
            deposito.operacion()
            print("¡Depósito completado! \n")
            fecha, hora = funciones.obtener_tiempo()
            ID = "0" + funciones.generar_numero(9)
            deposito.set_id(ID)
            while deposito.existe_id():
                ID = "0" + funciones.generar_numero(9)
                deposito.set_id(ID)
            funciones.mostrar_deposito(ID, monto, fecha, hora)
            lista = funciones.exportar_deposito(ID, num_cuenta, monto, fecha, hora)
            deposito.set_lista(lista)
            deposito.mandar_datos()
            deposito.cerrar_conexion()
        except ValueError:
            print("ERROR. No puede ingresar un monto que no sea un número.\n\n")
    else:
        print("Esta cuenta no existe...\n\n")