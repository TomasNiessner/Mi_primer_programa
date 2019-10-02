#Escribe un programa que imprima por pantalla una frase aleatoria cada segundo.
# La lista de frases de la que se seleccionará la frase aleatoria será distinta según el segundo en el que estemos:
#– Segundos acabados en ‘0’: frases alegres
#– Segundos acabados en ‘1’: nombres de muebles (silla, mesa)
#– Segundos acabados en ‘2’: nombres de bebidas
#– Segundos acabados en ‘3’: frases de odio
#– Segundos acabados en ‘4’: nombres de comidas
#– Segundos acabados en ‘5’: frases absurdas
#- Segundos acabados en ‘6’: nombres de animales
#– Segundos acabados en ‘7’: frases motivacionales
#– Segundos acabados en ‘8’: sonidos de animales
#– Segundos acabados en ‘9’: frases tristes

from time import sleep
import random

frases_alegres = ["Qué lindo día", "La vida es bella", "Que bello es vivir"]
nombres_muebles = ["Mesa", "Escritorio", "Cama"]
nombres_bebidas = ["Agua", "Pepsi", "Vino"]
frases_odio = ["Te odio", "Espero que mueras", "No te soporto"]
nombres_comidas = ["Milanesas", "Pizza", "Tarta"]
frases_absurdas = ["No hay mal que por bien no venga", "Lo peor ya pasó", "Estamos a mitad del río"]
nombres_animales = ["Calamar", "oso", "Gato"]
frases_motivacionales = ["Todavía hay tiempo", "Siempre que llovió paró", "Nada es imposible"]
sonidos_animales = ["Uau", "Miau", "Muu"]
frases_tristes = ["No va a volver", "Se descongeló el precio de la nafta", "Me siento solo"]



time_passed = 0
infinit_loop = True

def sentences(sentence, number):
    if time_passed % 10 == number:
        print(sentence[random.randint(0, 2)])

while infinit_loop == True:
    sentences(frases_alegres, 0)
    sleep(1)
    time_passed += 1
    sentences(nombres_muebles, 1)
    sentences(nombres_bebidas, 2)
    sentences(frases_odio, 3)
    sentences(nombres_comidas, 4)
    sentences(frases_absurdas, 5)
    sentences(nombres_animales, 6)
    sentences(frases_motivacionales, 7)
    sentences(sonidos_animales, 8)
    sentences(frases_tristes, 9)



