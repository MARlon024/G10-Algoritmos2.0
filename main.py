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