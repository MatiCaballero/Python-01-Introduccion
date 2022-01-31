class FabricaTelefonos ():
    def __init__(self, marca, *colores, **modelos):  # *Colores crea una tupla de colores
        # **modelos = crea un diccionario
        # self = this Se recomienda de todas formas por las buenas practicas utilizar siempre self
        self.marca = marca
        self.colores = colores
        self.modelos = modelos


# El diccionario empieza en s20=256 ej
telefono = FabricaTelefonos("Nokia", "Negro", "Azul", "Rojo", s20=256, s21=256)
print(telefono.marca)
print(telefono.colores)
print(telefono.modelos)

telefono.memoriaRam = 16 #Se crea un atributo temporal. Este atributo se le puede agregar solo al bojeto


print(telefono.memoriaRam)


