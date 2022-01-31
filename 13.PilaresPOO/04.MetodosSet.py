class A():
    def __init__(self):
        self._cuenta = 0  # Poner _ adelante del atributo es una buena practica. indica que son atributos encapsulados
        self._contador = 0

# - - Creacion de los metodos GET - - #

    # Sirve para llamar el metodo como si fuese el atributo. Sin los parentesis.
    @property
    def cuenta(self):
        return self._cuenta

 # - - Creacion de un metodo SET - - #   
    @cuenta.setter
    def cuenta(self, cuenta):
        self._cuenta = cuenta

    @property
    def contador(self):
        return self._contador
    
    @contador.setter
    def contador(self,contador):
        self._contador = contador

a = A()
print(a.cuenta)  # Forma correcta a traves de un metodo
a.cuenta = 20  #Forma correcta  de cambiar un numero
print (a.cuenta)
print(a.contador)
a.contador = 10
print(a.contador)