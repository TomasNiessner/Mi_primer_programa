#Obtener la tabla de multiplicación de un número dado por el usuario.

numero_tabla = int(input("Ingrese un número para obtener su tabla de multiplicación: "))

for numero in range(1,11):
    print("{} * {} = {}".format(numero_tabla, numero, numero_tabla * numero))


