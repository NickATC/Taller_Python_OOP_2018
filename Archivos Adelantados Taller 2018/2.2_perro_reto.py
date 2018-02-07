# Class exercises

#  Reto.
# Modificar el metodo sentarse().  output >> Maya se esta sentando!
# Modificar el metodo dormir().    output >> Maya se va a dormir ya mismo!


class Perro:
    nombre = "Maya"
    edad = 3
    color = "blanco con manchas negras"
    patas = 4
    orejas = 2
    cola = 1
    agresividad = 4   # 1 min, 10 max

    def ladrar(self):
        print("Guau Guau!!")

    def sentarse(self):
        print("{} se esta sentando!".format(nombre))

    def dormir(self):
        print("{} se va a dormir ya mismo!".format(nombre))


maya = Perro()

# accediendo a los metodos:
maya.ladrar()
maya.sentarse()
maya.dormir()
