import datetime
from random import randint
def menuPrincipal():
    print("\t \t  Bienvenido al panel de transacciones. Ingrese la opción a continuar: \n 1. Transferencia \n 2. Retiro \n 3. Pago de servicios \n 0. Salir")
    opc = int(input("\n"))
    return opc

def ingresoCuenta(cuentaInicial):
    cuentaDestino = cuentaInicial
    while(len(cuentaDestino)!=14 or cuentaDestino.isnumeric() == False or cuentaDestino == cuentaInicial):
        cuentaDestino = input("Introduzca el número de cuenta a la que va a depositar: \n")
        if(len(cuentaDestino)!=14):
            print("La cuenta debe contener 14 dígitos... \n")
        if(cuentaDestino.isnumeric() == False):
            print("Debe ingresar solo números... \n")
        if(cuentaDestino == cuentaInicial):
            print("No puede transferirse a usted mismo... \n ")
    return cuentaDestino

def obtenerTiempo():
    ahora = datetime.datetime.now()
    fechaActual = datetime.datetime.strftime(ahora, "%Y-%m-%d")
    horaActual = datetime.datetime.strftime(ahora, "%H:%M:%S")
    return fechaActual, horaActual

def mostrarTransferencia(cuenta, monto, ID, fecha, hora):
    print("\t \t Destinatario: \t \t \t Por el monto de:")
    print(f"\t \t {cuenta} \t \t \t {monto} \n")
    print(f"\t \t \t \t \t Fecha:")
    print(f"\t \t {fecha} \t \t {hora} \n")
    print(f"\t NÚMERO DE OPERACIÓN: {ID} \n \n")

def mostrarRetiro(monto, saldo, ID, fecha, hora):
    print(f"\t \t \t Usted ha retirado: \t S/. {monto}")
    print(f"\t \t Su nuevo saldo es: {saldo} \n")
    print(f"\t \t \t FECHA:")
    print(f"\t \t {fecha} \t \t {hora}\n")
    print(f"\t NÚMERO DE OPERACIÓN: {ID} \n \n")

def exportarTransferencia( ID, cuentaInicial, cuentaDestino, monto, fecha, hora):
    lista = [ID, cuentaInicial, cuentaDestino, monto, fecha, hora]
    return lista

def exportarRetiro(ID, cuenta, monto, fecha, hora):
    lista = [ID, cuenta, monto, fecha, hora]
    return lista

def crearID():
    ID = ""
    for i in range(9):
        p = str(randint(0, 9))
        ID = ID + p
    return ID