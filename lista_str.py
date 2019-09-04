#Dada una lista de strings, devolver una lista con el largo de cada string.

lista_str = ["hola", "bca", "string", "si"]
lista_enunciado = []

for str in lista_str:
    lista_enunciado.append(len(str))

print(lista_enunciado)