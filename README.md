# Day 10: FIND AND REPLACE
Write a findAndReplace() function that has three parameters: text is the string with text to
be replaced, oldText is the text to be replaced, and newText is the replacement text. Keep in mind
that this function must be case-sensitive: if you are replacing 'dog' with 'fox', then the 'DOG' in
'MY DOG JONESY' won’t be replaced.

At the beginning of the function, create a replacedText variable to hold the text with replacements. It starts as a blank string. We’ll write code that copies the text in the text parameter to replacedText, except for where it finds instances of oldText, in which case newText is copied to replacedText.

Create a while loop starts a variable named i at 0 and then keeps looping until i reaches the
length of the text string argument. This i variable points to an index in the text string. The code inside the loop increases i by the length of oldText if it has found an instance of oldText in text. Otherwise the code inside the loop increases i by 1 so it can examine the next character in text

The code inside the loop can examine the slice text[i:i + len(oldText)] to see if it
matches oldText. In that case, we append newText to replacedText and increase i by 1. If not, we append just the text[i] character to replacedText and increase i by len(oldText). By the time i reaches the end of text, the replacedText variable contains the finished string.