from colorama import Fore
from error_handlers import input_error


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    name, new_phone = args
    prev_phone = contacts[name]
    contacts[name] = new_phone
    return f"Contact updated from {prev_phone} on {new_phone}."


@input_error
def show_phone(args, contacts):
    name = args[0]
    return f"{contacts[name]}"


@input_error
def show_all(contacts):
    if not contacts:
        return "No contacts found."

    print("Contacts list:")
    contact_multirow_list = "\n".join(
        f"{key}: {value}" for key, value in contacts.items()
    )
    return contact_multirow_list


@input_error
def delete_contact(args, contacts):
    name = args[0]
    del contacts[name]
    return "Contact deleted."


@input_error
def show_help():
    print("The list of commands:")
    print(f"{Fore.YELLOW}'Hello'{Fore.RESET} - greet the bot")
    print(f"{Fore.YELLOW}'Add <name> <phone>'{Fore.RESET} - add a contact")
    print(
        f"{Fore.YELLOW}'Сhange <name> <new_phone>'{Fore.RESET} - change a contact's phone number"
    )
    print(f"{Fore.YELLOW}'Phone <name>'{Fore.RESET} - show contact's phone number")
    print(f"{Fore.YELLOW}'All'{Fore.RESET} - show all contacts")
    print(f"{Fore.YELLOW}'Help'{Fore.RESET} - show this help message")
    print(f"{Fore.YELLOW}'Close' or 'Exit'{Fore.RESET} - exit the program")
