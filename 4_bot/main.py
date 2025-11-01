from handlers import (
    add_contact,
    change_contact,
    show_phone,
    show_all,
    delete_contact,
    show_help,
)
from colorama import Fore, Back


def print_separator(char="-", length=40, color=Fore.LIGHTBLUE_EX):
    print(color + char * length + Fore.RESET)
    print("")


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def main():
    contacts = {}

    print("Welcome to the assistant bot!")
    print(f"{Fore.BLUE}To get help, type 'Help'.{Fore.RESET}")
    while True:
        print_separator()
        user_input = input(f"{Back.LIGHTBLACK_EX}Enter a command:{Back.RESET} ")
        print("")

        command, args = parse_input(user_input)
        # print(args)
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "help":
            show_help()
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "delete":
            print(delete_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
