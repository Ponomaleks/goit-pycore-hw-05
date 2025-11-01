from colorama import Fore


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return f"{Fore.RED}Give me name and phone please.{Fore.RESET}"
        except IndexError:
            return f"{Fore.RED}Enter user name{Fore.RESET}"
        except KeyError:
            return f"{Fore.RED}Contact not found.{Fore.RESET}"

    return inner
