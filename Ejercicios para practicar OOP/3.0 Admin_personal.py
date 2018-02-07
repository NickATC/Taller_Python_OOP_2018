# -*- coding: utf-8 -*-

# Ejercicio 3

# Crear un sencillo administrador de personal que ingresa a una empresa.

# Requisitos:
# 1.  Nuestro programa aceptará como parámetros PRIMER NOMBRE, PRIMER APELLIDO, ID, y CARGO.
# 2.  Una vez ejecutemos el código, nos creará un codigo de empleado, nos asignará un 
#     correo electrónico y una contraseña única para ese correo, así:
#  2.1 El codigo del empleado será el numero de ID con la primera letra del nombre y la primera del apellido
#      Ejemplo.  Si la ID de Pedro Perez es 12345678, su número de empleado será 12345678pp
#  2.2 Solo hay dos posibilidades de cargo:  OPERARIO o ADMINISTRATIVO. El correo variará dependiendo de este ítem.
#  2.3 El correo electrónico será las dos primeras letras del nombre seguida de un punto y el apellido, y  terminará 
#      en @empresa.com
#      ejemplo: Para Pedro Perez trabajando como Operario, el correo será:  pe.perez.oper@empresa.com
#      ejemplo: Para Pedro Perez trabajando como Administrativo, el correo será:  pe.perez.admin@empresa.com
#  2.4 La contraseña tendrá 9 caracteres y serán números, letras y/o símbolos.  Use los caracteres en línea 22
#      Para elegir de estos caracteres, use 'random.choice(caracteres)'
# 3.  Una vez creada toda esta información, la imprimirá en el CMD
# 4.  En líneas 56, 57 y 58 hay 3 objetos con los 4 parámetros a pasar.  Practique con ellos.


import random

#Letras, números y símbolos para contraseña
caracteres = "abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVXYZ1234567890@-!#$%+*~&¿?;:/="

class Empleado:
    def __init__(self):
        pass  

    def crear_email(self):
        pass

    def crear_password(self):
        for i in range(0, 9):
            char = random.choice(caracteres)
            # Agregue acá código para agregar 9 ítems a self.password
        return self.password
    
    def crear_empleado(self):
        """use este método para imprimir todo en el CMD, así:
        Nombre : Pedro
        Apellido : Perez
        Id : 80442789
        Cargo : Administrativo
        Código de empleado: 80442789pp
        Email : pe.perez.admin@empresa.com
        Password : y~r5TXe0e                  """
        pass




empleado1 = Empleado("Pedro", "Perez", "80442789", "Administrativo")
empleado2 = Empleado("Juan", "Quintero", "7756489", "operario")
empleado3 = Empleado("Ana", "Jimenez", "50426321", "Administrativo")
