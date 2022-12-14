from consultas.db_validar_num_cuenta import Db_validar_num_cuenta
from validaciones.validar_num_cuenta import Validar_num_cuenta
from consultas.db_desafiliar import Db_desafiliar
class Desafiliar_cuenta:
    def __init__(self):
        self.num_cuenta = input("Intoducir cuenta bancaria: ")
        self.deposito_cuenta()

    def deposito_cuenta(self):
        validar = Validar_num_cuenta(self.num_cuenta)
        if validar.convalidar_num_cuenta() == True:
            validar_exis=Db_validar_num_cuenta(self.num_cuenta, "cuentas_bancarias")
            if validar_exis.existe_cuenta() == True:
                desafiliar = Db_desafiliar(self.num_cuenta)
                if desafiliar.elimiar_cliente():
                    print("Espero que vuelva pronto")
            else:
                print("LA CUENTA BANCARIA NO EXISTE")
        else:
            print("NUMERO DE CUENTA NO VALIDO")