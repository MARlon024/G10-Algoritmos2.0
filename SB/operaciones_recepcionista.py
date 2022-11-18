import sqlite3
import uuid
import funciones
import getpass
from tarjeta import *
import transaccion

class Operaciones_recepcionista():
    def __init__(self, user_recep, psw_recep):
        self.__user_recep = user_recep
        self.__psw_recep = psw_recep

    def iniciar_sesion(self):
        sesion = self.__nueva_sesion(self.__user_recep, self.__psw_recep)
        return sesion

    def __nueva_sesion(self, __user_recep, __psw_recep):
        conn = sqlite3.connect("DataBase/Bank.db")
        cursor = conn.cursor()
        instruccion = f"SELECT * FROM recepcionistas WHERE usuario='{self.__user_recep}' AND contraseña='{self.__psw_recep}';"
        cursor.execute(instruccion)
        if not cursor.fetchone():
            return "Error al iniciar sesion"
        else:
            conex_seg = True
            return conex_seg

    def registro_cliente(self):
        registro = self.__registro_cliente()
        return registro

    def __registro_cliente(self):
        conn = sqlite3.Connection("DataBase/Bank.db")
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
        num_cuenta = "191" + funciones.generarNumero(11)
        existe = True
        while (existe):
            cursor.execute(
                f"SELECT * FROM clientes WHERE num_cuenta={num_cuenta}")
            lista1 = cursor.fetchall()
            if (lista1 == []):
                existe = False
            else:
                num_cuenta = "191" + funciones.generarNumero(11)
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
        generar = self.__generar_tarjeta()
        return generar

    def __generar_tarjeta(self):
        dni = input("DNI: ")
        dni = funciones.comprobarIngreso(dni, 8)
        RC = Tarjeta("4509xxxxxxxxxxxx", dni)
        return RC.generar_tarjeta()

    def bloquear_tarjeta(self):
        bloquear = self.__bloquear_tarjeta()
        return bloquear

    def __bloquear_tarjeta(self):
        dni = input("Dni: ")
        clave = getpass.getpass()
        conn = sqlite3.Connection("DataBase/Bank.db")
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
        renovar = self.__renovar_tarjeta()
        return renovar

    def __renovar_tarjeta(self):
        pass

    def transacciones(self):
        transaccion = self.__transaccion()
        return transaccion
    #ACAAAAAAAA
    def __transaccion(self):
        continuar=True
        while(continuar):
            try:
                opc = funciones.menuPrincipal()
                match(opc):
                    case 1:
                        cuenta_destino = input("Cuenta destino: ")
                        deposito = transaccion.Deposito()
                        try:
                            monto = float(input("Ingrese el monto a depositar \n"))
                        # REEMPLAZAR
                            deposito.operacion(monto, cuenta_destino) # REEMPLAZAR POR CUENTA INGRESADA PREVIAMENTE !!!
                            print("¡Depósito completado! \n")
                            fecha, hora = funciones.obtenerTiempo()
                            ID = "0" + funciones.generarNumero(9)
                            while (deposito.existeID(ID)):
                                ID = "0" + funciones.generarNumero(9)
                            funciones.mostrarDeposito(ID, monto, fecha, hora)
                            lista = funciones.exportarDeposito(ID, cuenta_destino,monto, fecha, hora)
                            deposito.mandarDatos(lista)
                            deposito.cerrarConexion()
                            continue
                        except ValueError:
                            print("\n ERROR: No puede ingresar variables que no sean números \n")
                        continue
                    case 2:
                        cuenta_origen = input("Cuenta origen: ")
                        transferencia = transaccion.Transferencia()
                        cuenta_destino = funciones.ingresoCuenta(cuenta_origen) #REEMPLAZAR POR CUENTA INGRESADA PREVIAMENTE !!!
                        if(transferencia.existeCuenta(cuenta_destino)):
                            try:
                                monto = float(input("Ingrese el monto a depositar: \n"))
                                if (transferencia.montoValido(monto, cuenta_origen)):  # REEMPLAZAR POR CUENTA INGRESADA PREVIAMENTE !!!
                                    transferencia.operacion(cuenta_origen, cuenta_destino, monto)  # REEMPLAZAR POR CUENTA INGRESADA PREVIAMENTE !!!
                                    print("¡Transacción completada!\n")
                                    fecha, hora = funciones.obtenerTiempo()
                                    ID = "1" + funciones.generarNumero(9)
                                    while(transferencia.existeID(ID)):
                                        ID = "1" + funciones.generarNumero(9)
                                    funciones.mostrarTransferencia(cuenta_destino, monto, ID, fecha, hora)
                                    lista = funciones.exportarTransferencia(ID, cuenta_origen, cuenta_destino, monto, fecha, hora)  # REEMPLAZAR POR CUENTA INGRESADA PREVIAMENTE !!!
                                    transferencia.mandarDatos(lista)
                                    transferencia.cerrarConexion()
                                    continue
                                else:
                                    continue
                            except ValueError:
                                print("\n ERROR: No puede ingresar variables que no sean números \n")
                        else:
                            continue
                    case 3:
                        cuenta_origen = input("Cuenta origen: ")
                        retiro = transaccion.Retiro()
                        try:
                            monto = float(input("Ingrese el monto a retirar \n"))
                            if(retiro.montoValido(monto, cuenta_origen)): # REEMPLAZAR POR CUENTA INGRESADA PREVIAMENTE !!!
                                retiro.operacion(cuenta_origen,monto) # REEMPLAZAR POR CUENTA INGRESADA PREVIAMENTE !!!
                                print("¡Retiro completado!\n")
                                fecha, hora = funciones.obtenerTiempo()
                                ID = "2" + funciones.generarNumero(9)
                                while(retiro.existeID(ID)):
                                    ID = "2" + funciones.generarNumero(9)
                                saldo = retiro.obtenerSaldo(cuenta_origen) # REEMPLAZAR POR CUENTA INGRESADA PREVIAMENTE !!!
                                funciones.mostrarRetiro(monto, saldo, ID, fecha, hora)
                                lista = funciones.exportarRetiro(ID,cuenta_origen, monto, fecha, hora) # REEMPLAZAR POR CUENTA INGRESADA PREVIAMENTE !!!
                                retiro.mandarDatos(lista)
                                retiro.cerrarConexion()
                                continue
                            else:
                                continue
                        except ValueError:
                            print("\n ERROR: No puede ingresar variables que no sean números \n")
                        continue
                    case 4:
                        dni = input("Dni: ")
                        cuenta_destino = input("Cuenta destino: ")
                        pagoServicios = transaccion.pagoServicios(cuenta_destino) #REEMPLAZAR POR CUENTA INGRESADA PREVIAMENTE!!!
                        deudas = pagoServicios.devolverDeudas()
                        funciones.mostrarDeudas(deudas)
                        try:
                            codigoDeuda = funciones.ingresoDeuda()
                            if (not pagoServicios.existeID(codigoDeuda)):
                                print("\n Este codigo no existe...\n \n")
                                continue
                            else:
                                monto = pagoServicios.deudaMonto(codigoDeuda)
                                if(pagoServicios.montoValido(monto,cuenta_destino)): # REEMPLAZAR POR CUENTA INGRESADA PREVIAMENTE !!!
                                    pagoServicios.operacion(dni,monto, codigoDeuda) # REEMPLAZAR POR CUENTA INGRESADA PREVIAMENTE !!!
                                    print("¡Servicio cancelado! \n")
                                    fecha, hora = funciones.obtenerTiempo()
                                    ID = "3" + funciones.generarNumero(9)
                                    while(pagoServicios.existeID(ID)):
                                        ID = "3" + funciones.generarNumero(9)
                                    funciones.mostrarServicio(ID, fecha, hora)
                                    lista = funciones.exportarServicio(ID, codigoDeuda, cuenta_destino, monto, fecha, hora) # REEMPLAZAR POR CUENTA INGRESADA PREVIAMENTE !!!
                                    pagoServicios.mandarDatos(lista)
                                    pagoServicios.cerrarConexion()
                                    continue
                                else:
                                    continue
                        except ValueError:
                            print("\n ERROR: No puede ingresar variables que no sean números \n")
                        continue
                    case 0:
                        continuar = False
                        continue
                    case _:
                        print("Ingrese una opción valida... \n")
                        continue
            except ValueError:
                return ("\n ERROR: No puede ingresar variables que no sean números \n")    