import random

COLORS : list = ["R", "G", "B", "Y", "W", "O"]
TRIES = 10
CODE_LENGTH = 4


def generate_code() -> list:
    code : list = []

    for _ in range(CODE_LENGTH):
        color : str = random.choice(COLORS)
        code.append(color)

    return code


def guess_code() -> list:
    while True:
        guess : list = input("Guess: ").upper().split(" ")

        if len(guess) != 4:
            print(f"You must guess {CODE_LENGTH} colors.")
            continue

        for color in guess:
            if color not in COLORS:
                print(f"Invalid color: {color}. Try again.")
                break
        else:
            break

    return guess


def check_code(guess : list, real_code : list) -> int and int:
    color_counts : dict= {}
    correct_pos : int = 0
    incorrect_pos : int = 0

    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1

    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_pos += 1
            color_counts[guess_color] -= 1

    for guess_color, real_color in zip(guess, real_code):
        if guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_pos += 1
            color_counts[guess_color] -= 1

    return correct_pos, incorrect_pos

def game() -> None:
    print(f"Welcome to mastermind, you have {TRIES} tries to guess the code...")
    print("The valid colors are:", *COLORS)
    code : list = generate_code()
    for attempts in range(1, TRIES + 1):
        guess : list = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)

        if correct_pos == CODE_LENGTH:
            print(f"You guessed the code in {attempts} tries!")

        print(f"Correct Positions: {correct_pos} | Incorrect Positions: {incorrect_pos}")
    else:
        print("You ran out of tries, the code was:", *code)


if __name__ == "__main__":
    game()