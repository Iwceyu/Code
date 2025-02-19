
def odd_even():
    """
    :return: This returns even or odd deppending on the inputs given
    """
    playing = True

    while playing:
        num = int(input("What number are you thinking? "))
        if num % 2 == 0:
            print("That's an even number.")
        else:
            print("That's an odd number")
        another = input("Have another (y/n)? ").lower()
        if another == "n":
            playing = False
    print("See you...")



odd_even()