# Class exercises

# Reto
# Agregar un metodo llamado describir_perro()
# output:  >> Maya es un dalmata de color blanco con manchas negras.
# tres posibles soluciones!!


class Perro:
    def __init__(self, nombre, raza, color):   
        self.nombre = nombre
        self.edad = 3
        self.raza = raza
        self.color = color
        self.patas = 4
        self.orejas = 2
        self.cola = 1
        self.agresividad = 4   # 1 min, 10 max

    def ladrar(self):
        print("Guau Guau!!")

    def sentarse(self):
        print("{} se esta sentando!".format(self.nombre))
        
    def dormir(self):
        print("{} se va a dormir".format(self.nombre))

    def describir_perro(self):
        print(self.nombre + " es un  " +  self.raza + " y es de color " + self.color)
        print("{} es un {} y es de color {}".format(self.nombre, self.raza, self.color))
        print(f"{self.nombre} es un {self.raza} y es de color {self.color}")



#creando una copia del objeto:
maya = Perro("Maya", "dalmata", "blanco con manchas negras.")
maya.describir_perro()

# print("")
# dana = Perro("Dana", "doberman", "negro")
# dana.describir_perro()

# print("")
# firulais = Perro("Firulais", "frech poodle", "blanco")
# firulais.describir_perro()
