diccionario = {'Nombre': "Matias", 'Apellido': "Arias" , 'Edad' : 26}

print (diccionario)

#.keys = Muestra solamente las llaves del diccionario
print(diccionario.keys())

#.values = Muestra valores del diccionario
print(diccionario.values())

#Muestra solo una llave en especifico
print(diccionario["Edad"])

#Agrego una llave y un valor al diccionario
diccionario["Peso"] = "80 kg"
print(diccionario)

#Modifico un valor  de una llave
diccionario["Nombre"] = "Arturito"
print(diccionario)

