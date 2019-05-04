frase_usuario = input("Ingrese una frase")

vocales = ["a", "e", "i", "o", "u"]
vocales_usadas = []
for letra in frase_usuario:
    if letra in vocales:
        vocales_usadas.append(letra)


print("{}".format(vocales_usadas))
