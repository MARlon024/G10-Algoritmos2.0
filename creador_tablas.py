import sqlite3
import datetime
from random import randint
'''fechagaa = datetime.datetime.now()
diaActual = datetime.datetime.strftime(fechagaa, "%Y-%m-%d")
horaActual = datetime.datetime.strftime(fechagaa, "%H:%M:%S")
print(fechagaa)
print(diaActual)
print(horaActual)
cn = sqlite3.Connection("Cuentas")
cursor = cn.cursor()
cursor.execute(f"INSERT INTO TRANSACCIONES VALUES('190','191',290, '{diaActual}', '{horaActual}')")
cn.commit()'''


# CREACIONES DE TABLAS:

''' CREAR TABLA DE TRANSFERENCIAS:
cn = sqlite3.Connection("Cuentas")
cursor = cn.cursor()
cursor.execute(f"CREATE TABLE TRANSFERENCIAS( ID_OPERACION VARCHAR(50) PRIMARY KEY UNIQUE, DESDE VARCHAR(50), HASTA VARCHAR(50), MONTO FLOAT, FECHA DATE, HORA TIME)")
cn.commit()'''

''' CREAR TABLA DE RETIROS:
cn = sqlite3.Connection("Cuentas")
cursor = cn.cursor()
cursor.execute(f"CREATE TABLE RETIROS(ID_OPERACION VARCHAR(50) PRIMARY KEY UNIQUE, CUENTA VARCHAR(50), MONTO FLOAT, FECHA DATE, HORA TIME)")
cn.commit()'''

''' CREAR TABLA DE SERVICIOS:
cn = sqlite3.Connection("Cuentas")
cursor = cn.cursor()
cursor.execute(f"CREATE TABLE SERVICIOS(CODIGO_DEUDA VARCHAR(50) PRIMARY KEY UNIQUE, EMPRESA VARCHAR(50), CUENTA VARCHAR(50), MONTO FLOAT, FECHA_VENCIMIENTO DATE)")
cn.commit()'''

''' CREAR TABLA DE PAGO DE SERVICIOS:
cn = sqlite3.Connection("Cuentas")
cursor = cn.cursor()
cursor.execute(f"CREATE TABLE PAGOSERV(ID_OPERACION VARCHAR(50) PRIMARY KEY UNIQUE, ID_DEUDA VARCHAR(50) UNIQUE, CUENTA VARCHAR(50), MONTO FLOAT, FECHA DATE, HORA TIME)")
cn.commit()'''

'''CREAR TABLA DE DEPOSITO:
cn = sqlite3.Connection("Cuentas")
cursor = cn.cursor()
cursor.execute(f"CREATE TABLE DEPOSITO(ID_OPERACION VARCHAR(50) PRIMARY KEY UNIQUE, CUENTA VARCHAR(50), MONTO FLOAT, FECHA DATE, HORA TIME)")
cn.commit()'''

'''cn = sqlite3.Connection("Cuentas")
cursor = cn.cursor()
cursor.execute(f"SELECT MONTO FROM RETIROS WHERE MONTO=15.5")
a = cursor.fetchall()[0][0]
print(a)
cn.close()'''


# ELIMINAR TABLA:

'''cn = sqlite3.Connection("Cuentas")
cursor = cn.cursor()
cursor.execute(f"DROP TABLE TRANSACCIONES")
cn.commit()
cn.close()'''
