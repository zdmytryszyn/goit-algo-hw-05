from collections.abc import Iterator
from typing import Callable


def parse_input(user_input: str):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def input_error(func: Callable) -> Callable:
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "There is no such contact. Add contact"
        except ValueError:
            return "Enter the argument for the command."
        except IndexError:
            return "Name of contact wasn't given in the argument.\
            Input the name of the contact"
    return inner


@input_error
def add_contact(args: list, contacts: dict) -> str:
    username, phone = args
    if username not in contacts:
        contacts[username] = phone
        return "Contact added."
    return "Contact already exists"


@input_error
def change_contact(args: list, contacts: dict) -> str:
    username, phone = args
    if username in contacts:
        contacts[username] = phone
        return "Contact updated."
    return "Name is not in contacts. Add new contact"


@input_error
def show_phone(args: str, contacts: dict) -> str:
    username = args[0]
    return contacts[username]


def show_all(contacts: dict) -> Iterator:
    return (f"{key} {value}" for key, value in contacts.items())


def main() -> None:
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            for contact in show_all(contacts):
                print(contact)
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
