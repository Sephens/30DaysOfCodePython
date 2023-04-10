"""Write a findAndReplace() function that has three parameters: text is the string with text to
be replaced, oldText is the text to be replaced, and newText is the replacement text. Keep in mind
that this function must be case-sensitive: if you are replacing 'dog' with 'fox', then the 'DOG' in
'MY DOG JONESY' won’t be replaced."""

def findAndReplace(text, oldText, newText):
    # a variable to hold the text with replacements
    replacedText = ''
    i = 0
    while i < len(text):
        # If index i in text is the start of the oldText pattern, add
        # the replacement text:
        if text[i:i + len(oldText)] == oldText:
            # Add the replacement text:
            oldText += newText
            # Increment i by the length of oldText:
            i += len(oldText)
        # Otherwise, add the characters at text[i] and increment i by 1:
        else:
            replacedText += text[i]
            i += 1
    return replacedText

print(findAndReplace('The book of good', 'good', 'brooms'))