#Crea un programa que encuentre el número más pequeño de una serie de números introducidos por el usuario.

lista_numeros = list(input("Ingrese una lista: "))

numero_menor = lista_numeros[0]

for numero in lista_numeros:
    if numero < numero_menor:
        numero_menor = numero

print("El numero menor es {}".format(numero_menor))








