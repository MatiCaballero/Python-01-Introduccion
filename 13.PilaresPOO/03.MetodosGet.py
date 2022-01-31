class A():
    def __init__(self):
        self._cuenta = 0  # Poner _ adelante del atributo es una buena practica. indica que son atributos encapsulados
        self._contador = 0

# - - Creacion de un metodo GET - - #

    # Sirve para llamar el metodo como si fuese el atributo. Sin los parentesis.
    @property
    def cuenta(self):
        return self._cuenta

    @property
    def contador(self):
        return self._contador

a = A()
print(a.cuenta)  # Forma correcta a traves de un metodo
print(a.contador)