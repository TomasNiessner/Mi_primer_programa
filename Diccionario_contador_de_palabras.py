#Crea un programa que cuente el número de veces que aparece una palabra en una string

str = "dinero dinero , el tiempo es dinero y el dinero es tiempo"

diccionario_str = dict()

def contador_dict(palabra):

    diccionario_funcion = dict()

    for cosa in str.split():

        if cosa in diccionario_funcion:
            diccionario_funcion[cosa] += 1
        else:
            diccionario_funcion[cosa] = 1

    return diccionario_funcion[palabra]

def print_todos(word_l):
    return print("La palabra {} aparece {} veces".format(word_l, contador_dict(word_l)))

print_todos("dinero")
print_todos((","))
print_todos("tiempo")
print_todos("el")
print_todos("es")



