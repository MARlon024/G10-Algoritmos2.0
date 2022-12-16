import sqlite3
class Db_validar_tarjeta:
    def __init__(self, num_cuenta):
        self.__num_cuenta = num_cuenta
        file_database = "DataBase/banquito.db"
        self.__conexion = sqlite3.Connection(file_database)
        self.__cursor = self.__conexion.cursor()

    def existe_tarjeta(self):
        self.__cursor.execute(f"SELECT num_tarjeta FROM tarjeta WHERE num_cuenta={self.__num_cuenta}")
        num_tarjeta = self.__cursor.fetchone()[0]
        if num_tarjeta == "":
            return False
        else:
            return True

    def devolver_clave(self):
        self.__cursor.execute(f"SELECT clave FROM tarjeta WHERE num_cuenta={self.__num_cuenta}")
        monto_deuda = self.__cursor.fetchone()[0]
        return monto_deuda

