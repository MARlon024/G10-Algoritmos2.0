import sqlite3

class Cuenta:
    def __init__(self, cuenta):
        self.__cuenta = cuenta
        self.__conexion = sqlite3.Connection("DataBase/Bank.db")
        self.__cursor = self.__conexion.cursor()

    def obtener_saldo(self):
        self.__cursor.execute(f"SELECT saldo FROM cuentas_bancarias WHERE num_cuenta={self.__cuenta}")
        saldo = self.__cursor.fetchall()[0][0]
        return saldo

    def existe_cuenta(self):
        self.__cursor.execute(f"SELECT * FROM cuentas_bancarias WHERE num_cuenta={self.__cuenta}")
        comprobacion = self.__cursor.fetchall()
        if(comprobacion==[]):
            print("Esta cuenta no existe...\n\n")
            existe = False
        else:
            existe = True
        return existe