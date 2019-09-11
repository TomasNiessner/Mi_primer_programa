#Dada una lista de enteros:
#Vamos a sustituir los múltiplos de 3 por un "Fizz"
#Vamos a sustituir los múltiplos de 5 por un "Buzz"
#Vamos a sustituir los múltiplos de ambos por un "FizzBuzz"


numeros = [1, 2, 5, 6, 7, 8, 23, 56, 75, 12, 30, 25]

for indice in range(len(numeros)):
    numero = numeros[indice]

    if numero % 3 == 0 or numero % 5 == 0:
        numeros[indice] = ""

        if numero % 3 == 0:
            numeros[indice] += "Fizz"

        if numero % 5 == 0:
            numeros[indice] += "Buzz"

print(numeros)

