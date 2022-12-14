import getpass
import sqlite3


class Bloquear_tarjeta():
    def __init__(self):
        self.cuenta = input("dni: ")
        self.clave = getpass.getpass()  # Validar la clave
        self.path = 'DataBase\banquito.db'
        self.status = "Bloqueado"

    def bloqueo_tarjeta(self):
        conn = sqlite3.Connection(self.path)
        cursor = conn.cursor()
        cursor.execute(
            f"UPDATE tarjeta SET status='{self.status}' WHERE cuenta={self.cuenta} AND clave={self.clave}")
        conn.commit()
        conn.close()
        return print("Tarjeta Bloqueada")
