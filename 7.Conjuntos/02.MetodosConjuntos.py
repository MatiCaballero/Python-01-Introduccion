# conjunto = {1, 2, 3, 4, 5, 1, 2, 4, 4, 5}
# lista = [1, 1, 2, 5, 2, 3, 4, 5]

# print("Lista: ", lista)  # La listra muestra datos repetidos
# print("Conjunto: ", conjunto)  # Los conjuntos NO muestran datos repetidos.

# ---------------------------------------------------------------------------------------------

conjunto = {1, 2, 3, 4, 5}
print(conjunto)

# Añadir elemento = .add
conjunto.add(20)
print(conjunto)

#  Elimina un valor = .remove o .discard
conjunto.remove(3)
print(conjunto)

# Elimina un valor al azar = .pop
conjunto.pop()
print(conjunto)

# Añadir elementos = .update
conjunto.update ([6,7,8])
print(conjunto)

# Dejar conjunto vacio = .clear
