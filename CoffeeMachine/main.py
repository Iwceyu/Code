machine_on = True

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 10,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5
    },
    "cappuccino":{
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.0
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

version = 1.2

def payment():
    try:
        quarters = int(input("How many quarters: ")) * 0.25
    except ValueError:
        quarters = 0
    try:
        dimes = int(input("How many dimes: ")) * 0.10
    except ValueError:
        dimes = 0
    try:
        nickles = int(input("How many nickles: ")) * 0.05
    except ValueError:
        nickles = 0
    try:
        pennies = int(input("How many pennies: ")) * 0.01
    except ValueError:
        pennies = 0


    total = quarters + dimes + nickles + pennies

    return total


def check_ingredients(choice: str):
    for i in menu_ingredients:
        if resources[i] < menu_ingredients[i]:
            print(F"Sorry there is not enough {i}.")
            return False
        else:
            resources[i] -= menu_ingredients[i]



while machine_on:
    try:
        user_choice = str(input(f"What would you like? (espresso ${MENU['espresso']['cost']}/latte ${MENU["latte"]['cost']}"
                                f"/cappuccino ${MENU["cappuccino"]['cost']}): ")).lower()

        if user_choice == "off":
            print("Turning off...")
            machine_on = False
        if user_choice == "report":
            print(f"Water: {resources["water"]}")
            print(f"Milk: {resources["milk"]}")
            print(f"Coffee: {resources["coffee"]}")
            print(f"Money: ${resources["money"]}")

        try:
            menu_ingredients = MENU[user_choice]["ingredients"]
            cost = MENU[user_choice]["cost"]

            if user_choice == "espresso":
                money = payment()
                check_ingredients(user_choice)
                if money >= cost:
                    if money > cost:
                        change = money - cost
                        print(f"Change: ${change}")
                    resources["money"] += cost
                    print(f"Making your {user_choice}")
                if money < cost:
                    print("Insuficient money.")
                    print(f"Money back: ${money}")
            if user_choice == "latte":
                money = payment()
                check_ingredients(user_choice)
                if money >= cost:
                    if money > cost:
                        change = money - cost
                        print(f"Change: ${change}")
                    resources["money"] += cost
                    print(f"Making your {user_choice}")
                if money < cost:
                    print("Insuficient money.")
                    print(f"Money back: ${money}")
            if user_choice == "cappuccino":
                money = payment()
                check_ingredients(user_choice)
                if money >= cost:
                    if money > cost:
                        change = money - cost
                        print(f"Change: ${change}")
                    resources["money"] += cost
                    print(f"Making your {user_choice}")
                if money < cost:
                    print("Insuficient money.")
                    print(f"Money back: ${money}")
        except KeyError:
            pass
    except KeyboardInterrupt:
        machine_on = False
        print("\nUser canceled.")

