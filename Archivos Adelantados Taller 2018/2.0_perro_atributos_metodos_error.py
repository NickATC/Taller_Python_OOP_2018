# Class exercises
# Agreguemos un método.  

class Perro:
    nombre = "Maya"
    edad = 3
    color = "blanco con manchas negras"
    patas = 4
    orejas = 2
    cola = 1
    agresividad = 4   # 1 min, 10 max

    def ladrar():
        #Una vez haya accedido a los atributos, creemos un metodo -> una función dentro de una class :)
        print("Guau Guau!!")


maya = Perro()


#accediendo a los metodos:
maya.ladrar()
