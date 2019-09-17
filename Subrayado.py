#Crea una función que muestre por pantalla un texto y tantas barritas de subrayado como larga
#sea la string.



def subrayar_frase(frase):
    cantidad_caracteres = 0
    subrayado = ""

    for letra in frase:
        subrayado += "-"
    print(frase)
    print(subrayado)

subrayar_frase("hola mundo")