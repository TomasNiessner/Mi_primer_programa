numero_elegido = int(input("Ingrese el numero del cual quiere la tabla: "))

for multiplo in reversed(range(1, 11)):
    print("{} x {} = {}".format(numero_elegido, multiplo, numero_elegido * multiplo))

