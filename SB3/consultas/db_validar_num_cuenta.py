import sqlite3


class Db_validar_num_cuenta:
    def __init__(self, num_cuenta, tabla):
        self.__num_cuenta = num_cuenta
        self.__tabla = tabla
        file_database = "DataBase/banquito.db"
        self.__cursor = sqlite3.Connection(file_database).cursor()

    def existe_cuenta(self):
        self.__cursor.execute(f"SELECT num_cuenta FROM {self.__tabla} WHERE num_cuenta={self.__num_cuenta}")
        num_cuenta = self.__cursor.fetchone()
        if num_cuenta == "":
            return False
            
        else:
            return True  

    def obtener_saldo(self):
        self.__cursor.execute(
            f"SELECT saldo FROM {self.__tabla} WHERE num_cuenta={self.__num_cuenta}")
        saldo = self.__cursor.fetchall()[0][0]
        return saldo

