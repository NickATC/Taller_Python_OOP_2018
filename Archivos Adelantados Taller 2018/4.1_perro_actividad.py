# Class exercises
# Actividad.  Agregemos variables de raza y color.


class Perro:
    def __ini__(self, nombre)    
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


#creando una copia del objeto:
maya = Perro()