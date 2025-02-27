def cm_to_inch(cm : float) -> float:
    if cm <= 0:
        print("Value must be greater than 0")
    else:
        return round(cm / 2.54, 2)


def inch_to_cm(inch : float) -> float:
    if inch <= 0:
        print("Value must be greater than 0")
    else:
        return round(inch * 2.54 , 2)


def cm_to_feet(cm : float) -> float:
    if cm <= 0:
        print("Value must be greater than 0")
    else:
        return round(cm / 30.48, 2)


def feet_to_cm(feet : float) -> float:
    if feet <= 0:
        print("Value must be greater than 0")
    else:
        return round(feet * 30.48, 2)


def inch_to_feet(inch : float) -> float:
    if inch <= 0:
        print("Value must be greater than 0")
    else:
        return round(inch/12,2)


def feet_to_inch(feet : float) -> float:
    if feet <= 0:
        print("Value must be greater than 0")
    else:
        return round(feet * 12, 2)