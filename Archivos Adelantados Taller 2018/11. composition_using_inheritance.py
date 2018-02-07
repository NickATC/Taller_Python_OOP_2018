#composition using OOP.  Continaution of composition.py
# Esta vez, usando la herencia múltiple

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


class Calculator(Addition, Substraction):
    """A first attempt to make a calculator using OOP"""

    def __init__(self, x, y):
        self.x = x
        self.y = y
       
    def power(self):
        value = self.x * self.y
        print(value)

    def division(self):
        value = self.x / self.y
        print(value)

calculadora = Calculator(21, 7)
calculadora.sum()
calculadora.subs()
calculadora.power()
calculadora.division()