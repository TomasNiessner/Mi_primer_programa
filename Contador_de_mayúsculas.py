#Crea un programa que sea capaz de contar la cantidad de letras mayúsculas en una string introducida por el usuario.

frase_usuario = input("Ingrese una frase: ")

n_mayusculas = 0
espacio = " "

for letra in frase_usuario:
    if letra == letra.upper() and letra != espacio:
        n_mayusculas += 1

print("Hay {} mayúsculas".format(n_mayusculas))

#La linea 9 exceptúa los espacios porque los toma como mayúsculas (por la condición que puse yo).

