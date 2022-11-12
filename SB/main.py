from recepcionista import *
recep1=Recepcionista("","","","","","","","","","","","")

def Menu():
    print("1)Registro\n2)Inicio Sesión")
    opc=int(input("Introduzca su opción: "))
    if(opc==1):
        recep1.registrar()
    elif opc==2:
       recep1.iniciar_sesion()
    else:
        print("Intente de nuevo")
Menu()
#AGREGAR NCUENTA FALTANTE