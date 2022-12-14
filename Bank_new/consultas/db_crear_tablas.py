import sqlite3

file_database = "DataBase/banquito.db"


def createDataBase():
    conn = sqlite3.connect(file_database)
    conn.commit()
    conn.close()


def createTableRecepcionista():
    conn = sqlite3.connect(file_database)
    cursor = conn.cursor()
    instruccion = f"""
        CREATE TABLE recepcionistas(
            dni INTEGER(8),
            nombre TEXT,
            apellido_Pat TEXT,
            apellido_Mat TEXT,
            correo VARCHAR(50),
            fecha_nac VARCHAR(10),
            celular INTEGER(9),
            operadora TEXT,
            usuario VARCHAR(10),
            contraseña VARCHAR(150),
            status CHAR
        )
    """
    cursor.execute(instruccion)
    conn.commit()
    conn.close()


def insertRowRecepcionista(dni, nombre, ape_Pat, ape_Mat, correo, fech, cel, oper, user, psw, status):
    conn = sqlite3.connect(file_database)
    cursor = conn.cursor()
    instruccion = f"INSERT INTO recepcionistas VALUES ('{dni}','{nombre}','{ape_Pat}','{ape_Mat}','{correo}','{fech}','{cel}','{oper}','{user}','{psw}','{status}')"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()


def createTableCliente():
    conn = sqlite3.connect(file_database)
    cursor = conn.cursor()
    instruccion = f"""CREATE TABLE clientes(
        id_cliente BINARY(20),
        dni INTEGER,
        nombre VARCHAR(50),
        ape_pat VARCHAR(50),
        ape_mat VARCHAR(50),
        correo VARCHAR(50),
        fecha_nac VARCHAR(50),
        celular INTEGER,
        operador VARCHAR(50),
        num_cuenta VARCHAR(150)
        )
        """
    cursor.execute(instruccion)
    conn.commit()
    conn.close()


def createTableCuentasBancarias():
    conn = sqlite3.connect(file_database)
    cursor = conn.cursor()
    instruccion = f"""CREATE TABLE cuentas_bancarias(
        id_cuenta BINARY(20),
        dni INTEGER,
        num_cuenta VARCHAR(150),
        num_tarjeta VARCHAR(150),
        saldo FLOAT
        )
        """
    cursor.execute(instruccion)
    conn.commit()
    conn.close()


def createTableTarjetas():
    conn = sqlite3.connect(file_database)
    cursor = conn.cursor()
    instruccion = f"""
        CREATE TABLE tarjetas(
            id_tarjeta BINARY(20) PRIMARY KEY,
            dni INTEGER,
            num_tarjeta VARCHAR(150),
            fecha_venc VARCHAR(150),
            ccv VARCHAR(150),
            clave VARCHAR(150)
        )
    """
    cursor.execute(instruccion)
    conn.commit()
    conn.close()


def createTableDepositos():
    conn = sqlite3.connect(file_database)
    cursor = conn.cursor()
    instruccion = f"""
        CREATE TABLE depositos(
            id_operacion INTEGER PRIMARY KEY,
            num_cuenta INTEGER,
            monto FLOAT,
            fecha DATE,
            hora TIME
        )
    """
    cursor.execute(instruccion)
    conn.commit()
    conn.close()


def createTableRetiros():
    conn = sqlite3.connect(file_database)
    cursor = conn.cursor()
    instruccion = f"""
        CREATE TABLE retiros(
            id_operacion INTEGER PRIMARY KEY,
            num_cuenta INTEGER,
            monto FLOAT,
            fecha DATE,
            hora TIME
        )
    """
    cursor.execute(instruccion)
    conn.commit()
    conn.close()


def createTablePagoServicios():
    conn = sqlite3.connect(file_database)
    cursor = conn.cursor()
    instruccion = f"""
        CREATE TABLE pago_servicios(
            id_operacion INTEGER PRIMARY KEY,
            id_deuda VARCHAR(50),
            num_cuenta INTEGER,
            monto FLOAT,
            fecha DATE,
            hora TIME
        )
    """
    cursor.execute(instruccion)
    conn.commit()
    conn.close()


def createTableServicios():
    conn = sqlite3.connect(file_database)
    cursor = conn.cursor()
    instruccion = f"""
        CREATE TABLE servicios(
            id_deuda INTEGER PRIMARY KEY,
            cod_deuda VARCHAR(50),
            nombre VARCHAR(50),
            num_cuenta INTEGER,
            monto FLOAT,
            fecha_venc DATE
        )
    """
    cursor.execute(instruccion)
    conn.commit()
    conn.close()


def createTableTransferencias():
    conn = sqlite3.connect(file_database)
    cursor = conn.cursor()
    instruccion = f"""
        CREATE TABLE transferencias(
            id_operacion INTEGER PRIMARY KEY,
            desde VARCHAR(50),
            hasta VARCHAR(50),
            monto FLOAT,
            fecha DATE,
            hora TIME
        )
    """
    cursor.execute(instruccion)
    conn.commit()
    conn.close()


# createDataBase()
# createTableRecepcionista()
# dni = input("Dni: ")
# nombres = input("Nombres: ")
# ape_Pat = input("Apellido Paterno: ")
# ape_Mat = input("Apellido Materno: ")
# correo = input("Correo: ")
# fech = input("Fecha de nacimiento: ")
# cel = input("Celular: ")
# oper = input("Operadora: ")
# user = input("Usuario: ")
# psw = input("Contraseña: ")
# status = input("Status: ")
# insertRowRecepcionista(dni, nombres, ape_Pat, ape_Mat, correo,
#           fech, cel, oper, user, psw, status)
# createTableCliente()
createTableCuentasBancarias()
createTableTarjetas()
createTableDepositos()
createTableRetiros()
createTableServicios()
createTableTransferencias()
createTablePagoServicios()
