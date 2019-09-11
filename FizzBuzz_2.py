
# Realizar el FizzBuzz con las mismas reglas pero en el caso que el numero sea divisible entre 3 y 5, cambiar el texto por “Bazinga”

numeros = [1, 2, 5, 15, 6, 7, 8, 23, 56, 75, 12, 30, 25]


for indice in range(len(numeros)):
    numero = numeros[indice]

    if numero % 3 == 0 and numero % 5 ==0:
        numeros[indice] = "Bazinga"

    elif numero % 3 == 0:
        numeros[indice] = "Fizz"

    elif numero % 5 == 0:
        numeros[indice] = "Buzz"


print(numeros)