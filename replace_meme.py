#Crear un programa que le repita al usuario todo lo que dice pero con todas las vocales cambiadas por i.

str_usuario = input("ingrese una frase: ")

str_replace = ""

vocales = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

for letra in str_usuario:
    if letra in vocales:
        str_replace += letra.replace(letra, "i")
    else:
        str_replace += letra

print(str_replace)