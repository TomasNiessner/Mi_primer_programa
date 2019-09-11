#Crear un programa que encuentre el numero más grande de una lista (sin usar la función max).

#La lista la defino yo, porque no aclara.

lista = [1, 2, 5, 15, 6, 7, 8, 23, 56, 75, 12, 30, 25]

numero_mayor = 0

for numero in lista:
    if numero > numero_mayor:
        numero_mayor = numero

print(numero_mayor)