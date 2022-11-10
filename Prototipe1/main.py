import json

file_users = './resources/usuarios.json'
file_cards = './resources/cards.json'
class Usuario:
    def __init__(self, id, identificador=None):
        self.id = id
        self.identificador = identificador

    def buscar(self):
        with open(file_users, 'r') as usuarios:
            data = json.load(usuarios)
            for usuario in data["users_account"]:
                if(self.id == usuario["dni"]):
                    TC = creditcard(usuario["num_card"])
                    return usuario["name"], TC.saldocard()


class creditcard:
    def __init__(self, codigocard):
        self.codigocard = codigocard

    def saldocard(self):
        saldo = self.__numero__card(self.codigocard)
        return saldo

    def __numero__card(self, codigocard):
        with open(file_cards, 'r') as creditcards:
            data = json.load(creditcards)
            for card in data["users_cards"]:
                if(self.codigocard == card["num_card"]):
                    return card["saldo"]


print("opciones: \n 1: Consulta saldo \n 2: Estatus Usuario \n 3: Estatus tarjeta\n")
opc = int(input("Opcion: "))
id = input("Id: ")

if opc == 1:
    data = Usuario(id)
    print(f"Hola {data.buscar()[0]} su saldo es: {data.buscar()[1]} USD")