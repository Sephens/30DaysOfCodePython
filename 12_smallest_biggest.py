"""Write a getSmallest() function that has a numbers parameter. The numbers parameter will
be a list of integer and floating-point number values. The function returns the smallest value in the
list. If the list is empty, the function should return None. Since this function replicates Python’s
min() function, your solution shouldn’t use it."""

def getSmallest(numbers):

    if len(numbers) == 0:
        return None 
    
    smallest = numbers[0]
    for i in (numbers):
        if i < smallest:
            smallest = i
    return smallest

myList = [34,6,77,4,0]

result  = getSmallest(myList)
print(result)