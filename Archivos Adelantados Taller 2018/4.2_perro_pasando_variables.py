# Class exercises
# Agreguemos mas variables:  Raza y color. 
# Agreguemos mas metodos:  describir() que output sea:  "Maya es un dalmata de color blanco."


class Perro:
    
    def __init__(self, nombre, color, raza):
        self.nombre = nombre
        self.patas = 4
        self.orejas = 2
        self.cola = 1
        self.color = color
        self.sonido = "guau"
        self.raza = raza

    def ladrar(self):
        #Una vez haya accedido a los atributos, creemos un metodo -> una función dentro de una class :)
        print("Guau Guau!!")

    def sentarse(self):
        print("{} se esta sentando!".format(self.nombre))
        
    def dormir(self):
        print("{} se va a dormir".format(self.nombre))

    def describir_perro(self):
        print("{} es un {} de color {}".format(self.nombre, self.raza, self.color))

# Tarea:
# Crear instancias con diferentes nombres.
# Crear otros objetos cuyo nombre sean: "Dana", "Milo" 
# imprimir los 3 metodos usando los nombres respectivos de los perros.

dana = Perro("Dana", "negro", "doberman")
dana.sentarse()
dana.dormir()
dana.describir_perro()


milo = Perro("Milo", "blanco", "poodle")
milo.sentarse()
milo.dormir()
milo.describir_perro()