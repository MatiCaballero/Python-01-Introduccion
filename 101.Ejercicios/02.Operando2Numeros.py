#   Realizar un programa en el cual se declaren dos valores
#   enteros por teclado utilizando el motodo __init__.
#   Calcular despues la suma, resta, multiplicacion y division
#   Utilizar un metodo para cada una e imprimir los resultados obtenidos.
#   Llamar a la clase Calculadora

class Calculadora():
    def __init__(self):
        self.n1 = int(input("Ingrese el primer numero: "))
        self.n2 = int(input("Ingrese el segundo valor: "))

    def suma(self):
        self.suma = self.n1 + self.n2
        print("La suma de como resultado: ", self.suma)

    def resta(self):
        self.resta = self.n1 - self.n2
        print("La resta da como resultado: ", self.resta)

    def multi(self):
        self.multi = self.n1 * self.n2
        print("La multiplicacion da como resultado: ", self.multi)

    def div(self):
        self.div = self.n1 / self.n2
        print("La division da como resultado: ", self.div)


calcular = Calculadora()
calcular.suma()
calcular.resta()
calcular.multi()
calcular.div()
