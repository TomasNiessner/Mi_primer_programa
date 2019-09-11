#Crear un programa que cambie todas las ‘A’ o ‘a’ por la string ‘VACA’ de una string introducida por el usuario.

str_usuario = (input("Ingrese una frase: "))


str_replace = str_usuario.replace("A", "a")

str_replace_new = str_replace.replace("a", "VACA")


print(str_replace_new)
