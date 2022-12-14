import sqlite3

class Db_devolver_servicios:
    def __init__(self, num_cuenta):
        self.num_cuenta = num_cuenta
        self.__path = r'DataBase\banquito.db'
        self.__cursor = sqlite3.Connection(self.__path).cursor()

    def devolver_servicios(self):
        self.__cursor.execute(f"SELECT id_deuda, cod_deuda, nombre, monto, fecha_venc FROM servicios WHERE num_cuenta={self.num_cuenta}")
        deudas = self.__cursor.fetchall()
        return deudas

    def imprimir_deudas(self):
        deudas = self.devolver_servicios()
        print("\n \n Bienvenido. A continuación se muestran sus deudas:")
        print("CODIGO DE DEUDA: \t \t \t EMPRESA: \t \t \t MONTO: \t \t \t FECHA VENCIMIENTO:")
        for i in deudas:
            print(f"{i[0]} \t \t \t \t \t {i[1]} \t \t \t \t {i[2]} \t \t \t \t {i[3]}")