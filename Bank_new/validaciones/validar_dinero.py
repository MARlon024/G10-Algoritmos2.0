class Validar_dinero:
    def __init__(self,monto):
        self.monto = monto

    def convalidar_monto(self):
        if self.monto.isnumeric() == True:
            return True
        else:
            return False
    def convalidar_operacion(self,operacion):
        conva=self.monto-operacion
        if conva>0:
            return True
        else:
            return False
        