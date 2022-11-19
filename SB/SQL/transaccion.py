import sqlite3

class Transaccion:

    def __init__(self, cuenta, saldo):
        self.__path=r'C:\Users\marli\OneDrive\Escritorio\Tra_Pro\G10-Algoritmos2.0\SB\DataBase\Bank.db'
        self.conexionCuentas = sqlite3.Connection(self.__path)
        self.__cuenta = cuenta
        self.__saldo = saldo
    def monto_valido(self):
        cursor = self.conexionCuentas.cursor()
        cursor.execute(f"SELECT saldo FROM cuentas_bancarias WHERE num_cuenta={self.__cuenta}")
        self.__saldo = cursor.fetchall()[0][0]
        if(self.__saldo>=self.__monto):
            valido = True
        else:
            print("Su cuenta no dispone del saldo suficiente para realizar esta transacción... \n")
            valido = False
        return valido

    def set_lista(self, lista):
        self.__lista = lista

    def set_id(self, ID):
        self.__ID = ID

    def set_monto(self, monto):
        self.__monto = monto
    def operacion(self):
        pass

    def existe_id(self):
        pass

    def mandar_datos(self):
        pass
    def cerrar_conexion(self):
        self.conexionCuentas.close()


class Deposito(Transaccion):


    def operacion(self):
        cursor = self.conexionCuentas.cursor()
        cursor.execute(f"UPDATE cuentas_bancarias SET saldo=saldo+{self._Transaccion__monto} WHERE num_cuenta={self._Transaccion__cuenta}")
        self.conexionCuentas.commit()

    def mandar_datos(self):
        cursor = self.conexionCuentas.cursor()
        cursor.execute("INSERT INTO depositos VALUES(?,?,?,?,?)", self._Transaccion__lista)
        self.conexionCuentas.commit()

    def existe_id(self):
        cursor = self.conexionCuentas.cursor()
        cursor.execute(f"SELECT * FROM depositos WHERE id_operacion={self._Transaccion__ID}")
        comprobacion = cursor.fetchall()
        if (comprobacion == []):
            existe = False
        else:
            existe = True
        return existe

class Transferencia(Transaccion):

    def existe_cuenta(self):
        cursor = self.conexionCuentas.cursor()
        cursor.execute(f"SELECT * FROM cuentas_bancarias WHERE num_cuenta={self.__cuentaDestino}")
        confirmacion = cursor.fetchall()
        if (confirmacion == []):
            print("No se ha encontrado la cuenta.")
            existe = False
        else:
            existe = True
        return existe

    def existe_id(self):
        cursor = self.conexionCuentas.cursor()
        cursor.execute(f"SELECT * FROM transferencias WHERE id_operacion={self._Transaccion__ID}")
        comprobacion = cursor.fetchall()
        if (comprobacion == []):
            existe = False
        else:
            existe = True
        return existe

    def operacion(self):
        cursor = self.conexionCuentas.cursor()
        cursor.execute(f"UPDATE cuentas_bancarias SET saldo=saldo+{self._Transaccion__monto} WHERE num_cuenta={self.__cuentaDestino}")
        cursor.execute(f"UPDATE cuentas_bancarias SET saldo=saldo-{self._Transaccion__monto} WHERE num_cuenta={self._Transaccion__cuenta}")
        self.conexionCuentas.commit()

    def mandar_datos(self):
        cursor = self.conexionCuentas.cursor()
        cursor.execute("INSERT INTO transferencias VALUES(?,?,?,?,?,?)", self._Transaccion__lista)
        self.conexionCuentas.commit()


    def set_destino(self, cuentaDestino):
        self.__cuentaDestino = cuentaDestino


class Retiro(Transaccion):
    def operacion(self):
        cursor = self.conexionCuentas.cursor()
        cursor.execute(f"UPDATE cuentas_bancarias SET saldo=saldo-{self._Transaccion__monto} WHERE num_cuenta={self._Transaccion__cuenta}")
        self.conexionCuentas.commit()

    def mandar_datos(self):
        cursor = self.conexionCuentas.cursor()
        cursor.execute("INSERT INTO retiros VALUES(?,?,?,?,?)", self._Transaccion__lista)
        self.conexionCuentas.commit()

    def existe_id(self):
        cursor = self.conexionCuentas.cursor()
        cursor.execute(f"SELECT * FROM retiros WHERE id_operacion={self._Transaccion__ID}")
        comprobacion = cursor.fetchall()
        if (comprobacion == []):
            existe = False
        else:
            existe = True
        return existe


class pago_servicios(Transaccion):

    def operacion(self):
        cursor = self.conexionCuentas.cursor()
        cursor.execute(f"UPDATE cuentas_bancarias SET saldo=saldo-{self._Transaccion__monto} WHERE num_cuenta={self._Transaccion__cuenta}")
        cursor.execute(f"DELETE FROM servicios WHERE cod_deuda = {self.__codigoDeuda}")
        self.conexionCuentas.commit()

    def devolver_deudas(self):
        cursor = self.conexionCuentas.cursor()
        cursor.execute(f"SELECT cod_deuda, nombre, monto, fecha_venc FROM servicios WHERE num_cuenta={self._Transaccion__cuenta}")
        deudas = cursor.fetchall()
        return deudas

    def mandar_datos(self):
        cursor = self.conexionCuentas.cursor()
        cursor.execute("INSERT INTO pago_servicios VALUES(?,?,?,?,?,?)", self._Transaccion__lista)
        self.conexionCuentas.commit()

    def deuda_monto(self):
        cursor = self.conexionCuentas.cursor()
        cursor.execute(f"SELECT monto FROM servicios WHERE cod_deuda={self.__codigoDeuda}")
        monto = cursor.fetchall()[0][0]
        return monto

    def existe_id(self):
        cursor = self.conexionCuentas.cursor()
        cursor.execute(f"SELECT * FROM pago_servicios WHERE id_operacion={self._Transaccion__ID}")
        comprobacion = cursor.fetchall()
        if (comprobacion == []):
            existe = False
        else:
            existe = True
        return existe

    def existe_deuda(self):
        cursor = self.conexionCuentas.cursor()
        cursor.execute(f"SELECT * FROM servicios WHERE cod_deuda={self.__codigoDeuda}")
        comprobacion = cursor.fetchall()
        if (comprobacion == []):
            existe = False
        else:
            existe = True
        return existe

    def set_cod_deuda(self, codigoDeuda):
        self.__codigoDeuda = codigoDeuda