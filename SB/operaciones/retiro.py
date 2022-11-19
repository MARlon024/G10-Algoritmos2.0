import funciones
from SQL.transaccion import Retiro
from SQL.cuenta import Cuenta

def retiro():
    num_cuenta = input("Ingrese la cuenta a retirar: \n")
    num_cuenta = num_cuenta.strip()
    num_cuenta = funciones.comprobar_ingreso(num_cuenta, 14)
    cuenta = Cuenta(num_cuenta)
    if cuenta.existe_cuenta():
        saldo = cuenta.obtener_saldo()
        try:
            monto = float(input("Ingrese el monto a retirar \n"))
            retiro = Retiro(num_cuenta, saldo)
            retiro.set_monto(monto)
            if retiro.monto_valido():
                retiro.operacion()
                print("¡Retiro completado!\n")
                fecha, hora = funciones.obtener_tiempo()
                ID = "2" + funciones.generar_numero(9)
                retiro.set_id(ID)
                while retiro.existe_id():
                    ID = "2" + funciones.generar_numero(9)
                    retiro.set_id(ID)
                funciones.mostrar_retiro(monto, cuenta.obtener_saldo(), ID, fecha, hora)
                lista = funciones.exportar_retiro(ID, num_cuenta, monto, fecha, hora)
                retiro.set_lista(lista)
                retiro.mandar_datos()
                retiro.cerrar_conexion()
        except ValueError:
            print("ERROR. No puede ingresar un monto que no sea un número.\n\n")
    else:
        print("Esta cuenta no existe...\n\n")