#Crea un programa que pregunte al usuario que adivine un numero del 1 al 10, pero ese numero se va a generar aleatoriamente.
# Hacer esperar al usuario 3 segundos antes de dar la respuesta.

from time import sleep
import random



list_numbers = [1, 2, 3, 4, 5, 6 ,7, 8, 9, 10]
random_number = random.randint(1, 10)
user_number = int(30)

while user_number > int(10) or user_number < int(1):
    user_number = int(input("Enter a number from 1 to 10: "))

if user_number == random_number:
    sleep(3)
    print("¡You win!")
else:
    sleep(3)
    print("¡You failed!, the number was {}".format(random_number))









