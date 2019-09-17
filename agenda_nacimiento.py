#Crea un programa que guarde los nombres de las personas y sus fecha de nacimiento.
agenda = dict()
salida = False

while not salida:
    accion = input("¿Qué quiere hacer?: Añadir persona [A] / Consultar fecha de nacimiento [B] / Salir [C]: ")

    #Acción añadir
    if accion == "A":
        print("Se va a añadir una nueva persona a la agenda: ")
        print("------------------------------------------------")
        nombre = input("Ingrese su nombre: ")
        fecha = input("Ingrese su fecha de nacimiento: ")
        agenda[nombre] = fecha

    #Acción consultar
    elif accion == "B":
        print("Consultar fecha de nacimiento")
        print("------------------------------")
        nombre = input("¿De quién quiere saber su fecha de nacimiento?: ")
        print("La fecha de nacimiento es: {}" .format(agenda[nombre]))

    elif accion == "C":
        salida = True

    else:
        print("Por favor introduzca una acción válida")




