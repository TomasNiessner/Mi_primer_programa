#Escribe una frase aleatoria de una lista de strings cada 3 segundos.

import random
from time import sleep

str_list = ["dinero", "es", "tiempo", "el", "aprende", "algo", "ey"]


loop = True
while loop == True:
    print(str_list[random.randint(0, 6)])
    sleep(3)

