from SB import funciones
from SB.SQL.transaccion import Transferencia
from SB.SQL.cuenta import Cuenta

def transferencia():
    cuenta_origen = input("Ingrese la cuenta origen: \n")
    cuenta_origen = cuenta_origen.strip()
    cuenta_origen = funciones.comprobar_ingreso(cuenta_origen, 14)
    cuenta = Cuenta(cuenta_origen)
    if(cuenta.existe_cuenta()):
        saldo = cuenta.obtener_saldo()
        cuenta_destino = funciones.ingreso_cuenta(cuenta_origen)
        transferencia = Transferencia(cuenta_origen, saldo)
        transferencia.set_destino(cuenta_destino)
        if transferencia.existe_cuenta():
            try:
                monto = float(input("Ingrese el monto a depositar: \n"))
                transferencia.set_monto(monto)
                if transferencia.monto_valido():
                    transferencia.operacion()
                    print("¡Transacción completada!\n")
                    fecha, hora = funciones.obtener_tiempo()
                    ID = "1" + funciones.generar_numero(9)
                    transferencia.set_id(ID)
                    while transferencia.existe_id():
                        ID = "1" + funciones.generar_numero(9)
                        transferencia.set_id(ID)
                    funciones.mostrar_transferencia(cuenta_destino, monto, ID, fecha, hora)
                    lista = funciones.exportar_transferencia(ID, cuenta_origen, cuenta_destino, monto, fecha,hora)
                    transferencia.set_lista(lista)
                    transferencia.mandar_datos()
                    transferencia.cerrar_conexion()
            except ValueError:
                print("ERROR. No puede ingresar un monto que no sea un número.\n\n")