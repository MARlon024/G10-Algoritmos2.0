import datetime
from random import randint


def menu_principal():
    print("\t \t  Bienvenido al panel de transacciones. Ingrese la opción a continuar: \n 1. Depósito \n 2. Transferencia \n 3. Retiro \n 4. Pago de servicios \n 0. Salir")
    opc = int(input("\n"))
    return opc

def comprobar_ingreso(variable, digitos):
    while (len(variable) != digitos or variable.isnumeric() == False):
        variable = input("ERROR. Introduzca de nuevo el dato solicitado: \n")
        if (len(variable) != digitos):
            print(f"Debe contener {digitos} dígitos... \n")
        if (variable.isnumeric() == False):
            print("Debe ingresar solo números... \n")
    return variable
def ingreso_cuenta(cuentaInicial):
    cuentaDestino = cuentaInicial
    while (len(cuentaDestino) != 14 or cuentaDestino.isnumeric() == False or cuentaDestino == cuentaInicial):
        cuentaDestino = input("Introduzca el número de cuenta a la que va a depositar: \n")
        cuentaDestino = cuentaDestino.strip()
        if (len(cuentaDestino) != 14):
            print("La cuenta debe contener 14 dígitos... \n")
        if (cuentaDestino.isnumeric() == False):
            print("Debe ingresar solo números... \n")
        if (cuentaDestino == cuentaInicial):
            print("No puede transferirse a usted mismo... \n ")
    return cuentaDestino


def ingreso_deuda():
    codigo_deuda = ""
    while (len(codigo_deuda) != 9 or codigo_deuda.isnumeric() == False):
        codigo_deuda = input("Introduzca el código de deuda a pagar: \n")
        if (len(codigo_deuda) != 9):
            print("El código debe contener 9 dígitos... \n")
        if (codigo_deuda.isnumeric() == False):
            print("Debe ingresar solo números... \n")
    return codigo_deuda


def obtener_tiempo():
    ahora = datetime.datetime.now()
    fechaActual = datetime.datetime.strftime(ahora, "%Y-%m-%d")
    horaActual = datetime.datetime.strftime(ahora, "%H:%M:%S")
    return fechaActual, horaActual


def mostrar_transferencia(cuenta, monto, ID, fecha, hora):
    print("\t \t Destinatario: \t \t \t Por el monto de:")
    print(f"\t \t {cuenta} \t \t \t {monto} \n")
    print(f"\t \t \t \t \t Fecha:")
    print(f"\t \t {fecha} \t \t {hora} \n")
    print(f"\t NÚMERO DE OPERACIÓN: {ID} \n \n")


def mostrar_retiro(monto, saldo, ID, fecha, hora):
    print(f"\t \t \t Usted ha retirado: \t S/. {monto}")
    print(f"\t \t Su nuevo saldo es: {saldo} \n")
    print(f"\t \t \t FECHA:")
    print(f"\t \t {fecha} \t \t {hora}\n")
    print(f"\t NÚMERO DE OPERACIÓN: {ID} \n \n")


def mostrar_deudas(deudas):
    print("\n \n Bienvenido. A continuación se muestran sus deudas:")
    print("CODIGO DE DEUDA: \t \t \t EMPRESA: \t \t \t MONTO: \t \t \t FECHA VENCIMIENTO:")
    for i in deudas:
        print(f"{i[0]} \t \t \t \t \t {i[1]} \t \t \t \t {i[2]} \t \t \t \t {i[3]}")


def mostrar_servicio(ID, fecha, hora):
    print(f"\t \t ID DE OPERACIÓN: \n \t \t {ID} \n")
    print(" \t \t \t FECHA:")
    print(f"\t \t {fecha} \t \t {hora}\n \n")


def mostrar_deposito(ID, monto, fecha, hora):
    print(f"\t \t Usted ha depositado: \t \t {monto}\n")
    print(f"\t \t ID de operación: \t \t {ID} \n")
    print(f"\t \t FECHA:")
    print(f"\t \t {fecha} \t \t \t {hora}")


def exportar_deposito(ID, cuenta, monto, fecha, hora):
    lista = [ID, cuenta, monto, fecha, hora]
    return lista


def exportar_transferencia(ID, cuentaInicial, cuentaDestino, monto, fecha, hora):
    lista = [ID, cuentaInicial, cuentaDestino, monto, fecha, hora]
    return lista


def exportar_retiro(ID, cuenta, monto, fecha, hora):
    lista = [ID, cuenta, monto, fecha, hora]
    return lista


def exportar_servicio(ID, codigoDeuda, cuenta, monto, fecha, hora):
    lista = [ID, codigoDeuda, cuenta, monto, fecha, hora]
    return lista


def generar_numero(a):
    ID = ""
    for i in range(a):
        p = str(randint(0, 9))
        ID = ID + p
    return ID


def existe_lista(lista):
    if (lista == []):
        existe = False
    else:
        existe = True
    return existe
