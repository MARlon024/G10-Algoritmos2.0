
from asyncio.windows_events import NULL
from itertools import product
from logging import exception
import random
import sqlite3
from tkinter import EXCEPTION
cn = sqlite3.Connection("Usuarios")
cursor = cn.cursor()

#cursor.execute('''
#    CREATE TABLE PRODUCT(
#    ID INTEGER PRIMARY KEY AUTOINCREMENT,
#    NOMBRE VARCHAR(50),
#    DNI INTEGER,
#    PSW VARCHAR(20),
#    NCUENTA VARCHAR(17) UNIQUE,
#    CVC VARCHAR(4),
#    DINERO FLOAT,
#    DEPOSITO FLOAT,
#    RETIRO FLOAT)
# ''')#Podemos poner "UNIQUE" al final de nombre

class usuario():
    def __init__(self, nom, dni, psw,ncuenta,cvc):
        self.nom = nom
        self.dni = dni
        self.psw = psw
        self.ncuenta=ncuenta
        self.cvc=cvc

    def estado(self):
        print(f"Bienvenido de vuelto {self.nom}")
    def menu(self):
        opc = 0
        while (opc == 0):
            print("1.Deposito")
            print("2.Retiro")
            print("3.Transferir")
            print("4.Salir")
            opc = int(input("Escoga una opcion: "))
            if (opc == 1):
                men=transferencias(self.nom,self.dni,self.psw,self.ncuenta,self.cvc)
                total=men.dinero()
                men.deposito(total)
            elif (opc == 2):
                men2=transferencias(self.nom,self.dni,self.psw,self.ncuenta,self.cvc)
                total2=men2.dinero()
                men2.retiro(total2)
            elif (opc == 3):
                men3=transferencias(self.nom,self.dni,self.psw,self.ncuenta,self.cvc)
                total3=men3.dinero()
                men3.transferir(total3)
            elif (opc == 4):
                print("Saliendo...")
                return 1
            else:
                print("Intente de nuevo...")
            opc = 0

    
class transferencias(usuario):
    
    def dinero(self):
        cursor.execute(f"SELECT * FROM PRODUCT WHERE NCUENTA ={self.ncuenta}")
        user=cursor.fetchall()
        for u in user:
            return u[6]
    
    def deposito(self,total):
        self.total=total
        depo=float(input("Ingrese la cantidad a depositar: "))
        if(depo>0):
            total=total+depo
            cursor.execute(f"UPDATE PRODUCT SET DEPOSITO = {depo},DINERO = {total} WHERE NCUENTA = {self.ncuenta}")
            cn.commit()
            print("Ha depositado:",depo,"\nDinero total: ",total)
        else:
            print("Dinero insuficiente")
    def retiro(self,total):
        self.total=total
        reti=float(input("Ingrese la cantidad a retirar: "))
        
        if(reti<total):
            total=total-reti
            cursor.execute(f"UPDATE PRODUCT SET RETIRO = {reti},DINERO = {total} WHERE NCUENTA = {self.ncuenta}")
            print("Ha retirado:",reti,"\nDinero total: ",total)
            cn.commit()
        else:
            print("Dinero insuficiente")
    def transferir(self,total): 
        self.total=total
        dni=input("Ingrese el número de DNI a transferir: ")
        cursor.execute(f"SELECT * FROM PRODUCT WHERE DNI ={dni}")
        user=cursor.fetchall()
        for u in user:
            veri=u[1]
            cuenta=u[4]
            T=u[6]
        if(self.ncuenta!=cuenta):
            if(veri==""):
                print("Usuario no registrado")
            else:
                trans=float(input("Ingrese la cantidad a transferir: "))
                if(trans<total):
                    total=total-trans
                    cursor.execute(f"UPDATE PRODUCT SET DEPOSITO = {trans},DINERO = {T+trans} WHERE DNI = {dni}")
                    print(f"Se acaba de transferir {trans} a la cuenta : {cuenta}")
                    cursor.execute(f"UPDATE PRODUCT SET RETIRO = {trans},DINERO = {total} WHERE NCUENTA = {self.ncuenta}")
                    print("Ha transferido:",trans,"\nDinero total: ",total)
                else:
                    print("Dinero insuficiente")
        else:
            print("Error...intente de nuevo")
        cn.commit()
    


def registro():
    print("-------REGISTRO-------")
    nom = input("Nombre: ")
    dni = input("DNI: ")
    psw = input("PSW: ")
    dinero = float(input("Cuanto dinero va a ingresar: "))
    boi=False
    veri=""
    while boi==False:
        r1=4551
        r2=random.randint(1000,10000)
        r3=random.randint(1000,10000)
        r4=random.randint(1000,10000)
        r=str(r1)+str(r2)+str(r3)+str(r4)
        print(r)
        cvc=str(random.randint(100,1000))
        card=[r,cvc]
        cursor.execute(f"SELECT * FROM PRODUCT WHERE NCUENTA ={r}")
        product=cursor.fetchall()
        for p in product:
            veri=p[0]
        if(veri!=r):
            print("Registrado")
            boi=True
    ele = [nom, dni, psw,r,cvc,dinero,0,0]
    user.append(ele)
    print(user)
    cursor.execute("INSERT INTO PRODUCT VALUES (NULL,?,?,?,?,?,?,?,?)", ele)
    cn.commit()
    print("SUCCESS")
    u = usuario(nom, dni, psw,r,cvc)
    u.estado()
    return u.menu()


def ingreso():
    c = 1
    veri=""
    while c == 1:
        
        try:
            print("------INGRESO-------")
            dni = input("DNI: ")
            psw = input("PSW: ")
            cursor.execute(f"SELECT * FROM PRODUCT WHERE DNI = {dni}")
            product = cursor.fetchall()
            for p in product:
                nom = p[1]
                veri = p[3]
                ncuenta = p[4]
                cvc=p[5]
            if veri=="":
                print("Usuario no encontrado")
            else:
                if (psw == veri):
                    u = usuario(nom, dni, psw,ncuenta,cvc)
                    u.estado()
                    return u.menu()
                else:
                    print("Contraseña incorrecta")
        except EXCEPTION:
            print("Error")
        print("1.Intentar de nuevo\n2.Retroceder")
        c=int(input("Opcion: "))
        if c==2:
            return 1

user = []
b = 1
while (b == 1):
    print("-----Bienvenido-----")
    print("1.Ingresar\n2.Registro\n3.Salir")
    c = int(input("Introduce una opción: "))
    if c == 1:
        b = ingreso()
    elif c == 2:
        b = registro()
    elif c == 3:
        break
    else:
        print("Error")
print("Muchas Gracias")
cn.close()