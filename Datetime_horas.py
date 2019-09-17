#Crea un programa que te diga, introduciendo cualquier fecha, cuantas horas han pasado desde ese momento.
import datetime

day = int(input("Ingrese un día: "))
month = int(input("Ingrese un mes: "))
year = int(input("Ingrese un año: "))

user_date = datetime.datetime(year=year, month=month, day=day)

righ_now = datetime.datetime.now()

difference = righ_now - user_date


print("Pasaron {} horas desde ese día".format(difference.days * 24))
