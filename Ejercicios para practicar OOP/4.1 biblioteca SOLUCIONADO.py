# -*- coding: utf-8 -*-

# Ejercicio 4  SOLUCIONADO

# Crear un programa para llevar control de libros en una biblioteca.

# Requisitos:
# 1.  Crear un manejo sencillo de una biblioteca
# 2.  Ya esta escrito el menú donde usuario puede Ver lista de libros, pedir, devolver libros y salir del programa.
# 3.  La lista de libros es muy sencilla. Lo importante acá es poder acceder y manipular objetos
# 4.  La Biblioteca puede ostrar__libros_disponibles, prestar_libro, y agregar_libro a la lista de libros disponibles 
# 5.  El Cliente puede pedir_libro y regresar_libro a la biblioteca
# 5.  En las líneas 61 y 62  están creados los dos objetos:  biblioteca y cliente.
# 
# Este ejercicio es interesante por que requiere el uso y la interacción de dos Class:  
#      Biblioteca (para el manejo interno de los libros) y
#      Cliente (que es quien pide y regresa los libros)
# Desde el menú de opciones, dirija el código al método que corresponda, por ejemplo si el usuario va a pedir 
# un libro, el orden sería así:
#        1.  El cliente pedirá el libro (Método del Cliente).    Línea 78
#        2.  Internamente verifique si el libro esta en la lista de libros disponibles (Atributo de Biblioteca).  Línea 37
#            Si esta disponible, la Biblioteca lo retira de la lista (método de Biblioteca)
#            SI NO esta disponible, un mensaje le dirá al usuario que no esta disponible.
#         DEJO ESTE CÓDIGO PARA QUE USTED VEA LA FORMA DE INTERACTUAR ENTRE LAS DOS CLASSES


class Biblioteca:
    def __init__(self):
        self.libros_disponibles = ["Think Python", "SQL", "Algoritmos"]

    def mostrar_libros_disponibles(self):
        print("Libros disponibles:")
        for i in self.libros_disponibles:
            print(i)
        print("")

    def prestar_libro(self, libro_solicitado):
        if libro_solicitado in self.libros_disponibles:
            print("Ahora usted tiene ese libro por 8 días.")
            self.libros_disponibles.remove(libro_solicitado)
        else:
            print("Lo siento, ese libro ya no está disponible")

    def agregar_libro(self, libro_regresado):
        self.libros_disponibles.append(libro_regresado)
        print("Libro regresado a la biblioteca.  Gracias")


class Cliente:
    def pedir_libro(self):
        print("Entre el nombre del libro que quiere solicitar:")
        self.libro_solicitado = input("> ")
        return self.libro_solicitado

    def regresar_libro(self):
        print("Ingrese el nombre del libro que quiere regresar:")
        self.libro_regresado = input("> ")
        return self.libro_regresado

biblioteca = Biblioteca()
cliente = Cliente()

while True:
    print()
    print("Bienvenido a su biblioteca")
    print("Seleccione una opción:")
    print("1 para ver lista de libros disponibles.")
    print("2 para pedir un libro.")
    print("3 para regresar un libro.")
    print("4 para salir")
    opcion = int(input(">  "))

    if opcion is 1:
        biblioteca.mostrar_libros_disponibles()
    elif opcion is 2:
        libro_solicitado = cliente.pedir_libro()
        biblioteca.prestar_libro(libro_solicitado)
    elif opcion is 3:
        libro_regresado = cliente.regresar_libro()
        biblioteca.agregar_libro(libro_regresado)
    elif opcion is 4:
        quit()
    else:
        print("Opción inválida")
