import random
import datetime
import sqlite3
cn = sqlite3.Connection("Usuarios")
cursor = cn.cursor()
#cursor.execute('''
#    CREATE TABLE TARJETA(
#	DNI VARCHAR(10),
#    NTARJETA VARCHAR(20),
#	CSATARJETA VARCHAR(20),
#	CVV VARCHAR(4),
#	FV VARCHAR(8))
# ''')#Podemos poner "UNIQUE" al final de nombre

class Generar_tarjeta():
	def __init__(self, BIN,DNI):
		self.BIN = BIN.replace(" ","")
		self.DNI=DNI
		cn=sqlite3.Connection("Usuarios")
		cursor=cn.cursor()
		ele_tarjeta=[]
		#Impresión de datos
		ele=[self.DNI,self.crear_numero(self.BIN),self.generar_codigo_cajero(),
				self.generar_codigo_ccv(),self.generar_fecha_venc()]
		ele_tarjeta.append(ele)
		for e in ele_tarjeta:
			tj=e[1]
			ccv=e[2]
			fv=e[3]
		print("Su tarjeta ha sido creada:")
		print("Número de tarjeta: ",tj)
		print("CCV: ",ccv)
		print("Fecha de Vencimiento: ",fv)
		cursor.execute("INSERT INTO TARJETA VALUES (?,?,?,?,?)", ele)
		cn.commit()
		
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
		return fecha["fecha_acortada"]
	
	def llenado(self,numero):
		numero_final = numero
		for i in range(0,16-len(numero)):
			numero_final+= "x"
		return numero_final

	def generar_codigo_ccv(self):
		return str(random.randint(100,998))

	def generar_codigo_cajero(self):
		return str(random.randint(1000,9998))
	

#bin_muestra = "4509xxxxxxxxxxxx"  #BIN Visa

#Lectura de datos de tarjeta
#num = Generar_tarjeta(bin_muestra)

