import sqlite3

class Transaccion():

    def __init__(self):
        self.conexionCuentas = sqlite3.Connection("Usuarios")

    def montoValido(self, monto, cuenta):
        cursor = self.conexionCuentas.cursor()
        cursor.execute(f"SELECT SALDO FROM CUENTA WHERE DNI={cuenta}")
        self.saldo = cursor.fetchall()[0][0]
        if(self.saldo>=monto):
            valido = True
        else:
            print("Su cuenta no dispone del saldo suficiente para realizar esta transacción... \n")
            valido = False
        return valido

    def existeCuenta(self, cuenta):
        cursor = self.conexionCuentas.cursor()
        cursor.execute(f"SELECT * FROM CUENTA WHERE DNI={cuenta}")
        self.confirmacion = cursor.fetchall()
        if(self.confirmacion==[]):
            print("No se ha encontrado la cuenta.")
            existe = False
        else:
            existe = True
        return existe

    def obtenerSaldo(self, cuenta):
        cursor = self.conexionCuentas.cursor()
        cursor.execute(f"SELECT SALDO FROM CUENTA WHERE DNI={cuenta}")
        saldo = cursor.fetchall()[0][0]
        return saldo

    def existeID(self, ID):
        pass
    def operacion(self):
        pass
    def mandarDatos(self, lista):
        pass
    def cerrarConexion(self):
        self.conexionCuentas.close()
        
class Deposito(Transaccion):
    def operacion(self, monto, cuenta):
        cursor = self.conexionCuentas.cursor()
        cursor.execute(f"UPDATE CUENTA SET SALDO=SALDO+{monto} WHERE DNI={cuenta}")
        self.conexionCuentas.commit()

    def mandarDatos(self, lista):
        cursor = self.conexionCuentas.cursor()
        cursor.execute("INSERT INTO DEPOSITO VALUES(?,?,?,?,?)", lista)
        self.conexionCuentas.commit()

class Transferencia(Transaccion):

    def operacion(self, cuentaInicial, cuentaDestino, monto):
        cursor = self.conexionCuentas.cursor()
        cursor.execute(f"UPDATE CUENTA SET SALDO=SALDO+{monto} WHERE DNI={cuentaDestino}")
        self.conexionCuentas.commit()
        cursor.execute(f"UPDATE CUENTA SET SALDO=SALDO-{monto} WHERE DNI={cuentaInicial}")
        self.conexionCuentas.commit()


    def mandarDatos(self, lista):
        cursor = self.conexionCuentas.cursor()
        cursor.execute("INSERT INTO TRANSFERENCIAS VALUES(?,?,?,?,?,?)", lista)
        self.conexionCuentas.commit()

    def existeID(self, ID):
        cursor = self.conexionCuentas.cursor()
        cursor.execute(f"SELECT * FROM TRANSFERENCIAS WHERE ID_OPERACION={ID}")
        self.comprobacion = cursor.fetchall()
        if(self.comprobacion == []):
            existe = False
        else:
            existe = True
        return existe


class Retiro(Transaccion):
    def operacion(self, cuenta, monto):
        cursor = self.conexionCuentas.cursor()
        cursor.execute(f"UPDATE CUENTA SET SALDO=SALDO-{monto} WHERE DNI={cuenta}")
        self.conexionCuentas.commit()

    def mandarDatos(self, lista):
        cursor = self.conexionCuentas.cursor()
        cursor.execute("INSERT INTO RETIROS VALUES(?,?,?,?,?)",lista)
        self.conexionCuentas.commit()

    def existeID(self, ID):
        cursor = self.conexionCuentas.cursor()
        cursor.execute(f"SELECT * FROM RETIROS WHERE ID_OPERACION={ID}")
        self.comprobacion = cursor.fetchall()
        if(self.comprobacion == []):
            existe = False
        else:
            existe = True
        return existe

class pagoServicios(Transaccion):

    def __init__(self, cuenta):
        super().__init__()
        self.cuenta = cuenta
    def operacion(self, cuenta, monto, codigoDeuda):
        cursor = self.conexionCuentas.cursor()
        cursor.execute(f"UPDATE CUENTA SET SALDO=SALDO-{monto} WHERE DNI={cuenta}")
        self.conexionCuentas.commit()
        cursor.execute(f"DELETE FROM SERVICIOS WHERE CODIGO_DEUDA = {codigoDeuda}")
        self.conexionCuentas.commit()

    def devolverDeudas(self):
        cursor = self.conexionCuentas.cursor()
        cursor.execute(f"SELECT CODIGO_DEUDA, EMPRESA, MONTO, FECHA_VENCIMIENTO FROM SERVICIOS WHERE CUENTA={self.cuenta}")
        deudas = cursor.fetchall()
        return deudas

    def mandarDatos(self, lista):
        cursor = self.conexionCuentas.cursor()
        cursor.execute("INSERT INTO PAGOSERV VALUES(?,?,?,?,?,?)", lista)
        self.conexionCuentas.commit()

    def deudaMonto(self, codigoDeuda):
        cursor = self.conexionCuentas.cursor()
        cursor.execute(f"SELECT MONTO FROM SERVICIOS WHERE CODIGO_DEUDA={codigoDeuda}")
        monto = cursor.fetchall()[0][0]
        return monto

    def existeID(self, ID):
        cursor = self.conexionCuentas.cursor()
        cursor.execute(f"SELECT * FROM SERVICIOS WHERE CODIGO_DEUDA={ID}")
        self.comprobacion = cursor.fetchall()
        if (self.comprobacion == []):
            existe = False
        else:
            existe = True
        return existe