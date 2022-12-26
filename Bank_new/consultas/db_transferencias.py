import datetime
from random import randint
from consultas.db_validar_tabla_depo_reti import Db_validar_tabla_depo_reti
import sqlite3
import pdfkit

class Db_transferencias:
    def __init__(self,num_cuenta_desde,num_cuenta_hasta,dinero,tabla):
        self.__path=r'DataBase\banquito.db'
        self.conexionCuentas = sqlite3.Connection(self.__path)
        self.id=self.generar_numero(9)
        self.num_cuenta_desde = num_cuenta_desde 
        self.num_cuenta_hasta = num_cuenta_hasta
        self.fecha,self.hora=self.obtener_tiempo()
        self.dinero = dinero
        self.lista_transferir = [self.id,self.num_cuenta_desde,self.num_cuenta_hasta,self.dinero,self.fecha,self.hora]
    def mandar_datos(self):
        try:
            cursor = self.conexionCuentas.cursor()
            self.validar_tablas()
            cursor.execute(f"INSERT INTO transferencias VALUES (?,?,?,?,?,?)", self.lista_transferir)
            cursor.execute(f"UPDATE cuentas_bancarias SET saldo=saldo-{self.dinero} WHERE num_cuenta={self.num_cuenta_desde}")
            cursor.execute(f"UPDATE cuentas_bancarias SET saldo=saldo+{self.dinero} WHERE num_cuenta={self.num_cuenta_hasta}")
            self.conexionCuentas.commit()
            self.conexionCuentas.close()
        except Exception:
            print("error")

    def validar_tablas(self):
        validar_desde=Db_validar_tabla_depo_reti(self.id,self.num_cuenta_desde,self.dinero,self.fecha,self.hora,"retiros")
        validar_hasta=Db_validar_tabla_depo_reti(self.id,self.num_cuenta_hasta,self.dinero,self.fecha,self.hora,"depositos")
        validar_desde.crear_row()
        validar_hasta.crear_row()

    def obtener_tiempo(self):
        ahora = datetime.datetime.now()
        fechaActual = datetime.datetime.strftime(ahora, "%Y-%m-%d")
        horaActual = datetime.datetime.strftime(ahora, "%H:%M:%S")
        return fechaActual, horaActual
    
    def generar_numero(self,a):
        id = "0"
        for i in range(a):
            p = str(randint(0, 9))
            id = id + p
        return id
    
    def mostrar_comprobante(self,text):
        comprobante=f"""\t \t \t Se ha {text}: \t S/. {self.dinero} de la cuenta {self.num_cuenta_desde} a la cuenta {self.num_cuenta_hasta}
                \n \t \t Su nuevo saldo es: {self.dinero} \n
                \t \t \t FECHA:\n\t \t {self.fecha} \t \t {self.hora}\n
                \t \t {self.fecha} \t \t {self.hora}\n
                \t NUMERO DE OPERACION: {self.id} \n"""
        self.imprimir_comprobante(comprobante)

    def imprimir_comprobante(self,comprobante):
        
        path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'#Cambiar la ubicación donde el programa ha sido instalado
        config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
        pdfkit.from_string(comprobante, f"comprobantes\Comprobante_{self.id}.pdf",configuration=config)
        print("PDF file saved.")