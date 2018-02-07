class Padre:
    color_ojos = "azules del padre"
    color_piel = "blanco del padre"

class Hijo(Padre):
    def __init__(self):
        self.color_ojos = "verdes del hijo"
        self.color_pelo = "rubio hijo"
    
nicolas = Hijo()
print(nicolas.color_ojos)
print(nicolas.color_pelo)
print(nicolas.color_piel)
