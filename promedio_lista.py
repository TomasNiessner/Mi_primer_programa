numero = ""
lista = []

while numero != 0:
    numero = int(input("Ingrese un numero (ingrese 0 para finalizar la lista): "))
    if numero != 0:
        lista.append(numero)
    print("Ahora la lista es {}".format(lista))

promedio = sum(lista) / len(lista)

print("El promedio de la lista es {}".format(promedio))







