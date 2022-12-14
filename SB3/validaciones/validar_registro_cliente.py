from funciones.persona import Persona


class Validar_registro_cliente(Persona):
    def __init__(self, id_cliente, dni, nom, ape_pa, ape_ma, correo, fecha, cel, cel_ope):
        super().__init__(dni, nom, ape_pa, ape_ma, correo, fecha, cel, cel_ope)
        self.id_cliente = id_cliente

    def convalidar_dni(self):
        if len(self.dni) != 8 or self.dni.isnumeric() == False:
            print("DNI NO VÁLIDO")
            return False
        else:
            return True

    def convalidar_correo(self):
        if self.correo.__contains__("@") == False or self.correo.__contains__(".") == False:
            print("CORREO NO VÁLIDO")
            return False
        else:
            return True

    def convalidar_cel(self):
        if len(self.cel) != 9 or self.cel.isnumeric() == False:
            print("CEL NO VÁLIDO")
            return False
        else:
            return True

    def mostrar_convalidaciones(self):
        conva_dni = self.convalidar_dni()
        conva_correo = self.convalidar_correo()
        conva_cel = self.convalidar_cel()
        if (conva_cel == True and conva_correo == True and conva_dni == True):
            return True
        else:
            return False
