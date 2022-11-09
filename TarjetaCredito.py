import random
import datetime

class Generar_tarjeta():
	def __init__(self, BIN):
		self.BIN = BIN.replace(" ","")

		#Generación de tarjeta
		print("Datos de la tarjeta creada")
		self.lista_tarjetas = []
		self.dic_tarjetas = {}
		tarj_creada = self.crear_tarjeta()
		self.lista_tarjetas.append(tarj_creada["datos_completos"])
		#Impresión de datos
		for n in self.lista_tarjetas:
			print("Numero de tarjeta | CVV | fecha de vencimiento")
			print(n)

	def crear_tarjeta(self):
		tarjeta = {}
		tarjeta["numero_tarjeta"] = self.crear_numero(self.BIN)
		tarjeta["codigo_seg"] 	  = self.generar_codigo_seguridad()
		tarjeta["vencimiento"]	  = self.generar_fecha_venc()
		self.string = ""
		self.string += tarjeta["numero_tarjeta"]
		self.string += "  | " + tarjeta["codigo_seg"]
		self.string += " | " + tarjeta["vencimiento"]["fecha_acortada"]
		tarjeta["datos_completos"] = self.string
		return tarjeta
		
	def gen_aleatorio(self, BIN):	
		numero = ""
		for i in BIN:
			numero+= str(random.randint(0,9)) if i.lower() == "x" else i
		return numero
		
	def crear_numero(self, BIN): #Genera numeros aleatorios 
		numero = self.gen_aleatorio(BIN)
		for i in range(1,1000):
			numero = self.gen_aleatorio(BIN)
			revision = self.checar(numero)
			if(revision and numero):
				return numero
		
	def checar(self, cc):  #Valida la secuencia de la tarjeta
		num = list((map(int, str(cc))))
		return sum(num[::-2] + [sum(divmod(d * 2, 10)) for d in num[-2::-2]]) % 10 == 0


	def generar_fecha_venc(self):
		fecha = {
			"anio":None,
			"mes":None,
			"fecha_completa":None,
			"fecha_acortada":None
		}
		def generar_anio():
			ahora = datetime.datetime.now()
			anio_actual = ahora.year
			return anio_actual  + 5
		fecha["anio"] = str(generar_anio())
		
		def generar_mes():
			mes = random.randint(1,12)
			if(mes > 9):
				return str(mes)
			else:
				return "0"+str(mes)	
		fecha["mes"] = generar_mes()

		fecha["fecha_completa"] = fecha["mes"] + "/" + fecha["anio"]       #12/2027
		fecha["fecha_acortada"] = fecha["mes"] + "/" + fecha["anio"][2:]   #12/27
		return fecha
	
	def llenado(self,numero):
		numero_final = numero
		for i in range(0,16-len(numero)):
			numero_final+= "x"
		return numero_final

	def generar_codigo_seguridad(self):
		return str(random.randint(100,999))
	

bin_muestra = "4509xxxxxxxxxxxx"  #BIN Visa
num = Generar_tarjeta(bin_muestra)

with open("tarjetas_creadas.txt", "a") as contenido:
	contenido.write(str(num.lista_tarjetas))
	contenido.close()
