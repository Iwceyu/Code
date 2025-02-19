def is_acronym():
    word = input("What word do you want to know its acronym? ").lower()
    words = word.split()
    acronym = ""
    for a in words:
        if a == 'without':
            acronym += 'wo'
        else:
            acronym += a[0]
    print(acronym.upper())


is_acronym()