diccionario = {1: 2, 2: 3, 3: 4}
diccionario2 = {4:500 , 6:20}
print(diccionario)

# .setdefault = recibe el valor de la llave y su valor

diccionario.setdefault(4, 5)
print(diccionario)

# .upadte = Sirve para juntar dos diccionarios.
diccionario.update(diccionario2)
print(diccionario)

#.copy = Sirve para crear una copia del diccionario
diccionario.copy()
print(diccionario)

# .pop = En el deccionario, elimina una llave deseada
diccionario.pop(3)
print(diccionario)

# .get = Muestra el valor de una clave determianda.
print(diccionario.get(2))

# .clear = Borra todos los elementos del diccionario
diccionario.clear()
print(diccionario)
