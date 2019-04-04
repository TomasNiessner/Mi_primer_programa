


number_to_guess = 14

user_number = int(input("Adivina un numero: "))

if number_to_guess == user_number:
    print("Has ganado")

else:
    user_number = int(input("Adivina otra vez: "))
    if number_to_guess == user_number:
        print("has ganado")
    else:
        user_number = int(input("Adivina otra vez: "))
        if number_to_guess == user_number:
            print("has ganado")
        else:
            user_number = int(input("Adivina otra vez: "))
            if number_to_guess == user_number:
                print("has ganado")
            else:
                user_number = int(input("Adivina otra vez: "))
                if number_to_guess == user_number:
                    print("has ganado")
                else:
                    print("Has perdido")









