#Crea un programa que te diga la fecha de hace 5 días respecto a hoy, y el día de la semana.
import datetime

today = datetime.datetime.now() #Hoy

past_5_days = datetime.timedelta(days=5) #Esto significa 5 días

difference = today - past_5_days

print("Hace 5 días era el día {} del {}".format(difference.weekday(), difference.strftime("%d de %m de %Y")))



