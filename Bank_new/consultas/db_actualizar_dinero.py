import datetime
from random import randint
from consultas.db_validar_tabla_depo_reti import Db_validar_tabla_depo_reti
import sqlite3
import pdfkit

class Db_actualizar_dinero:
    def __init__(self,num_cuenta,dinero,tabla):
        self.__path=r'DataBase\banquito.db'
        self.conexionCuentas = sqlite3.Connection(self.__path)
        self.id=self.generar_numero(9)
        self.num_cuenta = num_cuenta
        self.fecha,self.hora=self.obtener_tiempo()
        self.dinero = dinero
        self.tabla = tabla

    def mandar_datos(self):
        try:
            cursor = self.conexionCuentas.cursor()
            validar=Db_validar_tabla_depo_reti(self.id,self.num_cuenta,self.dinero,self.fecha,self.hora,self.tabla)
            if validar.existe_row() ==True:
                cursor.execute(f"UPDATE '{self.tabla}' SET saldo={self.dinero} WHERE num_cuenta={self.num_cuenta}")
            else:
                validar.crear_row()
            cursor.execute(f"UPDATE cuentas_bancarias SET saldo={self.dinero} WHERE num_cuenta={self.num_cuenta}")
            self.conexionCuentas.commit()
            self.conexionCuentas.close()
        except Exception:
            print("error")
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
    
    def mostrar_comprobante(self,monto,text):
        self.dinero=100
        comprobante=f"""\t \t \t Usted ha {text}: \t S/. {monto}
                \n \t \t Su nuevo saldo es: {self.dinero} \n
                \t \t \t FECHA:\n\t \t {self.fecha} \t \t {self.hora}\n
                \t \t {self.fecha} \t \t {self.hora}\n
                \t NUMERO DE OPERACION: {self.id} \n"""
        self.imprimir_comprobante(comprobante)

    def imprimir_comprobante(self,comprobante):
        
        path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'#Cambiar la ubicación donde el programa ha sido instalado
        config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
        pdfkit.from_string(comprobante, f"PDF\Comprobante_{self.id}.pdf",configuration=config)
        print("PDF file saved.")