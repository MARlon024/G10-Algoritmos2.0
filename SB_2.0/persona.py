class Persona():
    def __init__(self ,__nom, __dni,__ape_pa,__ape_ma,__correo,__fecha,__cel=None,__cel_ope=None):
        self.nom = __nom
        self.dni = __dni
        self.ape_pa=__ape_pa
        self.ape_ma=__ape_ma
        self.correo=__correo
        self.fecha=__fecha
        self.cel=__cel    
        self.cel_ope=__cel_ope
    def getDNI(self):
        return self.__dni