
frase_usuario = input("Escriba una frase")

espacios = [" "]
puntos = ["."]
comas = [","]

n_espacios = 0
n_puntos = 0
n_comas = 0

for signo in frase_usuario:
    if signo in espacios:
       n_espacios +=1
    elif signo in puntos:
        n_puntos +=1
    elif signo in comas:
        n_comas +=1

print("La frase tiene {} espacios, {} puntos, y {} comas".format(n_espacios, n_puntos, n_comas))