from email.errors import MalformedHeaderDefect
from ssl import VERIFY_DEFAULT


class FabricaTelefonos():
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
        print("El objeto {} ha sido creado".format(self.marca))

    def __str__(self):
        return "El bojeto es {}".format(self.marca)

    def __del__(self):
        print("El objeto {} ha sido destruido".format(self.marca))


telefono = FabricaTelefonos("Samsung", "Negro")
print(telefono.marca)
print(telefono)
