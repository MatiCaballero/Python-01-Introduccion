def valores():
    global num1 #Inicializamos la viarable adentro y fuera de la funcion
    global num2
    num1 = 110
    num2 = 40
    resultado = num1 + num2
    return resultado

print (valores())

resta = num1 - num2
print (resta)