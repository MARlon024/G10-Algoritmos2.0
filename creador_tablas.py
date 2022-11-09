import sqlite3
import datetime

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
cursor.execute(f"CREATE TABLE TRANSACCIONES(DESDE VARCHAR(50), HASTA VARCHAR(50), MONTO FLOAT, FECHA DATE, HORA TIME)")
cn.commit()'''

''' CREAR TABLA DE RETIROS:
cn = sqlite3.Connection("Cuentas")
cursor = cn.cursor()
cursor.execute(f"CREATE TABLE RETIROS(CUENTA VARCHAR(50), MONTO FLOAT, FECHA DATE, HORA TIME)")
cn.commit()'''





# ELIMINAR TABLA:

'''cn = sqlite3.Connection("Cuentas")
cursor = cn.cursor()
cursor.execute(f"DROP TABLE ?")
cn.commit()
cn.close()'''