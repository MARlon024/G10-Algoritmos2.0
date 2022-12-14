import sqlite3

class Db_validar_codigo_deuda:
    def __init__(self, codigo_deuda):
        self.__codigo_deuda=codigo_deuda
        self.__path="DataBase/banquito.db"
        self.__cursor = sqlite3.Connection(self.__path).cursor()

    def existe_codigo_deuda(self):
        self.__cursor.execute(f"SELECT cod_deuda FROM servicios WHERE cod_deuda={self.__codigo_deuda}")
        codigo = self.__cursor.fetchone()
        if codigo == None:
            return False
        else:
            return True

    def monto_deuda(self):
        self.__cursor.execute(f"SELECT monto FROM servicios WHERE cod_deuda={self.__codigo_deuda}")
        monto_deuda = self.__cursor.fetchone()[0]
        return monto_deuda