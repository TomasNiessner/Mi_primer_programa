#Escribe una funcion que dado un numero y un rango (otros dos numeros),
# compruebe que ese numero está entre los dos (dentro del rango).

def numero_intermedio(minimo, intermedio, maximo):
    if (minimo < intermedio < maximo):
        return True
    else:
        return False

print(numero_intermedio(1, 19, 100))
print(numero_intermedio(10, 40, 20))
