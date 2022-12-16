import sqlite3

class Db_buscar_num_cuenta:
    def __init__(self, dni):
        self.__dni = dni
        file_database = "DataBase/banquito.db"
        self.__conexion = sqlite3.Connection(file_database)
        self.__cursor = self.__conexion.cursor()

    def buscar(self):
        self.__cursor.execute(f"SELECT num_cuenta FROM cuentas_bancarias WHERE dni={self.__dni}")
        dato = self.__cursor.fetchone()[0]
        self.__conexion.commit()
        self.__conexion.close()
        if dato == "":
            return False
        else:
            return True
