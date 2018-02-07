class Padre:
    def __init__(self):
        self.color_ojos = "azules del padre"
        self.color_piel = "blanco del padre"

class Hijo(Padre):
    color_ojos = "azules del hijo"
    color_pelo = "rubio hijo"
    
nicolas = Hijo()
print(nicolas.color_ojos)
print(nicolas.color_pelo)
print(nicolas.color_piel)
