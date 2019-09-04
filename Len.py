#Crea un programa que cuente los elementos de la lista de números introducida por el usuario. Está prohibido utilizar la función len() para resolver el problema.

lista= list(input("Ingrese una lista: "))
elementos = 0

for elemento in lista:
    if elemento.isdigit():
        elementos += 1

print("La lista tiene {} elementos ".format(elementos))

