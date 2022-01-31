
class Animales():
    def habla(self):
        print("Yo soy un Animal")
    def descripcion(self):
        print("Yo soy un {}" .format(self.animal))

class Perro(Animales): #al poner entre el parentesis (animales), heredamos todos los metodos de la clase animales
    pass

class Abeja (Animales):
    def __init__ (self,animal):
        self.animal = animal

animal = Animales()
animal.habla()


perro = Perro()
perro.habla()

abeja = Abeja("Abeja")
abeja.descripcion()



