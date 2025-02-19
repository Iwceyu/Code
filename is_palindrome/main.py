def is_palindrome(word:str='madam'):
    """
    :param word: Word to know if it's a palindrome or not
    """
    word = input("Wich word do you want to know if it's a palindrome or not?: ")
    compare = ""
    for w in word:
        compare = w + compare
    if word == compare:
        print(f"This word {word} is a palindrome.")
    else:
        print(f"That word {word} is not a palindrome.")

is_palindrome()