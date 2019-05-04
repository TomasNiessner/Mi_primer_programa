frase_usuario = input("Ingrese una frase")

n_mayusculas = 0

for letra in frase_usuario:
    if (letra.isupper()) == True:
        n_mayusculas +=1

print("Hay {} mayusculas".format(n_mayusculas))


