import sqlite3

class Transaccion:

    def __init__(self):
        self.conexionCuentas = sqlite3.Connection("Cuentas")

    def montoValido(self, monto, cuenta):
        cursor = self.conexionCuentas.cursor()
        cursor.execute(f"SELECT SALDO FROM CUENTA WHERE NUMERO_CUENTA={cuenta}")
        saldo = cursor.fetchall()[0][0]
        if(saldo>=monto):
            valido = True
        else:
            print("Su cuenta no dispone del saldo suficiente para realizar esta transacción... \n")
            valido = False
        return valido

    def existeCuenta(self, cuenta):
        cursor = self.conexionCuentas.cursor()
        cursor.execute(f"SELECT * FROM CUENTA WHERE NUMERO_CUENTA={cuenta}")
        confirmacion = cursor.fetchall()
        if(confirmacion==[]):
            print("No se ha encontrado la cuenta.")
            existe = False
        else:
            existe = True
        return existe

    def obtenerSaldo(self, cuenta):
        cursor = self.conexionCuentas.cursor()
        cursor.execute(f"SELECT SALDO FROM CUENTA WHERE NUMERO_CUENTA={cuenta}")
        saldo = cursor.fetchall()[0][0]
        return saldo

    def existeID(self, ID):
        pass

    def operacion(self):
        pass

    def cerrarConexion(self):
        self.conexionCuentas.close()






class Transferencia(Transaccion):

    def operacion(self, cuentaInicial, cuentaDestino, monto):
        cursor = self.conexionCuentas.cursor()
        cursor.execute(f"UPDATE CUENTA SET SALDO=SALDO+{monto} WHERE NUMERO_CUENTA={cuentaDestino}")
        self.conexionCuentas.commit()
        cursor.execute(f"UPDATE CUENTA SET SALDO=SALDO-{monto} WHERE NUMERO_CUENTA={cuentaInicial}")
        self.conexionCuentas.commit()


    def mandarDatos(self, lista):
        cursor = self.conexionCuentas.cursor()
        cursor.execute("INSERT INTO TRANSFERENCIAS VALUES(?,?,?,?,?,?)", lista)
        self.conexionCuentas.commit()

    def existeID(self, ID):
        cursor = self.conexionCuentas.cursor()
        cursor.execute(f"SELECT * FROM TRANSFERENCIAS WHERE ID_OPERACION={ID}")
        comprobacion = cursor.fetchall()
        if(comprobacion == []):
            existe = False
        else:
            existe = True
        return existe


class Retiro(Transaccion):
    def operacion(self, cuenta, monto):
        cursor = self.conexionCuentas.cursor()
        cursor.execute(f"UPDATE CUENTA SET SALDO=SALDO-{monto} WHERE NUMERO_CUENTA={cuenta}")
        self.conexionCuentas.commit()

    def mandarDatos(self, lista):
        cursor = self.conexionCuentas.cursor()
        cursor.execute("INSERT INTO RETIROS VALUES(?,?,?,?,?)",lista)
        self.conexionCuentas.commit()

    def existeID(self, ID):
        cursor = self.conexionCuentas.cursor()
        cursor.execute(f"SELECT * FROM RETIROS WHERE ID_OPERACION={ID}")
        comprobacion = cursor.fetchall()
        if(comprobacion == []):
            existe = False
        else:
            existe = True
        return existe

class pagoServicios(Transaccion):
    def operacion(self):
        pass