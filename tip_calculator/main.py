

def tip_calculator():
    bill = float(input("What's the total bill for today: $"))
    people = int(input("How much people where eating?: "))
    tip = int(input("How much tip do you want to give (18%, 20%, 25%)?: "))
    tip_amount = bill * (tip/100)
    total = bill + tip_amount

    print(f"Your tip is: ${round(tip_amount, 2)}, which brings your total to: ${round(total, 2)}")
    if people == 2:
        one_pays = round(total/people, 2)
        print(f"One pays ${round(total-one_pays,2)} and the other pays ${one_pays}")
    elif people > 2:
        print(f"Everyone should pay: ${round(total/people, 2)}")


tip_calculator()