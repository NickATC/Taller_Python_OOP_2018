# Class exercises

# Reto opcional !
# Crear una lista con 5 nombres
# Crear una lista con 5 razas
# Crear una lista con 5 colores
# Al instanciar, que se elijan el nombre, raza y color de forma aleatoria

import random

nombres_perros = ["firulais", "maya", "motas", "dana", "mara", "puka"]
color_perros = ["cafe", "negro", "blanco", "chocolate"]
razas_perros = ["doberman", "dalmata", "labrador",
                "golden retriever", "french poodle", "pinscher"]


class Perro:

    def __init__(self, nombre, color, raza):
        self.nombre = nombre
        self.edad = 3
        self.patas = 4
        self.orejas = 2
        self.cola = 1
        self.color = color
        self.sonido = "guau"
        self.raza = raza
        self.ladrar()

    def ladrar(self):
        print("Guau Guau!!")

    def sentarse(self):
        print("{} se esta sentando!".format(self.nombre))

    def dormir(self):
        print("{} se va a dormir".format(self.nombre))

    def describir(self):
        print("{} es un {} de color {}".format(
            self.nombre, self.raza, self.color))
        print("")

# Tarea:
# Crear instancias con diferentes nombres.
# Crear otros objetos cuyo nombre sean: "Dana", "Milo"
# imprimir los 3 metodos usando los nombres respectivos de los perros.


dana = Perro("Dana", "negro", "doberman")
dana.sentarse()
dana.dormir()
dana.describir()

print("")

milo = Perro("Milo", "blanco", "poodle")
milo.sentarse()
milo.dormir()
milo.describir()
print("")

any_perro = random.choice(nombres_perros)
any_perro = Perro(any_perro, random.choice(color_perros), random.choice(razas_perros))
any_perro.sentarse()
any_perro.dormir()
any_perro.describir()
