import pandas as pd
import pdfkit
import sqlite3

class obtener_frame:
    def __init__(self, tabla, id):
        self.__conexion = sqlite3.connect("DataBase/BBDD")
        self.__tabla = tabla
        self.__id = id

    def obtener_data_frame(self):
        data_frame = pd.read_sql(f"SELECT * FROM {self.__tabla} WHERE id_operacion={self.__id}", self.__conexion)
        return data_frame