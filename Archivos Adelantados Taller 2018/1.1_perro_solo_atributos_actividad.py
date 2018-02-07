# Class exercises
# Como accedemos a los atributos

class Perro:
    nombre = "Maya"
    edad = 3
    color = "blanco con manchas negras"
    patas = 4
    orejas = 2
    cola = 1
    agresividad = 4   # 1 min, 10 max


# creando una copia del objeto:
maya = Perro()


print("")
print("Actividad:")

# accediendo a sus atributos
print(maya.nombre)
print(maya.edad)
print(maya.color)

# Reto
print("")
print("Reto:")
print("Nombre:" + maya.nombre)
print("Edad:" + str(maya.edad))  # Tenga en cuenta el tipo de dato!
print("Color:" + maya.nombre)