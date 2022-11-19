from persona import *
from cliente import *
from cryptography.fernet import Fernet
from operaciones_recepcionista import *


def menu():
    print("1. Registrar nuevo cliente")
    print("2. Solicitar tarjeta debito")
    print("3. Bloqueo de tarjeta de debito")
    print("4. Renovar tarjeta debito")
    print("5. Transacciones")
    print("6. Salir")


def menu_transacciones():
    print("1. Deposito")
    print("2. Retiro")
    print("3. Pago de Servicios")
    print("6. Salir")


class Recepcionista(Persona):
    def __init__(self, dni=None, nom=None, ape_pa=None, ape_ma=None, correo=None, fecha=None, cel=None, cel_ope=None, user_recep=None, psw_recep=None, status=None):
        super().__init__(dni, nom, ape_pa, ape_ma,
                         correo, fecha, cel, cel_ope)
        self.__user_recep = user_recep
        self.__psw_recep = psw_recep
        self.__status = status

    def buscar_recepcionista(self):
        self.__user_recep = input("Usuario: ")
        self.__psw_recep = getpass.getpass()
        recepcionista = Operaciones_recepcionista(self.__user_recep, self.__psw_recep)
        if recepcionista.iniciar_sesion() == True:
            menu()
            opc = int(input("Opcion: "))
            if opc == 1:
                print(self.registrar_cliente())
            elif opc == 2:
                print(self.generar_tarjeta_cliente())
            elif opc == 3:
                print(self.bloquear_tarjeta_cliente())
            elif opc == 4:
                print(self.renovar_tarjeta_Cliente())
            elif opc == 5:
                print(self.transacciones())
            elif opc == 6:
                return 0
        else:
            print("Error, usuario no encontrado")

    def registrar_cliente(self):
        recepcionista = Operaciones_recepcionista(self.__user_recep, self.__psw_recep)
        return recepcionista.registrar_cliente()

    def generar_tarjeta_cliente(self):
        recepcionista = Operaciones_recepcionista(self.__user_recep, self.__psw_recep)
        return recepcionista.generar_tarjeta()

    def bloquear_tarjeta_cliente(self):
        recepcionista = Operaciones_recepcionista(self.__user_recep, self.__psw_recep)
        return recepcionista.bloquear_tarjeta()

    def renovar_tarjeta_Cliente(self):
        recepcionista = Operaciones_recepcionista(self.__user_recep, self.__psw_recep)
        return recepcionista.renovar_tarjeta()

    def transacciones(self):
        recepcionista = Operaciones_recepcionista(self.__user_recep, self.__psw_recep)
        return recepcionista.transacciones()
