import sqlite3

class Db_registrar_tarjeta:
    def __init__(self, datos):
        self.__datos = datos
        file_database = "DataBase/banquito.db"
        self.__conexion = sqlite3.Connection(file_database)
        self.__cursor = self.__conexion.cursor()

    def registrar_tarjeta(self):
        self.__cursor.execute(f"INSERT INTO tarjeta VALUES (?,?,?,?,?,?,?)", self.__datos)
        self.__conexion.commit()
        self.__conexion.close()
        print("Tarjeta registrada exitosamente")
