class Validar_num_cuenta:
    def __init__(self, num_cuenta):
        self.num_cuenta = num_cuenta

    def convalidar_num_cuenta(self):
        if len(self.num_cuenta) != 14 or self.num_cuenta.isnumeric() == False:
            return False
        else:
            return True
