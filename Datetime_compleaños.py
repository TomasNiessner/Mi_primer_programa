#Crea un programa que te diga cuando falta para tu cumpleaños y que día de la semana será.
import datetime

birthday = datetime.date(year=2020, month=1, day=14) #mi cumpleaños

today = datetime.date.today() #hoy

remaning_days = birthday - today #días faltantes


print("Para mi cumpleaños faltan {} días y cae el día {} ".format(remaning_days.days, birthday.weekday()))



