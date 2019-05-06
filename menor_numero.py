
numeros_introducidos= []
numeros_usuario = ""

while len(numeros_introducidos) < 6:
    while not numeros_usuario.isdigit():
        numeros_usuario = input("Diga un numero: ")
    numeros_introducidos.append(int(numeros_usuario))
    numeros_usuario = ""
    print("numero agregado")

numero_chico = numeros_introducidos[0]

for numero in numeros_introducidos:
    if numero < numero_chico:
        numero_chico = numero

print("El numero mas chico es {}".format(numero_chico))






