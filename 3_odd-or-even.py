"""Write two functions, isOdd() and isEven(), with a single numeric parameter named
number. The isOdd() function returns True if number is odd and False if number is even. The
isEven() function returns the True if number is even and False if number is odd. Both
functions return False for numbers with fractional parts, such as 3.14 or -4.5. Zero is considered
an even number."""


def isOdd(number):
    # Return whether number mod 2 is 1:
    return number % 2 == 1


def isEven(number):
    # Return whether number mod 2 is 0:
    return number % 2 == 0


print(isOdd(11.4))
