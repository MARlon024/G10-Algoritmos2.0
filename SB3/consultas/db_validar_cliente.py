import sqlite3


class Db_validar_cliente:
    def __init__(self, dni):
        self.__dni = dni
        file_database = "DataBase/banquito.db"
        self.__cursor = sqlite3.Connection(file_database).cursor()

    def existe_cuenta_cliente(self):
        self.__cursor.execute(
            f"SELECT dni FROM clientes WHERE dni={self.__dni}")
        usu = self.__cursor.fetchone()
        if usu == None:
            return False
        else:
            return True
