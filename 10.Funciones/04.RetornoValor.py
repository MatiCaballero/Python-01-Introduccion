# sintaxis: def <nombre de la funcion>():
#           <sentencia>
#           return

def entero():
    print('Este es un dato entero:')
    return 10

entero()  # No devuelve el valor
print(entero())  # Devuelve el valor


def decimal():
    print("Este es un dato decimal:")
    return 88.88

print(decimal())


def frase():
    return "No hay mal, que por bien no venga."

print(frase())


def asignacion():
    return 1, 2, 3, 4, 5

print(asignacion())

a, b, c, d, e = asignacion()  # Le asigno un valor de la funcion  a cada letra

print(a, b, c)
