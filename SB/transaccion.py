import sqlite3

class Transaccion():

    def __init__(self):
        self.conexionCuentas = sqlite3.Connection("DataBase/Bank.db")

    def montoValido(self, monto, cuenta):
        cursor = self.conexionCuentas.cursor()
        cursor.execute(f"SELECT saldo FROM cuentas_bancarias WHERE num_cuenta={cuenta}")
        self.saldo = cursor.fetchall()[0][0]
        if(self.saldo>=monto):
            valido = True
        else:
            print("Su cuenta no dispone del saldo suficiente para realizar esta transacción... \n")
            valido = False
        return valido

    def existeCuenta(self, cuenta):
        cursor = self.conexionCuentas.cursor()
        cursor.execute(f"SELECT * FROM cuentas_bancarias WHERE num_cuenta={cuenta}")
        self.confirmacion = cursor.fetchall()
        if(self.confirmacion==[]):
            print("No se ha encontrado la cuenta.")
            existe = False
        else:
            existe = True
        return existe

    def obtenerSaldo(self, cuenta):
        cursor = self.conexionCuentas.cursor()
        cursor.execute(f"SELECT saldo FROM cuentas_bancarias WHERE num_cuenta={cuenta}")
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
        cursor.execute(f"UPDATE cuentas_bancarias SET saldo=saldo+'{monto}' WHERE num_cuenta={cuenta}")
        self.conexionCuentas.commit()

    def mandarDatos(self, lista):
        cursor = self.conexionCuentas.cursor()
        cursor.execute("INSERT INTO depositos VALUES(?,?,?,?,?)", lista)
        self.conexionCuentas.commit()

class Transferencia(Transaccion):

    def operacion(self, cuentaInicial, cuentaDestino, monto):
        cursor = self.conexionCuentas.cursor()
        cursor.execute(f"UPDATE cuentas_bancarias SET saldo=saldo+'{monto}' WHERE num_cuenta={cuentaDestino}")
        self.conexionCuentas.commit()
        cursor.execute(f"UPDATE cuentas_bancarias SET saldo=saldo-'{monto}' WHERE num_cuenta={cuentaInicial}")
        self.conexionCuentas.commit()


    def mandarDatos(self, lista):
        cursor = self.conexionCuentas.cursor()
        cursor.execute("INSERT INTO transferencias VALUES(?,?,?,?,?,?)", lista)
        self.conexionCuentas.commit()

    def existeID(self, ID):
        cursor = self.conexionCuentas.cursor()
        cursor.execute(f"SELECT * FROM transferencias WHERE id_operacion={ID}")
        self.comprobacion = cursor.fetchall()
        if(self.comprobacion == []):
            existe = False
        else:
            existe = True
        return existe


class Retiro(Transaccion):
    def operacion(self, cuenta, monto):
        cursor = self.conexionCuentas.cursor()
        cursor.execute(f"UPDATE cuentas_bancarias SET saldo=saldo-'{monto}' WHERE num_cuenta={cuenta}")
        self.conexionCuentas.commit()

    def mandarDatos(self, lista):
        cursor = self.conexionCuentas.cursor()
        cursor.execute("INSERT INTO retiros VALUES(?,?,?,?,?)",lista)
        self.conexionCuentas.commit()

    def existeID(self, ID):
        cursor = self.conexionCuentas.cursor()
        cursor.execute(f"SELECT * FROM retiros WHERE id_operacion={ID}")
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
        cursor.execute(f"UPDATE cuentas_bancarias SET saldo=saldo-'{monto}' WHERE num_cuenta={cuenta}")
        self.conexionCuentas.commit()
        cursor.execute(f"DELETE FROM servicios WHERE cod_deuda = {codigoDeuda}")
        self.conexionCuentas.commit()

    def devolverDeudas(self):
        cursor = self.conexionCuentas.cursor()
        cursor.execute(f"SELECT cod_deuda, nombre, monto, fecha_venc FROM SERVICIOS WHERE num_cuenta={self.cuenta}")
        deudas = cursor.fetchall()
        return deudas

    def mandarDatos(self, lista):
        cursor = self.conexionCuentas.cursor()
        cursor.execute("INSERT INTO pago_servicios VALUES(?,?,?,?,?,?)", lista)
        self.conexionCuentas.commit()

    def deudaMonto(self, codigoDeuda):
        cursor = self.conexionCuentas.cursor()
        cursor.execute(f"SELECT monto FROM servicios WHERE cod_deuda={codigoDeuda}")
        monto = cursor.fetchall()[0][0]
        return monto

    def existeID(self, ID):
        cursor = self.conexionCuentas.cursor()
        cursor.execute(f"SELECT * FROM servicios WHERE cod_deuda={ID}")
        self.comprobacion = cursor.fetchall()
        if (self.comprobacion == []):
            existe = False
        else:
            existe = True
        return existe