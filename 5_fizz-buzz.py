"""Write a fizzBuzz() function with a single integer parameter named upTo. For the numbers 1
up to and including upTo, the function prints one of four things:
Prints 'FizzBuzz' if the number is divisible by 3 and 5.
Prints 'Fizz' if the number is only divisible by 3.
Prints 'Buzz' if the number is only divisible by 5.
Prints the number if the number is neither divisible by 3 nor 5."""

upTo = int(input('Enter the upTo number: '))

numbers = range(1,upTo + 1)

def fizzBuzz(upTo):
    # Loop from 1 up to (and including) the upTo parameter:
   for number in numbers:
       # If the loop number is divisible by 3 and 5, print 'FizzBuzz':
       if number % 3 == 0 and number % 5 == 0:
           print("FizzBuzz", end=' ')
        # Otherwise the loop number is divisible by only 3, print 'Fizz':
       elif number % 3 == 0:
           print("Fizz", end=' ')
        # Otherwise the loop number is divisible by only 5, print 'Buzz':
       elif number % 5 == 0:
           print("Buzz", end=' ')
        # Otherwise, print the loop number:
       else:
           print(number, end=' ')
           
fizzBuzz(upTo)
    