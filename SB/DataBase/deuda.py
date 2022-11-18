class DBDeuda:
    def __init__(self):
        self.conexionCuentas = sqlite3.Connection("DataBase/Bank.db")

    def save_deuda(deuda):
        cursor = self.conexionCuentas.cursor()
        cursor.execute("INSERT INTO pago_servicios VALUES(?,?,?,?,?,?)", DBDeuda)

    def buscar_deuda(deuda):
        cursor = self.conexionCuentas.cursor()
        cursor.execute("SELECT * FROM pago_servicios WHERE dni=?", deuda.dni)
