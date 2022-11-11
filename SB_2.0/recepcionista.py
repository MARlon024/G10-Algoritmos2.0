import getpass
import sqlite3
from tkinter import EXCEPTION
import uuid
import transacciones
from tarjetaCredito import *
from cryptography.fernet import Fernet
from persona import *

cn = sqlite3.Connection("Usuarios")
cursor = cn.cursor()
#cursor.execute('''
#    CREATE TABLE CLIENTES(
#    ID BINARY(20) PRIMARY KEY UNIQUE,
#    NOMBRE VARCHAR(50),
#    APATERNO VARCHAR(50),
#    AMATERNO VARCHAR(50),
#    DNI INTEGER,
#    CORREO VARCHAR(50),
#    FECHA VARCHAR(50),
#    CEL INTEGER,
#    OPERADOR VARCHAR(50),
#    KEY_PSW VARCHAR(50),
#    PSW VARCHAR(150))
# ''')#Podemos poner "UNIQUE" al final de nombre
class Recepcionista(Persona):
    def __init__(self, __dni, __nom, __ape_pa, __ape_ma, __correo, __fecha, __cel, __cel_ope, __codigo_recep, __clave_recep,__key_clave_recep, __status):
        super().__init__(__dni, __nom, __ape_pa, __ape_ma,
                         __correo, __fecha, __cel, __cel_ope)
        self.codigo_recep = __codigo_recep
        self.clave_recep = __clave_recep
        self.status = __status
        self.key_clave_recep= __key_clave_recep

    def registrar(self):
        cn = sqlite3.Connection("Usuarios")
        cursor = cn.cursor()
        veri=""
        user_recep = []
        boi=False
        print("-------REGISTRO-------")
        while (len(self.dni) != 8 or self.dni.isnumeric() == False or boi==False):
            self.dni = input("DNI: ")
            cursor.execute(f"SELECT * FROM CLIENTES WHERE DNI ={self.dni}")
            product=cursor.fetchall()
            for p in product:
                veri=p[4]
            print(veri)
            if (len(self.dni) != 8 or self.dni.isnumeric() == False):
                print("Introducir sus 8 dígitos de DNI")
            else:
                if(veri==""):
                    boi=True
            veri=""
        self.nom = input("Nombre: ").capitalize() 
        self.ape_pa = input("Apellido paterno: ").capitalize()
        self.ape_ma = input("Apellido materno: ").capitalize()

        while self.correo.__contains__("@") != True or self.correo.__contains__(".") != True:
            self.correo=input("Correo Personal: ")
            if (self.correo.__contains__("@") == False or self.correo.__contains__(".") == False):
                print("Introducir un correo valido ")

        self.fecha = input("Fecha de nacimiento: ")
        while (len(self.cel) != 9 or self.cel.isnumeric() == False):
            self.cel = input("Celular: ")
            if (len(self.cel) != 9 or self.cel.isnumeric() == False):
                print("Introducir sus 9 dígitos de celular")
        self.cel_ope = input("Operadora: ")
        self.codigo_recep = str(uuid.uuid1())  # GENERANDO CODIGO UUID
        try:
            while (len(self.clave_recep) != 6 or self.clave_recep.isnumeric() == False):
                self.clave_recep = getpass.getpass()
                if (len(self.clave_recep) != 6 or self.clave_recep.isnumeric() == False):
                    print("Introducir sus 6 dígitos de clave")    
        except Exception as err:
            print('ERROR:', err)

        self.key_clave_recep = Fernet.generate_key()
        fernet = Fernet(self.key_clave_recep )
        
        cod_encrypt = str(self.clave_recep)
        encMessage = fernet.encrypt(cod_encrypt.encode())
        self.clave_recep=encMessage
        # decMessage = fernet.decrypt(encMessage).decode()     - DESENCRIPTAR self.clave_recept
        ele = [self.codigo_recep, self.nom, self.ape_pa, self.ape_ma, self.dni,
               self.correo, self.fecha, self.cel, self.cel_ope, self.key_clave_recep,self.clave_recep]
        user_recep.append(ele)
       
        cursor.execute("INSERT INTO CLIENTES VALUES (?,?,?,?,?,?,?,?,?,?,?)", ele)
        ele2=[self.dni,0]
        cursor.execute("INSERT INTO CUENTA VALUES (?,?)", ele2)
        cn.commit()
        print("FELICIDADES SU CUENTA HA SIDO CREADA: ",self.nom)

    def iniciar_sesion(self):
        cn = sqlite3.Connection("Usuarios")
        cursor = cn.cursor()
        print("------INGRESO-------")
        while (len(self.dni) != 8 or self.dni.isnumeric() == False):
            self.dni = input("DNI: ")
            if (len(self.dni) != 8 or self.dni.isnumeric() == False):
                print("Introducir sus 8 dígitos de DNI")
        try:
            while (len(self.clave_recep) != 6 or self.clave_recep.isnumeric() == False):
                self.clave_recep = getpass.getpass()
                if (len(self.clave_recep) != 6 or self.clave_recep.isnumeric() == False):
                    print("Introducir sus 6 dígitos de claves")       
        except Exception as err:
            print('ERROR:', err)
        veri=""
        key=""
        
        try:
    
            cursor.execute(f"SELECT * FROM CLIENTES WHERE DNI = {self.dni}")
            user = cursor.fetchall()
            for p in user:
                veri = p[10]
                key = p[9]
                
            fernet = Fernet(key)
            decMessage = fernet.decrypt(veri).decode()
            if veri=="":
                print("Usuario no encontrado")
            else:
                cn.commit()
                if (self.clave_recep == decMessage):
                    print("1)Transacciones\n2)Generar Tarjeta\n3)Salir")
                    opc=int(input("Introduzca una opción: "))
                    if(opc==1):
                        transacciones.transacciones(self.dni)
                    elif opc==2:
                        try:
                            Generar_tarjeta("4509xxxxxxxxxxxx",self.dni)
                        except Exception:
                            print("Tarjeta ya creada")
                    elif opc==3:
                        print("Salir")
                else:
                    print("Contraseña incorrecta")
        except EXCEPTION:
            print("Error")
cn.close()