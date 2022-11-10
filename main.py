<<<<<<< HEAD
import Transaccion
import funciones

continuar=True
while(continuar):
    try:
        opc = funciones.menuPrincipal()
        match(opc):
            case 1:
                transferencia = Transaccion.Transferencia()
                cuenta = funciones.ingresoCuenta('19145078912346') #REEMPLAZAR POR CUENTA INGRESADA PREVIAMENTE !!!
                if(transferencia.existeCuenta(cuenta)):
                    try:
                        monto = float(input("Ingrese el monto a depositar: \n"))
                        if (transferencia.montoValido(monto, '19145078912346')):  # REEMPLAZAR POR CUENTA INGRESADA PREVIAMENTE !!!
                            transferencia.operacion('19145078912346', cuenta, monto)  # REEMPLAZAR POR CUENTA INGRESADA PREVIAMENTE !!!
                            print("¡Transacción completada!\n")
                            fecha, hora = funciones.obtenerTiempo()
                            ID = "1" + funciones.crearID()
                            while(transferencia.existeID(ID)):
                                ID = "1" + funciones.crearID()
                            funciones.mostrarTransferencia(cuenta, monto, ID, fecha, hora)
                            lista = funciones.exportarTransferencia(ID, '19145078912346', cuenta, monto, fecha, hora)  # REEMPLAZAR POR CUENTA INGRESADA PREVIAMENTE !!!
                            transferencia.mandarDatos(lista)
                            transferencia.cerrarConexion()
                            continue
                        else:
                            continue
                    except ValueError:
                        print("\n ERROR: No puede ingresar variables que no sean números \n")
                else:
                    continue
            case 2:
                retiro = Transaccion.Retiro()
                try:
                    monto = float(input("Ingrese el monto a retirar \n"))
                    if(retiro.montoValido(monto, '19145078912346')): # REEMPLAZAR POR CUENTA INGRESADA PREVIAMENTE !!!
                        retiro.operacion('19145078912346',monto) # REEMPLAZAR POR CUENTA INGRESADA PREVIAMENTE !!!
                        print("¡Retiro completado!\n")
                        fecha, hora = funciones.obtenerTiempo()
                        ID = "2" + funciones.crearID()
                        while(retiro.existeID(ID)):
                            ID = "2" + funciones.crearID()
                        saldo = retiro.obtenerSaldo('19145078912346') # REEMPLAZAR POR CUENTA INGRESADA PREVIAMENTE !!!
                        funciones.mostrarRetiro(monto, saldo, ID, fecha, hora)
                        lista = funciones.exportarRetiro(ID,'19145078912346', monto, fecha, hora) # REEMPLAZAR POR CUENTA INGRESADA PREVIAMENTE !!!
                        retiro.mandarDatos(lista)
                        retiro.cerrarConexion()
                        continue
                    else:
                        continue
                except ValueError:
                    print("\n ERROR: No puede ingresar variables que no sean números \n")
                continue
            case 3:
                print("Bienvenido")
                # IMPRIMIR DEUDAS SEGÚN N° CUENTA
                # INGRESAR ID DE DEUDA
                # COMPLETADO - DEVOLVER DETALLES
                # EXPORTAR A BBDD
                continue
            case 0:
                continuar = False
                continue
            case _:
                print("Ingrese una opción valida... \n")
                continue
    except ValueError:
        print("\n ERROR: No puede ingresar variables que no sean números \n")
=======
#PLATAFORMA PARA EL CLINETE
import json
import os
import time

def choices_main():
    print("1. Recepcionista")
    print("2. Cliente")

def Choices_user():
    print("AllSafe")
    print("Sistema Bancario")
    print("1. Iniciar sesión")
    print("2. Bloquear tarjeta")
    print("3. Exit")

def choices_receptionist():
    print("Sistema Bancario")
    print("1. Iniciar sesión")
    print("2. Exit")
    print()

cont = 0
run = True
while run:
    if cont < 3:
        os.system("clear")
        choices_main()
        choice = int(input("\nIngrese eleccion: "))
        if choice == 1:
            os.system("clear")
            choices_receptionist()
            opc = int(input("\nIngrese eleccion: "))
        elif choice == 2:
            os.system("clear")
            Choices_user()
            opc = int(input("\nIngrese eleccion: "))
        elif choice == 3:
            break
        else:
            cont += 1
            print("No has seleccionado un numero correcto. Por favor lea mas cuidadosamente.")
            time.sleep(2.5)     
    else:
        print("Try again in 5 minutes")
        run = False
>>>>>>> ff779f64d874b3f10d17e882f79ea8056d517928
