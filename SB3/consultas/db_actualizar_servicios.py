import sqlite3

class Db_actualizar_servicios:
    def __init__(self, codigo_deuda):
        self.__path = r'DataBase\banquito.db'
        self.__conexion = sqlite3.Connection(self.__path)
        self.__cursor = self.__conexion.cursor()
        self.__codigo_deuda = codigo_deuda

    def actualizar_servicios(self):
        self.__cursor.execute(f"DELETE FROM servicios WHERE cod_deuda = {self.__codigo_deuda}")
        self.__conexion.commit()