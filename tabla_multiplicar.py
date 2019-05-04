numero_elegido = int(input("Elija el numero del cual quiere la tabla: "))


for multiplo in range(1, 11):
    if multiplo%2 == 0:
        print("{} x {} = {}".format(numero_elegido, multiplo, numero_elegido * multiplo))

        




