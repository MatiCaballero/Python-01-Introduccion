# Creamos una clase 'FabricaTelefonos'
class FabricaTelefonos():

    # Colocamos los atributos
    marca = "Samsung"
    color = "Negro"
    memoriaRam = 32
    almacenamiento = 256

# creamos un metodo
    def llamar(self, mensaje):
        return mensaje

    def escucharMusica(self):
        print("Estas escuchando Musica")

# Creamos el objeto
telefono = FabricaTelefonos()

# Agregamos los atributos la telefono
telefono.marca
telefono.color
telefono.memoriaRam
telefono.almacenamiento

print(telefono.almacenamiento)

#Utilizamos el metodo a travez del objeto
print(telefono.llamar("Hola, buen dia."))
telefono.escucharMusica()