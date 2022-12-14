import sqlite3

from funciones.persona import Persona
from generador.generar import Generar


class Db_registrar_cliente(Persona):
    def __init__(self, id_cliente, dni, nom, ape_pa, ape_ma, correo, fecha, cel, cel_ope):
        super().__init__(dni, nom, ape_pa, ape_ma, correo, fecha, cel, cel_ope)
        self.id_cliente = id_cliente
        self.num_cuenta = Generar.generar_num_cuenta(dni)
        file_database = "DataBase/banquito.db"
        self.__conexion = sqlite3.Connection(file_database)
        self.__cursor = self.__conexion.cursor()

    def registrar(self):
        self.__cursor.execute(
            f"INSERT INTO clientes VALUES ('{self.id_cliente}', '{self.dni}', '{self.nom}', '{self.ape_pa}', '{self.ape_ma}','{self.correo}','{self.fecha}','{self.cel}','{self.cel_ope}')")
        self.__cursor.execute(
            f"INSERT INTO cuentas_bancarias VALUES ('{self.id_cliente}', '{self.dni}', '{self.num_cuenta}', {0.0})")
        self.__conexion.commit()
        self.__conexion.close()
        print("Cliente registrado exitosamente")
