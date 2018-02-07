# -*- coding: utf-8 -*-

# Ejercicio 1

# Crear un cajero automático muy sencillo

# Requisitos:
# 1.  No habrá login.  Simplemente cree las opciones de un ATM
# 2.  Ya tiene un menú con las 4 opciones principales.
# 3.  En la línea 34 esta creado un objeto y como atributo pasamos un valor de 100.
# 4.  En el menú hay creada una variable 'cantidad' (líneas 55 y 60) úsela para pedir al usuario 
#     valor a retirar o a depositar.
# 5.  Vamos a mantenerlo muy sencillo.  No analicemos los errores (Ingreso de letras, etc))


class ATM:
    def __init__(self, balance):
        self.__balance = balance

    def ver_balance(self):
        pass

    def retirar(self):
        pass

    def consignar(self):
        pass

    def finalizar_transaccion(self):
        # Si la opción es 4, simplemente salimos:
        quit()


account1 = ATM(100)


while True:
    print("")
    print("        ************      ")
    print("Bienvenido a su banco.")
    print("Por favor seleccione una opción: \n")

    print("Seleccione 1 para ver su balance.")
    print("Seleccione 2 para hacer un retiro.")
    print("Seleccione 3 para hacer una consignación.")
    print("Seleccione 4 para terminar su transacción.")
    print("        ************      \n")

    opcion = (int(input("> ")))
    if opcion is 1:
        # Escriba el código si la opción es 1

    elif opcion is 2:
        print("Ingrese la cantidad a retirar: ")
        cantidad = int(input("> "))
        # Escriba el código si la opción es 2

    elif opcion is 3:
        print("Ingrese la cantidad a consignar: ")
        cantidad = int(input("> "))
        # Escriba el código si la opción es 3

    elif opcion is 4:
        # Escriba el código si la opción es 4