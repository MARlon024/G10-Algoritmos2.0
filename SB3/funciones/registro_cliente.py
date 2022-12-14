import uuid
from validaciones.validar_registro_cliente import Validar_registro_cliente
from consultas.db_validar_cliente import Db_validar_cliente
from consultas.db_registrar_cliente import Db_registrar_cliente



class Registro_cliente:
    def __init__(self):
        self.id_cliente = str(uuid.uuid1())
        self.dni = input("DNI: ")
        self.nom = input("Nombres: ")
        self.ape_pa = input("Apellido Paterno: ")
        self.ape_ma = input("Apellido Materno: ")
        self.correo = input("Correo personal: ")
        self.fecha = input("Fecha de nacimiento: ")
        self.cel = input("Numero de celular: ")
        self.cel_ope = input("Operadora del celular: ")
        return self.registrar()

    def registrar(self):
        validar = Validar_registro_cliente(self.id_cliente, self.dni, self.nom, self.ape_pa,
                                           self.ape_ma, self.correo, self.fecha, self.cel, self.cel_ope)
        if validar.mostrar_convalidaciones() == True:
            db_validar = Db_validar_cliente(self.dni)
            if db_validar.existe_cuenta_cliente == True:
                return ("EL CLIENTE YA EXISTE")
            else:
                registrar = Db_registrar_cliente(self.id_cliente, self.dni, self.nom, self.ape_pa,
                                                 self.ape_ma, self.correo, self.fecha, self.cel, self.cel_ope)
                registrar.registrar()

        else:
            return "ERROR, DATOS NO VÁLIDOS"
