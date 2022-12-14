import sqlite3

class Db_validar_tabla_depo_reti:
    def __init__(self,id,num_cuenta,saldo,fecha,hora,tabla):
        self.__path=r'DataBase\banquito.db'
        self.conexionCuentas = sqlite3.Connection(self.__path)
        self.num_cuenta=num_cuenta
        self.saldo=saldo
        self.fecha=fecha
        self.hora=hora
        self.id=id
        self.tabla=tabla
        self.lista_dinero=[self.id,self.num_cuenta,self.saldo,self.fecha,self.hora]

    def crear_row(self):
        cursor = self.conexionCuentas.cursor()
        cursor.execute(f"INSERT INTO '{self.tabla}' VALUES (?,?,?,?,?)", self.lista_dinero)
        self.conexionCuentas.commit()

    def crear_row_transfer(self):
        cursor = self.conexionCuentas.cursor()
        cursor.execute(f"INSERT INTO transferencias VALUES (?,?,?,?,?,?)", self.lista_dinero)
        self.conexionCuentas.commit()
    

    