#Crea un programa que sea un juego, donde el programa te diga:
#La fecha en que vas a morir, cuantos años faltan para esa fecha, cuantos días faltan para esa fecha, la edad que vas a tener esa fecha
#Crea parametros que reduzcan la esperanza de vida del individuo.

import datetime
import random


AVERAGE_LIFEARG = 80
real_average_life = random.randint(40, AVERAGE_LIFEARG)

print("¡Averigua cuanto te queda de vida!")
print("Completa la siguiente encuesta:")

date_birth = (input("Ingrese su fecha de nacimiento [en formato(dd/mm/yyyy)]: "))
date_birth = datetime.datetime.strptime(date_birth, "%d/%m/%Y")


DRUGS_PENALTY = 5
EMOTIONAL_PENALTY = 4
TRANSIT_PENALTY = 7
VOLENT_PENALTY = 3

years_lost = 0

def ask_everything(message):
    response = ""
    while response != "S" and response != "N" and response != "O":
        response = input(message + "[S/N/O(ocasionalmente)]")
        return response

drugs = ask_everything("¿Consume usted alguna droga?: ")
emotion = ask_everything("¿Es usted feliz?: ")
transit = ask_everything("¿Cruza la calle de forma responsable?: ")
violence = ask_everything("¿Es usted una persona violenta?: ")

if drugs == "S":
    years_lost += DRUGS_PENALTY
elif drugs == "O":
    years_lost += DRUGS_PENALTY / 2
elif emotion == "N":
    years_lost += EMOTIONAL_PENALTY
elif emotion == "O":
    years_lost += EMOTIONAL_PENALTY / 2
elif transit == "N":
    years_lost += TRANSIT_PENALTY
elif transit == "O":
    years_lost += TRANSIT_PENALTY / 2
elif violence == "S":
    years_lost += VOLENT_PENALTY
elif violence == "O":
    years_lost += VOLENT_PENALTY / 2


life_time = real_average_life - years_lost
death_day = date_birth + datetime.timedelta(days=life_time * 365)
days_to_death = death_day - datetime.datetime.now()

print("La fecha de tu muerte es {}, y le quedan {} días de vida".format(death_day.strftime("%d/%m/%Y"), days_to_death.days))