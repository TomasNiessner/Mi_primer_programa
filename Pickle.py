#Crear la función para borrar contactos.
#En find_contact; Si no encuentra ninguno, que te pregunte si quiere seguir buscando o si quiere ir al menú.
#Que no solo se pueda buscar por nombre, sino por e-mail también. (en el find)

import pickle


from time import sleep

ACTION_ADD_CONTACT = 1
ACTION_REMOVE_CONTACT = 2
ACTION_FIND_CONTACT = 3
ACTION_EXPORT_CONTACT = 4
ACTION_SHOW_CONTACTS = 7
ACTION_EXIT = 5


SAVE_FILE_NAME = "contacts.save"

MENU_OPTIONS = [ACTION_ADD_CONTACT, ACTION_REMOVE_CONTACT, ACTION_FIND_CONTACT, ACTION_EXPORT_CONTACT, ACTION_EXIT, ACTION_SHOW_CONTACTS]


def ask_until_option_expected(options):
    selected_action = ""

    while not selected_action.isdigit() or (selected_action.isdigit() and int(selected_action) not in options):
        selected_action = input("¿Qué opción deseas? ")

    return int(selected_action)


def show_menu():
    print("Acciones disponinbles: ")
    print("1 - Añadir contacto")
    print("2 - Eliminar contacto")
    print("3 - Buscar un contacto")
    print("4 - Exportar contactos a un CSV")
    print("7 - Mostrar los contactos")
    print("5 - Salir")

    return ask_until_option_expected(MENU_OPTIONS)


def add_contact(contacts):
    print("\n\nAñadir contacto\n")
    contact = {
        "name": input("Nombre: "),
        "phone": input("Teléfono: "),
        "email": input("Email: ")
    }
    contacts.append(contact)
    print("Se ha añadido el contacto {} correctamente\n".format(contact["name"]))
    sleep(2)


def remove_contact(contacts):
    print("\n\nBuscar contacto para eliminar")
    search_delete = input("Introduzca el nombre del contacto (o parte de él) que quiere eliminar: ")
    found_contacts_delete = []

    print("Se han encontrado los siguientes contactos:")
    contact_indexes_delete = []
    contact_counter_delete = 0

    for contact in contacts:
        if contact["name"].find(search_delete) >= 0:
            found_contacts_delete.append(contact)
            print("{} - {}".format(contact_counter_delete, contact["name"]))
            contact_indexes_delete.append(contact_counter_delete)
            contact_counter_delete += 1

    contact_index_delete = 0

    if len(contact_indexes_delete) > 1:
        contact_index_delete = ask_until_option_expected(contact_indexes_delete)
    elif len(contact_indexes_delete) == 0:
        print("No se han encontrado contactos con ese nombre: ")

    confirmation = int(input("¿Estás seguro de que quieres eliminar a {}? Presiona 1 para confirmar, o cualquier número para seguir al menú.".format(found_contacts_delete[contact_index_delete]["name"])))
    if confirmation == 1:
        for person in contacts:
            if person["name"] == found_contacts_delete[contact_index_delete]["name"]:
                contacts.pop(contacts.index(contact))
                print("El contacto {} ha sido eliminado con éxito.".format(found_contacts_delete[contact_index_delete]["name"]))
                sleep(2)
    else:
        show_menu()

def find_contact(contacts):
    print("\n\nBuscar contacto\n")
    search_term = input("Introducir el nombre del contacto o parte de él: ")


    found_contacts = [] #Lista que va a contener diccionarios.
    contact_indexes = [] #Lista que va a tener enteros, que son una referencia al indice.
    contact_counter = 0 #La cantidad de contactos que resultaron de la búsqueda.

    for contact in contacts:
        if contact["name"].find(search_term) >= 0 or contact["email"].find(search_term) >= 0:
            found_contacts.append(contact)
            contact_indexes.append(contact_counter)
            contact_counter += 1
            sleep(2)

    contact_index = 0 #no borrar

    if len(contact_indexes) == 1:
        print("He encontrado los siguientes contactos:")
        print("\nInformación sobre {}\n".format(found_contacts[contact_index]["name"]))
        print("Nombre: {name}, Telefono: {phone}, Email: {email}\n\n".format(**found_contacts[contact_index]))
        sleep(2)


    elif len(contact_indexes) > 1:
        contact_index = ask_until_option_expected(contact_indexes)
        print("He encontrado los siguientes contactos:")
        print("\nInformación sobre {}\n".format(found_contacts[contact_index]["name"]))
        print("Nombre: {name}, Telefono: {phone}, Email: {email}\n\n".format(**found_contacts[contact_index]))
        sleep(2)

    elif len(contact_indexes) == 0:
        print("No se han encontrado resultados. Para seguir buscando, ingrese 1, para volver al menú ingrese 0")
        go_or_exit = ask_until_option_expected([1, 0])
        if go_or_exit == 1:
            find_contact(contacts)
        else:
            show_menu()


def show_contacts(contacts):
    for user in contacts:
        print("Nombre: {name}, Telefono: {phone}, Email: {email}\n\n".format(**user))
    sleep(2)

def export_contacts():
    pass


def load_contacts():
    try:
        return pickle.load(open(SAVE_FILE_NAME, "rb"))
    except FileNotFoundError:
        return []


def save_contacts(contacts):
    with open(SAVE_FILE_NAME, "wb") as save_file:
        pickle.dump(contacts, save_file)
    print("Datos guardados correctamente.")


def main():
    contacts = load_contacts()
    action = show_menu()

    while action != ACTION_EXIT:
        if action == ACTION_ADD_CONTACT:
            add_contact(contacts)
        elif action == ACTION_REMOVE_CONTACT:
            remove_contact(contacts)
        elif action == ACTION_FIND_CONTACT:
            find_contact(contacts)
        elif action == ACTION_EXPORT_CONTACT:
            export_contacts()
        elif action == ACTION_SHOW_CONTACTS:
            show_contacts(contacts)



        action = show_menu()

    save_contacts(contacts)
    print("¡Adiós!")


if __name__ == "__main__":
    main()