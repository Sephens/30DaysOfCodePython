"""In English, ordinal numerals have suffixes such as the ―th‖ in ―30th‖ or ―nd‖ in ―2nd‖. Write an
ordinalSuffix() function with an integer parameter named number and returns a string of the
number with its ordinal suffix. For example, ordinalSuffix(42) should return the string
'42nd'."""

number = input('Enter number to insert ordinal suffix: ')


def ordinalSuffix(number):
    # convert the number to a string
    numberStr = str(number)

    # 11, 12, and 13 have the suffix th:
    if numberStr[-2:] in ('11', '12', '13'):
        return numberStr + "th"

    # Numbers that end with 1 have the suffix st:
    elif numberStr[-1] == '1':
        return numberStr + "st"

    # Numbers that end with 2 have the suffix nd:
    elif numberStr[-1] == '2':
        return numberStr + "nd"

    # Numbers that end with 3 have the suffix rd:
    elif numberStr[-1] == '3':
        return numberStr + "rd"

    # All other numbers end with th:
    return numberStr + "th"


print(ordinalSuffix(number))
