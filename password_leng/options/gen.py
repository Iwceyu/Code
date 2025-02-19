import string
from pyperclip import copy as cp
from random import choice
from os import name, system, environ as en

def clean_console():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")

def letter_gen(digits: int = 8) -> str:
    letters = string.ascii_letters
    password: str = ""

    for l in range(1, digits + 1):
        password += choice(letters)

    return password

def letter_num_gen(digits: int = 8) -> str:
    num_lett: str = string.digits + string.ascii_letters
    password: str = ""

    for d in range(1, digits + 1):
        password += choice(num_lett)

    return password


def letter_num_punc(digits: int = 8):
    lett_num_punc = string.ascii_letters + string.punctuation + string.digits
    password = ""

    for _ in range(1, digits + 1):
        pick = choice(lett_num_punc)
        password += pick

    return password


def generator():
    is_off = False
    while not is_off:

        print("\n===== Password Generator =====\n")
        print("Please select how you want to build your password: ")
        print("1. Just letters")
        print("2. Letters and numbers")
        print("3. Letters, numbers and special digits")
        print("4. Exit password generator")

        option = int(input("Please enter an option: "))
        password = ""

        if option == 1:
            clean_console()
            num_chars = int(input("Please enter the number of characters: "))
            password += letter_gen(num_chars)
            clean_console()
            print(password)
            copy = input("Do you want to copy this password to your clipboard (Y/N)?: ").lower()
            if copy == "y":
                cp(password)
                clean_console()
                print("Password copied")
        elif option == 2:
            clean_console()
            num_chars = int(input("Please enter the number of characters: "))
            password += letter_num_gen(num_chars)
            clean_console()
            print(password)
            copy = input("Do you want to copy this password to your clipboard (Y/N)?: ").lower()
            if copy == "y":
                cp(password)
                clean_console()
                print("Password copied")
        elif option == 3:
            clean_console()
            num_chars = int(input("Please enter the number of characters: "))
            password += letter_num_punc(num_chars)
            clean_console()
            print(password)
            copy = input("Do you want to copy this password to your clipboard (Y/N)?: ").lower()
            if copy == "y":
                cp(password)
                clean_console()
                print("Password copied")
        elif option == 4:
            is_off = True
            print("Clossing password generator....")