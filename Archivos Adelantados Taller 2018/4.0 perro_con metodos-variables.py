# Class exercises
# No todos los perros se llaman Maya...  agreguemos variables


class Perro:
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.edad = 3
        self.color = "blanco con manchas negras"
        self.patas = 4
        self.orejas = 2
        self.cola = 1
        self.agresividad = 4   # 1 min, 10 max

    def ladrar(self):
        #Una vez haya accedido a los atributos, creemos un metodo -> una función dentro de una class :)
        print("Guau Guau!!")

    def sentarse(self):
        print("{} se esta sentando!".format(self.nombre))
        
    def dormir(self):
        print("{} se va a dormir".format(self.nombre))



# Tarea:
# Crear instancias con diferentes nombres.
# Crear otros objetos cuyo nombre sean: "Dana", "Milo" 
# imprimir los 3 metodos usando los nombres respectivos de los perros.

dana = Perro("Dana")
dana.sentarse()
dana.dormir()


milo = Perro("Milo")
milo.sentarse()
milo.dormir()