#   Crear una clase Fabrica que tenga los atributos de Llantas,
#   Color y Precio; luego crear dos clases mas que hereden de Fabrica,
#   las cuales son Moto y Carro. Crear metodos que muestren la cantidad
#   de llantas, color y precio de ambos transportes. Por ultimo,
#   crear objetos para cada clase y mostrar por pantalla los atributos
#   de cada uno

class Fabrica():
    def __init__(self, llantas, color, precio):
        self.llantas = llantas
        self.color = color
        self.precio = precio


class Auto(Fabrica):
    def datos(self):
        print("La cantidad de llantas  es de: ", self.llantas)
        print("El color del auto es: u$d  ", self.color)
        print("El precio del auto es: ", self.precio)


class Moto(Fabrica):
    def datos(self):
        print("La cantidad de llantas es de: ", self.llantas)
        print("El color de la moto es: u$d ", self.color)
        print("El precio de la moto: ", self.precio)


moto = Moto(2, "Negro", 4000)
moto.datos()

auto = Auto(4, "Blanco", 6000)
auto.datos()
