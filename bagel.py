"""Bagels, by Steve adesephens@gmail.com
A deductive logic game where you must guess a number based on clues.
Tags: short, game, puzzle"""

# random — Generate pseudo-random numbers
import random

NUMBER_OF_DIGITS = 3
NUMBER_OF_GUESS = 10

# define a main function
def main():
    print(''' Bagels, A deductive logic game.
    By Steve

    I am thinking of a {}-digit number with no repeated digits.
    Try to guess what it is. Here are some clues:
    When I say:         That means:
        Pico :       One digit is correct but in the wrong position.
        Fermi :      One digit is correct and in the right position.
        Bagels :     No digit is correct.

    For example, if the secret number was 248 and your guess was 843, the
    clues would be Fermi Pico.'''.format(NUMBER_OF_DIGITS))

    while True: # The main loop of the game

        secretNum = getSecretNum()
        print('I have thought up a number')
        print('You have {} guesses to get it'.format(NUMBER_OF_GUESS))

        numGuesses = 1
        while numGuesses <= NUMBER_OF_GUESS:
            guess = ''
            # Keep looping until they enter a valid guess:
            while len(guess) != NUMBER_OF_DIGITS or not guess.isdecimal():
                print('Guess #{}:'.format(numGuesses))
                guess = input('> ')

                clues = getClause(guess, secretNum)
                print(clues)

                numGuesses += 1

                if guess == secretNum:
                    break
                if numGuesses > NUMBER_OF_GUESS:
                    print('You ran out of guesses')
                    print('The answer was {}'.format(secretNum))
        print('Do you want to play again? (Y/N)')
        if not input('> ').lower().startswith('y'):
            break
    print('Bye, Thank you for playing...')


# Returns a list of NUM_DIGITS unique random digits
def getSecretNum():
    numbers = list('0123456789')  # a list of 10 digits from 1 to 9
    random.shuffle(numbers)  # randomly shuffle the numbers in the list

    # Get the first NUM_DIGITS digits in the list for the secret number:
    secretNum = ''
    for i in range(NUMBER_OF_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


def getClause(guess, secretNum):
    """Returns a string with the pico, fermi, bagels clues for a guess nd secret number pair."""
    if guess == secretNum:
        return 'Hurray!! You got it'

    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
                # A correct digit is in the correct place.
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    if len(clues) == 0:
        clues.append('Bagels')
    else:
            # Sort the clues into alphabetical order so their original order
            # doesn't give information away.
        clues.sort()

            # Make a single string from the list of string clues.
        return ' '.join(clues)


# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()
