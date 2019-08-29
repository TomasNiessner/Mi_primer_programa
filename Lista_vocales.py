#Crea un programa que muestre por pantalla una lista de todas las vocales que aparecen en una string introducida por el usuario.

frase_usuario = input("Ingrese una frase: ")

vocales = ["a", "e", "i", "o", "u"]
l_vocales = []

for letra in frase_usuario:
    if letra in vocales:
        l_vocales.append(letra)

print("vocales: {}".format(l_vocales))

