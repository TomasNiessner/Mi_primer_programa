
largo_lista = 0
lista = input("Introduzca una lista de numeros: ")

for numero in lista:
    if numero.isdigit():
        largo_lista +=1

print("La lista tiene {} numeros".format(largo_lista))





