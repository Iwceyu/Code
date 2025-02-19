from rand_gen import num_gen, difficulty


def game_on():
    is_on: bool = True
    print("===== Guess the Number =====")
    print("Select the level: ")
    level: str = input("Easy(e), Medium(m) or Hard (h): ").lower()

    n_attempts: int = difficulty(level)
    number_to_guess: int = num_gen(level)

    print(f"You have {n_attempts} attempts. Good luck!")
    while is_on:

        guess = int(input("Take a guess: "))

        if n_attempts == 0:
            is_on:bool = False
            print(f"You ran out of attempts, the number was {number_to_guess}!")
        elif guess == number_to_guess:
            is_on: bool = False
            print(f"You win!! The number was {guess}!")
        elif guess < number_to_guess:
            n_attempts -= 1
            print(f"To low, you have {n_attempts} attempts left!")
        elif guess > number_to_guess:
            n_attempts -= 1
            print(f"To high, you have {n_attempts} attempts left!")



game_on()
