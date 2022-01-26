# Definimos el argumento con un * al principio para poder colocar uno mas valores
def argumento(*num):
    for i in num:
        print(i)

print(argumento(10, 1, 23, 45, 6, 7))
