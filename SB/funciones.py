import datetime
from random import randint


# no es S de SOLID: 
def menuPrincipal():
    print("\t \t  Bienvenido al panel de transacciones. Ingrese la opción a continuar: \n 1. Depósito \n 2. Transferencia \n 3. Retiro \n 4. Pago de servicios \n 0. Salir")
    opc = int(input("\n"))
    return opc

def comprobarIngreso(variable, digitos):
    while (len(variable) != digitos or variable.isnumeric() == False):
        variable = input("Introduzca de nuevo el dato solicitado: \n")
        if (len(variable) != digitos):
            print(f"Debe contener {digitos} dígitos... \n")
        if (variable.isnumeric() == False):
            print("Debe ingresar solo números... \n")
    return variable
def ingresoCuenta(cuentaInicial):
    cuentaDestino = cuentaInicial
    while (len(cuentaDestino) != 14 or cuentaDestino.isnumeric() == False or cuentaDestino == cuentaInicial):
        cuentaDestino = input(
            "Introduzca el número de cuenta a la que va a depositar: \n")
        if (len(cuentaDestino) != 14):
            print("La cuenta debe contener 14 dígitos... \n")
        if (cuentaDestino.isnumeric() == False):
            print("Debe ingresar solo números... \n")
        if (cuentaDestino == cuentaInicial):
            print("No puede transferirse a usted mismo... \n ")
    return cuentaDestino


def ingresoDeuda():
    codigoDeuda = ""
    valid = correrValidacionesDeuda(deuda)
    return false if !valid

    while (len(codigoDeuda) != 8 or codigoDeuda.isnumeric() == False):
        codigoDeuda = input("Introduzca el código de deuda a pagar: \n")
        if (len(codigoDeuda) != 8):
            print("La cuenta debe contener 8 dígitos... \n")
        if (codigoDeuda.isnumeric() == False):
            print("Debe ingresar solo números... \n")
    return codigoDeuda


class Deuda:
    def __init__():
        __codigo_deuda = input("introduzca codigo")
        __valor = input("valor deuda")
        __dni = input("dni")
        if self.__validaciones() != true:
            print("Error al validar!")
            raise "some_error"

    def mostrar_deuda(self):
        return self.__codigo_deuda

    def __validaciones():
        return false if len(__codido_deuda)!= 8
        return false if __codigo_deuda.isnumeric() == False
        return true



def main():
    deuda = Deuda()
    dbDeuda = DBDeuda()
    mostrar_deuda()
    dbDeuda.save_deuda(deuda)
    
    buscar_deuda(deuda)


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


def mostrarDeudas(deudas):
    print("\n \n Bienvenido. A continuación se muestran sus deudas:")
    print("CODIGO DE DEUDA: \t \t \t EMPRESA: \t \t \t MONTO: \t \t \t FECHA VENCIMIENTO:")
    for i in deudas:
        print(f"{i[0]} \t \t \t \t \t {i[1]} \t \t \t \t {i[2]} \t \t \t \t {i[3]}")


def mostrarServicio(ID, fecha, hora):
    print(f"\t \t ID DE OPERACIÓN: \n \t \t {ID} \n")
    print(" \t \t \t FECHA:")
    print(f"\t \t {fecha} \t \t {hora}\n \n")


def mostrarDeposito(ID, monto, fecha, hora):
    print(f"\t \t Usted ha depositado: \t \t {monto}\n")
    print(f"\t \t ID de operación: \t \t {ID} \n")
    print(f"\t \t FECHA:")
    print(f"\t \t {fecha} \t \t \t {hora}")


def exportarDeposito(ID, cuenta, monto, fecha, hora):
    lista = [ID, cuenta, monto, fecha, hora]
    return lista


def exportarTransferencia(ID, cuentaInicial, cuentaDestino, monto, fecha, hora):
    lista = [ID, cuentaInicial, cuentaDestino, monto, fecha, hora]
    return lista


def exportarRetiro(ID, cuenta, monto, fecha, hora):
    lista = [ID, cuenta, monto, fecha, hora]
    return lista


def exportarServicio(ID, codigoDeuda, cuenta, monto, fecha, hora):
    lista = [ID, codigoDeuda, cuenta, monto, fecha, hora]
    return lista


def generarNumero(a):
    ID = ""
    for i in range(a):
        p = str(randint(0, 9))
        ID = ID + p
    return ID


def existeLista(lista):
    if (lista == []):
        existe = False
    else:
        existe = True
    return existe
