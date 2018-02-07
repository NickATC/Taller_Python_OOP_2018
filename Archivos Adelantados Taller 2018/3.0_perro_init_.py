# Class exercises
# Inicialicemos los atributos de Perro
# Accedamos a los atributos desde los metodos

class Perro:
    
    def __init__(self):
        self.nombre = "Maya"
        self.edad = 3
        self.color = "blanco con manchas negras"
        self.patas = 4
        self.orejas = 2
        self.cola = 1
        self.agresividad = 4   # 1 min, 10 max
       
    def ladrar(self):
        print("Guau Guau!!")

    def sentarse(self):
        print("{} se esta sentando!".format(nombre))
        
    def dormir(self):
        print("{} se va a dormir".format(nombre))