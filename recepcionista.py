import json
import cliente
Cliente = cliente.Cliente

file_clientes = './resources/clientes.json'


class Recepcionista(Cliente):
    def __init__(self, id_recepcionista, id, dni, nombres, apellidos, correo_cliente, edad, sexo, correo_recepcionista, status):
        super().__init__(id, dni, nombres, apellidos, correo_cliente, edad, sexo)
        self.id_recepcionista = id_recepcionista
        self.correo_recepcionistas = correo_recepcionista
        self.status = status

    def agregar_clientes(datos, filename="./resources/clientes.json"):
        with open(filename, "r") as clientes:
            json.dump(datos, filename, indent=4)

    def transaccion():
        pass

    def registro():
        with open(file_clientes, "r") as nuevo_registro:
            data = json.load(nuevo_registro)
            temp = data["data_clientes"]
            y = {
                "dni": "26572417",
                "nombres": "PEDRO",
                "apellidos": "SUAREZ VERTIZ",
                "correo_cliente": "pedrito.suarez@gmail.com",
                "edad": "45",
                "sexo": "Masculino",
                "status": "activo"
            }
            temp.append(y)
        with open(file_clientes, "r") as clientes:
            json.dump(data, file_clientes, indent=4)  

    def modificar():
        pass

    def eliminar():
        pass

    def bloqueoTarjeta():
        pass

    def historialBancario():
        pass
