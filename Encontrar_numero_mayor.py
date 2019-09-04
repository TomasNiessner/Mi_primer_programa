#Preguntale al usuario una serie de 10 números, y determiná cual es el mas grande.

lista_numeros = []
numero_usuario = ""

while len(lista_numeros) < 10:
    while not numero_usuario.isdigit():
        numero_usuario = input("Ingrese un número: ")
    lista_numeros.append(int(numero_usuario))
    numero_usuario = "" #para un bug
    print("Numero añadido")

numero_mayor = lista_numeros[0]

for numero in lista_numeros:
    if numero > numero_mayor:
        numero_mayor = numero


print("El número mayor es {}".format(numero_mayor))





