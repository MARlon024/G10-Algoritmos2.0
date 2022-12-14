class Validar_codigo_deuda:
    def __init__(self, codigo_deuda):
        self.codigo_deuda = codigo_deuda

    def convalidar_codigo_deuda(self):
        if len(self.codigo_deuda) != 6 or self.codigo_deuda.isnumeric() == False:
            return False
        else:
            return True