#composition using OOP

class Addition:
    def __init__(self, x, y):
        self.x = x
        self.y = y
       
    def sum(self):
        self.value = self.x + self.y
        print(self.value)

class Substraction:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def subs(self):
        value = self.x - self.y
        print(value)


class Calculator:
    """A first attempt to make a calculator using OOP and Composition"""

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.suma = Addition(x, y)      #  Instanciamos dentro de otra clase y pasamos atributos
        self.resta = Substraction(x, y)   # Instanciamos dentro de otra clase y pasamos atributos
        
    def power(self):
        value = self.x * self.y
        print(value)

    def division(self):
        value = self.x / self.y
        print(value)


#Usar estas instancias para hacer la calculadora desde diferentes classes
# suma = Addition(7, 7)
# suma.sum()

# resta = Substraction(10, 5)
# resta.subs()

# calculadora = Calculator(10, 5)
# calculadora.power()
# calculadora.division()

#Usamos lo siguiente para usar COMPOSITION en la OOP:

# calculadora = Calculator(10, 5)     # Instanciamos y pasamos valores.
# calculadora.power()
# calculadora.division()

# calculadora.suma.sum()    # accedemos a la instancia de suma e invocamos el método sum()
# calculadora.resta.subs()   
