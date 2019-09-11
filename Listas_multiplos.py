#Crear un programa que guarde e imprima varias listas con todos los números que estén dentro de una lista proporcionada por el usuario y sean múltiplos de 2, de 3, de 5 y de 7.

lista_usuario = []

input_usuario = input("Ingrese una serie de numeros separados por un espacio: ")

lista_usuario = [int(i) for i in input_usuario.split()] #Esto es nuevo, no se explicó en el curso pero lo saqué de un foro.


multiplos_dos = []

multiplos_tres = []

multiplos_cinco = []

multiplos_siete = []

for numero in lista_usuario:

    if numero % 2 == 0:
        multiplos_dos.append(numero)
    if numero % 3 == 0:
        multiplos_tres.append(numero)
    if numero % 5 == 0:
        multiplos_cinco.append(numero)
    if numero % 7 == 0:
        multiplos_siete.append(numero)

print("Los múltiplos de dos son:{} ".format(multiplos_dos))
print("Los múltiplos de tres son:{} ".format(multiplos_tres))
print("Los múltiplos de cinco son: {}".format(multiplos_cinco))
print("Los múltiplos de siete son:{} ".format(multiplos_siete))
