while True:
    try:
        edad=int(input("Ingrese tu edad: "))
        print ("Tu edad es: ",edad)
        break
    except ValueError:
        print ("Has colocado un  valor erroeno.")

while True:
    try:
        edad=int(input("Ingrese tu edad: "))
        print ("Tu edad es: ",edad)
        break
    except KeyboardInterrupt:
        print ("Has cancelado la ejecucion")