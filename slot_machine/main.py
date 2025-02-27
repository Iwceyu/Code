import random

MAX_LINES : int = 3
MAX_BET : int = 100
MIN_BET : int = 1

ROWS = 3
COLS = 3

symbols_count : dict = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
symbol_values : dict = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winning(columns, lines, bet, values) -> int and list:
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_check = column[line]
            if symbol != symbol_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines



def machine_spin(rows : int, cols : int, symnbols : dict) -> list:
    all_symbols : list = []
    for symbol, symbol_count in symnbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns : list= []

    for _ in range(cols):
        column : list = []
        current_symbol = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)
        columns.append(column)

    return columns


def print_machine(columns) -> None:
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end= " | ")
            else:
                print(column[row], end= "")
        print()


def deposit() -> int:
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number")
    return amount


def number_of_lines() -> int:
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES})?: ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return lines


def get_bet() -> int:
    while True:
        amount = input("How much would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Please enter a number.")
    return amount


def spin(balance) -> int:
    lines: int = number_of_lines()
    while True:
        bet: int = get_bet()
        total_bet: int = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is {balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = machine_spin(ROWS, COLS, symbols_count)
    print_machine(slots)
    winnings, winning_lines = check_winning(slots, lines, bet, symbol_values)
    print(f"You won ${winnings}")
    print("You won on lines: ", *winning_lines)
    return winnings - total_bet

def main() -> None:
    balance : int = deposit()
    while True:
        print(f"Current balance is: ${balance}")
        play = input("Press enter to spin (q to quit)")
        if play == "q":
            break
        balance += spin(balance)
    print(f"You left with ${balance}")



main()