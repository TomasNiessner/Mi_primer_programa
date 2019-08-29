#Modifica el programa de la tabla de multiplicar para que sólo muestre los resultados cuando son múltiplos de 2.

numero_tabla = int(input("Ingrese un número para obtener su tabla de multiplicación: "))


for numero in range(1,11):
    if (numero_tabla * numero)%2 == 0:
        print("{} * {} = {}".format(numero_tabla, numero, numero_tabla * numero))

#El signo "%" es la operación resto. En la linea 7 dije que si el "numero_tabla" multiplicado por "numero" da resto cero, se haga tal cosa.

