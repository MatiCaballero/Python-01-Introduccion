#   Realizar un programa que conste de una clase llamada
#   Estudiante, que tenga como atributos el nombre
#   y la nota del alumno. Definir los métodos para
#   inicializar sus atributos, imprimirlos y mostrar
#   un mensaje con el resultado de la nota y si ha
#   aprobado o no.

class Estudiante():
    def __init__(self, nombre, nota):  # inicializamos los atributos
        self.nombre = nombre  # atributo nombre inicializado
        self.nota = nota  # Atributo nota inicializado

    def imprimir(self):
        print("Nombre: {} \nNota: {}".format(self.nombre, self.nota))
    
    def resultados(self):
        if self.nota<7:
            print("Desaprobado")
        else:
            print("Aprobado")

estudiante1 = Estudiante("Daniel" , 10)
estudiante1.imprimir()
estudiante1.resultados()

estudiante2 = Estudiante("Karla" , 3)
estudiante2.imprimir()
estudiante2.resultados()