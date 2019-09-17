#Crea un programa que al decirle un color, te devuelva su traducción en inglés.

colores = {"amarillo": "yellow", "rojo": "red",
           "azul": "blue", "black": "negro", "marrón": "brown", "violeta": "violet",
           "blanco": "violet", "gris": "gray", "verde": "green", "naranja": "orange"}

color_usuario = input("Ingrese un color el cual quiera traducir (en minúsculas): ")
if color_usuario in colores:
    print(colores[color_usuario])
else:
    print("Introduzca un color: ")



