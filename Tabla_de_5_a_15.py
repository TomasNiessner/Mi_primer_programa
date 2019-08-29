#Modifica el programa de la tabla de multiplicar para que vaya del 5 al 15 en lugar del 1 al 10.

numero_tabla = int(input("Ingrese un número para obtener su tabla de multiplicación: "))

for numero in range(5,16):
    print("{} * {} = {}".format(numero_tabla, numero, numero_tabla * numero))

    