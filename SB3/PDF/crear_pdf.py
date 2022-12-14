import pandas as pd
import pdfkit
import os

class Crear_pdf:
    def __init__(self, data_frame):
        self.__data_frame = data_frame

    def crear_csv(self):
        self.__data_frame.to_csv("table.csv", index=False)

    def configuracion(self):
        programa = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
        config = pdfkit.configuration(wkhtmltopdf = programa)
        return config

    def leer_csv(self):
        self.__archivo_csv = pd.read_csv(r'D:\PROYECTOS PYTHON\INICIAR SESION\PDF\table.csv')

    def convertir_csv_pdf(self):
        config = self.configuracion()
        html_string = self.__archivo_csv.to_html(index=False)
        pdfkit.from_string(html_string, "prueba.pdf",configuration=config)

    def borrar_csv(self):
        os.remove("table.csv")

    def proceso_creacion_pdf(self):
        self.crear_csv()
        self.leer_csv()
        self.convertir_csv_pdf()