class A():
    def __init__(self):
        self.cuenta = 0  # Encapsular el atributo con un _

    def incrementar(self):
        self._contador += 1

    def cuenta(self):
        return self._contador


a = A()
#print(a.cuenta)  # Este modo es incorrecto, se hace a traves de un get
#a.cuenta = 20 # Incorrecto, para cambiar el valor se utiliza un set
#print(a.cuenta)

