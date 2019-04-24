
primer_numero = float(input("Elija el primer numero"))

segundo_numero = float(input("Elija el segundo numero"))

operacion_elegida = input("¿Que operacion se va a realizar? (suma / resta / division / multiplicacion)")

if operacion_elegida == "suma":
    resultado_operacion = primer_numero + segundo_numero
    print(resultado_operacion)

elif operacion_elegida == "resta":
    resultado_operacion = primer_numero - segundo_numero
    print(resultado_operacion)

elif operacion_elegida == "division":
    resultado_operacion = primer_numero / segundo_numero
    print(resultado_operacion)

elif operacion_elegida == "multiplicacion":
    resultado_operacion = primer_numero * segundo_numero
    print(resultado_operacion)




