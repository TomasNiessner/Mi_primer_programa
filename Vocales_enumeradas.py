#Crear un programa que cambia las vocales por su numero de aparición. Por ejemplo la string “aurora boreal” se convertiría en “12r3r4 b5r67l”

str_usuario = input("Ingrese una frase: ")

numero = 0

str_replace = " "

vocales = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

for letra in str_usuario:
    if letra in vocales:
        numero += 1
        str_replace += letra.replace(letra, str(numero))
    else:
        str_replace += letra

print(str_replace)