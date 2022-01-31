class FabricaTelefonos():
    marca = "Samsung"

    # self = Nos permite englobar atributos a todas las clases y a todo el programa general
    def ElaborarHuawei(self):
        self.marca = "Huawei" # self. se engloba en toda la clase
        
telefono = FabricaTelefonos()
telefono.ElaborarHuawei()
print(telefono.marca)