#Este es un programa para saber cuanto vale "i" cuando tiene un exponente muy grande


valor_exponente = int(input("Ingrese el valor del exponente de i: "))
valor_i = ""

if valor_exponente % 4 == 0:
    valor_i = 1
elif valor_exponente % 4 == 1:
    valor_i = "i"
elif valor_exponente % 4 == 2:
    valor_i = -1
elif valor_exponente % 4 == 3:
    valor_i = "-i"

print("El valor de i es {}".format(valor_i))


