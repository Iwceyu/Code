import random


def roll() -> int:
    """
    :return: Random integer value between 1 and 6.
    """
    min_val : int = 1
    max_val : int = 6
    roll : random = random.randint(min_val, max_val)
    return roll


while True:
    players = input("Enter the number of players (2 - 4): ")

    # Checking if is a valid number
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players")
    else:
        print("Invalid, try again.")


max_score : int = 50
player_scores : list = [0 for _ in range(players)]

while max(player_scores) < max_score:

    for player_indx in range(players):
        print(f"\nPlayer {player_indx + 1}, turn has just started!")
        print(f"Your total score is: {player_scores[player_indx]}\n")
        current_score : int = 0

        while True:
            should_roll : str = input("Would you like to roll (y/n): ")
            if should_roll.lower() != "y" and should_roll.lower() != "":
                break

            value : int = roll()
            if value == 1:
                print("You rolled a 1! Turnd done!")
                current_score += 0
                break
            else:
                current_score += value
                print(f"You rolled a: {value}")
            print(f"Your current score is: {current_score}")

        player_scores[player_indx] += current_score
        print(f"Your total score is: {player_scores[player_indx]}")


max_score = max(player_scores)
winner_idx = player_scores.index(max_score)
print(f"\nPlayer number {winner_idx + 1} is the winner with a score of {max_score}!")