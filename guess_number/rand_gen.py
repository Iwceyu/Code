from random import randint

def num_gen(level:str) -> int:
    num:int = 0
    if level == "e" or level == "easy":
        num:int = randint(1, 10)
    elif level == "m" or level == "medium":
        num:int = randint(1, 25)
    elif level == "h" or level == "hard":
        num:int = randint(1, 50)
    return num


def difficulty(level:str) -> int:
    intents:int = 0
    if level == "e" or level == "easy":
        intents:int = 15
    elif level == "m" or level == "medium":
        intents:int = 10
    elif level == "h" or level == "hard":
        intents:int = 5
    return intents
