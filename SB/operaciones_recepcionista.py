from operaciones.deposito import deposito
from operaciones.retiro import retiro
from operaciones.transferencia import transferencia
from operaciones.pago_servicios import pagos_servicios
import funciones
from tarjeta import *


class Operaciones_recepcionista():
    def __init__(self, user_recep, psw_recep):
        self.__user_recep = user_recep
        self.__psw_recep = psw_recep
        self.path=r'SB\DataBase\Bank.db'
    def iniciar_sesion(self):
        conn = sqlite3.connect(self.path)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM recepcionistas WHERE usuario='{self.__user_recep}' AND contraseña='{self.__psw_recep}'")  
        product = cursor.fetchall()
        
        if cursor.fetchone() == False:
            return False
        else:
            return True
        
    def registrar_cliente(self):
        conn = sqlite3.Connection(self.path)
        cursor = conn.cursor()
        veri = ""
        user_recep = []
        boi = False
        print("-------REGISTRO-------")
        id_cliente = str(uuid.uuid1())  # GENERANDO CODIGO UUID
        dni=""
        while (len(dni) != 8 or dni.isnumeric() == False or boi == False):
            dni = input("DNI: ")
            dni = dni.strip()
            cursor.execute(f"SELECT * FROM clientes WHERE dni ={dni}")
            product = cursor.fetchall()
            for p in product:
                veri = p[1]
            if (len(dni) != 8 or dni.isnumeric() == False):
                print("Introducir sus 8 dígitos de DNI")
            else:
                if (veri == ""):
                    boi = True
                else:
                    print("Ya existe una cuenta bancaria vinculada a este DNI")
            veri = ""
        nom = input("Nombre: ").capitalize()
        ape_pa = input("Apellido paterno: ").capitalize()
        ape_ma = input("Apellido materno: ").capitalize()
        correo = input("Correo Personal: ")
        while correo.__contains__("@") != True or correo.__contains__(".") != True:
            correo = input("Correo Personal: ")
            if (correo.__contains__("@") == False or correo.__contains__(".") == False):
                print("Introducir un correo valido ")

        fecha_nac = input("Fecha de nacimiento: ")
        cel = input("Celular: ")
        while (len(cel) != 9 or cel.isnumeric() == False):
            cel = input("Celular: ")
            if (len(cel) != 9 or cel.isnumeric() == False):
                print("Introducir sus 9 dígitos de celular")
        cel_ope = input("Operadora: ")
        num_cuenta = "191" + funciones.generar_numero(11)
        existe = True
        while (existe):
            cursor.execute(
                f"SELECT * FROM clientes WHERE num_cuenta={num_cuenta}")
            lista1 = cursor.fetchall()
            if (lista1 == []):
                existe = False
            else:
                num_cuenta = "191" + funciones.generar_numero(11)
        ele = [id_cliente, dni, nom, ape_pa, ape_ma,
               correo, fecha_nac, cel, cel_ope, num_cuenta]
        user_recep.append(ele)
        id_cuenta = str(uuid.uuid1())
        tarjeta = 'INACTIVO'
        cursor.execute(
            "INSERT INTO clientes VALUES (?,?,?,?,?,?,?,?,?,?)", ele)
        ele2 = [id_cuenta, dni, num_cuenta, tarjeta, 0]
        cursor.execute(
            "INSERT INTO cuentas_bancarias VALUES (?,?,?,?,?)", ele2)
        conn.commit()
        conn.close()
        return (f"FELICIDADES {nom} SU CUENTA HA SIDO CREADA. Su numero de cuenta es: {num_cuenta}")

    def generar_tarjeta(self):
        dni = input("DNI: ")
        dni = funciones.comprobar_ingreso(dni, 8)
        RC = Tarjeta("4509xxxxxxxxxxxx", dni)
        return RC.generar_tarjeta()

    def bloquear_tarjeta(self):
        dni = input("Dni: ")
        clave = getpass.getpass()
        conn = sqlite3.Connection(self.path)
        cursor = conn.cursor()
        status = "Bloqueada"
        sql1 = f"UPDATE cuentas_bancarias SET tarjeta='{status}' WHERE dni={dni}"
        sql2 = f"UPDATE tarjetas SET status='{status}' WHERE dni={dni}"
        cursor.execute(sql1)
        cursor.execute(sql2)
        conn.commit()
        conn.close()
        return ("Operacion Realizada con Exito")

    def renovar_tarjeta(self):
        pass

    def transacciones(self):
        continuar=True
        while(continuar):
            try:
                opc = funciones.menu_principal()
                match(opc):
                    case 1:
                        deposito()
                        continue
                    case 2:
                        transferencia()
                        continue
                    case 3:
                        retiro()
                        continue
                    case 4:
                        pagos_servicios()
                        continue
                    case 0:
                        continuar = False
                        continue
                    case _:
                        print("Ingrese una opción valida... \n")
                        continue
            except ValueError:
                return ("\n ERROR: No puede ingresar variables que no sean números \n")    