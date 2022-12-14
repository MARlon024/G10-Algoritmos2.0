import sqlite3


class Db_validar_recepcionista:
    def __init__(self, cuenta, contra, cargo):
        self.__cuenta = cuenta
        self.__contra = contra
        self.__cargo = cargo
        file_database = "DataBase/banquito.db"
        self.__cursor = sqlite3.Connection(file_database).cursor()

    def existe_cuenta_recepcionista(self):
        self.__cursor.execute(
            f"SELECT * FROM personal WHERE usuario={self.__cuenta} AND cargo='{self.__cargo}'")
        usu = self.__cursor.fetchone()
        if usu == None:
            return False
        else:
            return True

    def contra_correcta_recepcionista(self):
        self.__cursor.execute(
            f"SELECT contraseña FROM personal WHERE usuario={self.__cuenta}")
        password = self.__cursor.fetchone()[0]
        if self.__contra == password:
            return True
        else:
            return False
