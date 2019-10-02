#Antes de comenzar el while principal, preguntar al usuario si desea configurar una alarma,
# esta alarma sonara una vez al día a la hora que el usuario decida (no hace falta tener los minutos en cuenta).
# También el usuario podrá decidir que días de la semana quiere que esta alarma suene o si quiere que suene una fecha en concreto.
# Cuando llegue el momento especificado en la alarma, simplemente escribir una nueva linea de texto en el archivo y en pantalla.
# Esto representaría que la alarma ha sonado.

from time import sleep
import datetime

NIGHT_STARTS = 19
DAY_STARTS = 8
HOUR_DURATION = 1


def write_file_and_screen(text, file_name):
    with open(file_name, "a") as hours_file:
        hours_file.write("{}{}".format(text, "\n"))
        print(text)



def main():
    current_time = datetime.datetime.now()
    is_night = False
    alarm_confirmation = input("¿Quiere configurar una alarma? Si[S]/No[N]: ")

    if alarm_confirmation == "S":
        type_alarm = input("Si desea configurar la alarma para una fecha exacta pulse[E], si quiere que suene algunos días, presione[D]: ")

        if type_alarm == "E": #Alarma para fecha exacta
            e_date_hour = int(input("Ingrese la hora: "))
            e_date_month = int(input("Ingrese número del mes: "))
            e_date_day = int(input("Ingrese el número del día: "))
            e_alarm_date = datetime.datetime(year=2019, month=e_date_month, day=e_date_day, hour=e_date_hour)

        elif type_alarm == "D": #Alarma para días de semana
            weekdays = {1: "Lunes", 2: "Martes", 3: "Miercoles", 4: "Jueves", 5: "Viernes", 6: "Sábado", 7: "Domingo"}
            d_date_day = 8
            d_date_day_list = []

            d_date_hour = int(input("Ingrese la hora que quiere que suene la alarma: "))
            while d_date_day != 0:
                d_date_day = int(input("Agregue un día que quiere que suene la alarma (En números, ej:  Lunes=1. Ingrese 0 para finalizar) "))
                if d_date_day != 0:
                    d_date_day_list.append(d_date_day)
            for numero in d_date_day_list:
                print("La alarma va a sonar el día {}".format(weekdays[numero]))


    while True:
        sleep(HOUR_DURATION)
        current_time += datetime.timedelta(hours=1)
        light_changed = False

        if (current_time.hour >= NIGHT_STARTS or current_time.hour <= DAY_STARTS) and not is_night:
            is_night = True
            light_changed = True

        elif (current_time.hour > DAY_STARTS and current_time.hour < NIGHT_STARTS) and is_night:
            is_night = False
            light_changed = True

        if light_changed:
            if is_night:
                write_file_and_screen("Se ha hecho de noche", "horas.txt")
            else:
                write_file_and_screen("Se ha hecho de día", "horas.txt")

        write_file_and_screen("La hora actual es {}".format(current_time), "horas.txt")

        if type_alarm == "E":
            if (current_time.hour == e_alarm_date.hour) and (current_time.day == e_alarm_date.day) and (current_time.month == e_alarm_date.month):

                write_file_and_screen("¡RING!", "horas.txt")
        if type_alarm == "D":
            if current_time.isoweekday() in d_date_day_list:
                if current_time.hour == d_date_hour:
                    write_file_and_screen("¡RING!", "horas.txt")




if __name__ == "__main__":
    main()