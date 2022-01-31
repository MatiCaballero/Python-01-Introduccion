
class A():
    def __init__(self):
        self.contador = 0

    def incrementar(self):
        self.contador += 1

    def cuenta(self):
        return self.contador


class B():
    #Al utilizar doble guion bajo (__) es un atributo que no puede se accedido por fuera de la clase
    def __init__(self):
        self.__contador = 0

    def incrementar(self):
        self.__contador +=1

    def cuenta(self):
        return self.__contador


print("- . OBJETO 1 - -")
a = A()
print(a.cuenta())
a.incrementar()
print(a.cuenta())
print(a.contador) #Es incorrecto.

print(" - - OBJETO 2 - -")
b = B()
print(b.cuenta())
b.incrementar()
print(b.cuenta())
print(b.__contador) #Mala practica, es incorreto.
