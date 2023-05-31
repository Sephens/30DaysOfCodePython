"""Write a printASCIITable() function that displays the ASCII number and its corresponding
text character, from 32 to 126. (These are called the printable ASCII characters.)
Your solution is correct if calling printASCIITable() displays output that looks like the
following:
32
33 !
34 "
35 #
--more--
124 |
125 }
126 ~
"""

# ASCII stands for American Standard Code for Information Interchange. Computers can only store
# numbers, so each letter, numeral, punctuation mark, and every other character is assigned a number
# called a code point. ASCII was a popular standard mapping of text characters to numbers. For example,
# 'Hello' would be represented by 72, 101, 108, 108, 111. Specifically, computers only store the ones
# and zeros of binary numbers. These decimal numbers translate to 01001000, 01100101, 01101100,
# 01101100, 01101111 in binary. An ASCII table showed all the characters and their assigned ASCII
# number values.

def printASCIITable():
    # Loop over integers 32 up to and including 126:
    for number in range(32,127):
        # Print the integer and its ASCII text character:
        print(number, chr(number))
        
printASCIITable()