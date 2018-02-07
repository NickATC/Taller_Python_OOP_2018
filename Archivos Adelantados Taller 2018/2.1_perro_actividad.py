# Class exercises
#Agreguemos un método usando (self).  Actividad de agregar otros 2 métodos.

class Perro:
    nombre = "Maya"
    edad = 3
    color = "blanco con manchas negras"
    patas = 4
    orejas = 2
    cola = 1
    agresividad = 4   # 1 min, 10 max

    def ladrar(self):
        # Una vez haya accedido a los atributos, creemos un metodo -> una función dentro de una class :)
        print("Guau Guau!!")

    def sentarse(self):
        print("El perro se esta sentando!")

    def dormir(self):
        print("El perro se va a dormir ya mismo!")


maya = Perro()

#  Actividad.
# Crear un metodo donde el perro se siente. Nombre del metodo >sentarse().  output >> El perro se esta sentando!
# Crear otro metodo donde el perro se vaya a dormir. Nombre del metodo >dormir()  output >> El perro se va a dormir ya mismo!

# accediendo a los metodos:
maya.ladrar()
maya.sentarse()
maya.dormir()
