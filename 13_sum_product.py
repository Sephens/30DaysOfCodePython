"""Write two functions named calculateSum() and calculateProduct(). They both have a
parameter named numbers, which will be a list of integer or floating-point values. The
calculateSum() function adds these numbers and returns the sum while the
calculateProduct() function multiplies these numbers and returns the product. If the list passed
to calculateSum() is empty, the function returns 0. If the list passed to calculateProduct()
is empty, the function returns 1. Since this function replicates Python’s sum() function, your solution
shouldn’t call."""

# Function calculate sum


def calculateSum(numbers):
    # check wether the list is empty
    if len(numbers) == 0:
        return 0

    result = 0
    for i in numbers:
        result += i
    return result


def calculateProduct(numbers):
    if len(numbers) == 0:
        return 0

    result = 1
    for i in numbers:
        result *= i
    return result


print(calculateSum([3, 5, 7, 99]))
print(calculateProduct([3, 5, 7, 99]))
