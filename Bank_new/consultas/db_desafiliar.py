import sqlite3


class Db_desafiliar:
    def __init__(self,num_cuenta) :
        self.__path = r'DataBase\banquito.db'
        self.__conexion = sqlite3.Connection(self.__path)
        self.__cursor = self.__conexion.cursor()
        self.num_cuenta=num_cuenta
    
    def elimiar_cliente(self):
        dni=self.buscar_dni()
        self.__cursor.execute(f"DELETE FROM clientes WHERE dni = '{dni}'")
        self.__conexion.commit()
        self.eliminar_tarjeta()
        self.eliminar_cuenta()
        self.__conexion.close()
        return True

    def eliminar_tarjeta(self):
        self.__cursor.execute(f"DELETE FROM tarjeta WHERE num_cuenta = {self.num_cuenta}")
        self.__conexion.commit()

    def eliminar_cuenta(self):
        self.__cursor.execute(f"DELETE FROM cuentas_bancarias WHERE num_cuenta = {self.num_cuenta}")
        self.__conexion.commit()

    def buscar_dni(self):
        self.__cursor.execute(f"SELECT dni FROM cuentas_bancarias WHERE num_cuenta={self.num_cuenta}")
        dni=self.__cursor.fetchone()[0]
        return dni