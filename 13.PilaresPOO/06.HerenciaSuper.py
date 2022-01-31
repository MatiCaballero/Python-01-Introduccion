class Animales():
    def __init__(self, nombre):
        self.nombre = nombre
class Perro (Animales):
    def __init__(self, nombre, sonido):
        super().__init__(nombre) #Super = Heredamos el init de la clase anterior
        self.sonido = sonido

perro = Perro ("Firulais","Guaaaou")
print(perro.nombre)
print(perro.sonido)