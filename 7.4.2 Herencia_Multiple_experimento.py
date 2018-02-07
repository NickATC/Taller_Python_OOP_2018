# -*- coding: utf-8 -*-

# Herencia múltiple  Experimento.  __init__ en todas las class

class Padre:
    def __init__(self, color_ojos,  color_piel):
        self.color_ojos = color_ojos
        self.color_piel = color_piel


class Madre:
    def __init__(self, color_pelo):
        self.color_pelo = color_pelo


#a la clase HIJO herede Padre y Madre
class Hijo(Padre, Madre):
    def __init__(self, color_ojos,  color_piel, color_pelo):
        Padre.__init__(self, color_ojos,  color_piel)
        Madre.__init__(self, color_pelo)
        
        self.color_ojos = "azulitos del hijo"
        

# Instance Hijo
nicolas = Hijo("azules", "blanco", "pelo rubio")

# Acceda a atributos de ambos.
print(nicolas.color_ojos)
print(nicolas.color_piel)
print(nicolas.color_pelo)