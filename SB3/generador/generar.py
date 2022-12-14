import random
import datetime
import uuid
import getpass
from cryptography.fernet import Fernet
# Falta la llave y guardarlo


class Generar:
    def __init__(self, num_cuenta):
        self.num_cuenta = num_cuenta
        self.num_tarje = "4509xxxxxxxxxxxx"

    def generar_tarjeta(self):

        id_tarjeta = str(uuid.uuid1())
        status = "Activo"
        ele_tarjeta = [id_tarjeta, self.num_cuenta, self.crear_numero(self.num_tarje), self.generar_fecha_venc(),
                       self.generar_codigo_ccv(), self.generar_clave(), status]
        return ele_tarjeta

    def gen_aleatorio(self, bin):
        numero = ""
        for i in bin:
            numero += str(random.randint(0, 9)) if i.lower() == "x" else i
        return numero

    def crear_numero(self, bin):  # Genera numeros aleatorios
        numero = self.gen_aleatorio(bin)
        for i in range(1, 1000):
            numero = self.gen_aleatorio(bin)
            revision = self.checar(numero)
            if (revision and numero):
                # ENCRIPTACION
                numero = Fernet.generate_key()
                fernet = Fernet(numero)
                cod_encrypt = str(numero)
                encMessage = fernet.encrypt(cod_encrypt.encode())
                numero = encMessage
                return numero

    def checar(self, cc):  # Valida la secuencia de la tarjeta
        num = list((map(int, str(cc))))
        return sum(num[::-2] + [sum(divmod(d * 2, 10)) for d in num[-2::-2]]) % 10 == 0

    def generar_fecha_venc(self):
        fecha = {
            "anio": None,
            "mes": None,
            "fecha_completa": None,
            "fecha_acortada": None
        }

        def generar_anio():
            ahora = datetime.datetime.now()
            anio_actual = ahora.year
            return anio_actual + 5
        fecha["anio"] = str(generar_anio())

        def generar_mes():
            mes = random.randint(1, 12)
            if (mes > 9):
                return str(mes)
            else:
                return "0"+str(mes)
        fecha["mes"] = generar_mes()
        fecha["fecha_completa"] = fecha["mes"] + "/" + fecha["anio"]  # 12/2027
        fecha["fecha_acortada"] = fecha["mes"] + \
            "/" + fecha["anio"][2:]  # 12/27
        return fecha["fecha_acortada"]

    def generar_codigo_ccv(self):
        ccv = str(random.randint(100, 998))
        # ENCRIPTACION
        ccv = Fernet.generate_key()
        fernet = Fernet(ccv)
        cod_encrypt = str(ccv)
        encMessage = fernet.encrypt(cod_encrypt.encode())
        ccv = encMessage
        return ccv

    def generar_clave(self):
        print("Introducir clave")
        clave = getpass.getpass()
        # ENCRIPTACION
        clave = Fernet.generate_key()
        fernet = Fernet(clave)
        cod_encrypt = str(clave)
        encMessage = fernet.encrypt(cod_encrypt.encode())
        clave = encMessage
        return clave

    def generar_num_cuenta(self):
        num1 = str(random.randint(100, 1000))
        num2 = str(random.randint(1000, 10000))
        num3 = str(random.randint(1000, 10000))
        num_cuenta = "191"+num1+num2+num3
        return num_cuenta
