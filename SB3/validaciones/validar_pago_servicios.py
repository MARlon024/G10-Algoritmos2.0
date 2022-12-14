class Validar_pago_servicios:
    def __init__(self,saldo,monto):
        self.saldo=saldo
        self.monto = monto

    def validar_pago(self):
        if self.saldo>=self.monto:
            return True
        else:
            return False