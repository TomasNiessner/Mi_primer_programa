#Escribe una función que encuentre el numero más grande entre 3 numeros.

def numero_maximo(primero, segundo, tercero):
    numero_mayor = 0
    lista_numeros = [primero, segundo, tercero]
    for numero in lista_numeros:
        if numero > numero_mayor:
            numero_mayor = numero

    return numero_mayor

print("El numero máximo es {}".format(numero_maximo(25, 20, 392)))