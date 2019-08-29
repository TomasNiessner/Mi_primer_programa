#Crea un programa que muestre por pantalla la tabla de multiplicar de un número introducido por el usuario, pero invertida, comenzando desde el 10.

numero_tabla = int(input("Ingrese un número para obtener su tabla de multiplicación: "))
lista = []

for elemento in range(1,11):
    lista.append(elemento)

lista.reverse() #no se si esto queda bien acá pero funciona.

for numero in lista:
    print("{} * {} = {}".format(numero_tabla, numero, numero_tabla * numero))