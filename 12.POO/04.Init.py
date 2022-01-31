
class FabricaTelefonos():
    def __init__(self, marca, color):  # Se le pide al usuario una  marca y un color como parametro
        self.marca = marca
        self.color = color
        #print("Estoy ejecutando  init")


telefono = FabricaTelefonos('Huawei', 'Verde')
print(telefono.color)
print(telefono.marca)
