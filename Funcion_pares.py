#Escribe una función que reciba una lista de números y devuelva otra pero conteniendo solo los números pares.

def pares(lista):
    lista_pares = []
    for numero in lista:
        if numero % 2 == 0:
            lista_pares.append(numero)
    return lista_pares

print(pares([1, 2, 34, 5, 36, 73, 20]))

