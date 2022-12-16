from getpass import getpass
from consultas.db_validar_recepcionista import Db_validar_recepcionista
from funciones.desafiliar_cuenta import Desafiliar_cuenta
from funciones.registro_cliente import Registro_cliente
from funciones.registro_tarjeta_cliente import Registro_tarjeta_cliente
from funciones.depositar import Depositar
from funciones.retirar import Retirar
from funciones.pago_servicios import Pago_servicios
from funciones.transferencias import Transferencias
from funciones.pago_servicios import Pago_servicios
from grupos_menu.menu import *
from tarjeta_funciones.bloquear_tarjeta import Bloquear_tarjeta
class Main:
    def presentacion(self):
        print("\n ======")
        print("Bienvenido a BANK. \nIngrese sus credenciales:\n")
        print("=====")
        Menu.menu_inicio()
        self.iniciar_sesion()

    def iniciar_sesion(self):
        opc = int(input("Ingresar opción: "))
        if opc == 1:
            cargo = "recepcionista"
        elif opc == 2:
            cargo = "plataforma"
        cuenta = input("Ingrese su usuario: ")
        contra = getpass("Ingrese su contraseña: ")
        recepcionista = Db_validar_recepcionista(cuenta, contra, cargo)
        if recepcionista.existe_cuenta_recepcionista():
            if recepcionista.contra_correcta_recepcionista():
                print("Ingresastes como ", cargo)
                print("Ha ingresado a BANK.\n")  # CONTINUAR A PARTIR DE AQUÍ
                self.personal_funcion(cargo)
            else:
                print("Su contraseña es incorrecta.\n")
        else:
            print("Este nombre de usuario no existe...\n")

    def personal_funcion(self,cargo):
        if cargo == "recepcionista":
            Menu.menu_recepcionista()
            opc = int(input("Opcion: "))
            if opc == 1:
                Registro_tarjeta_cliente()  # El key de generar
            elif opc == 2:
                Menu.menu_transacciones()
                opt = int(input("Opcion: "))
                if opt == 1:
                    Depositar()
                elif opt == 2:
                    Retirar()
                elif opt == 3:
                    Transferencias()
                elif opt == 4:
                    Pago_servicios()
                else:
                    print("Error")
            else:
                print("Salir")
        elif cargo == "plataforma":
            Menu.menu_plataforma()
            opc = int(input("Opcion: "))
            if opc == 1:
                Registro_cliente()
            elif opc == 2:
                Bloquear_tarjeta()  # Validar y el key tbm
            elif opc == 3:
                Desafiliar_cuenta()  # Validar y el key tbm
            else:
                print("4. Salir")

personal=Main()
personal.presentacion()
