#Crea un programa que sea capaz de contar espacios, puntos y comas en una string introducida por el usuario.

frase_usuario = input("Ingrese una frase: ")

puntos = ["."]
comas = [","]
espacios = [" "]

n_puntos = 0
n_comas = 0
n_espacios = 0

for letra in frase_usuario:
    if letra in puntos:
        n_puntos += 1
    elif letra in comas:
        n_comas +=1
    elif letra in espacios:
        n_espacios +=1

print("Hay {} puntos".format(n_puntos))
print("Hay {} comas".format(n_comas))
print("Hay {} espacios".format(n_espacios))

