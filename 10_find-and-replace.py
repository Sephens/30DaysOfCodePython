"""Write a findAndReplace() function that has three parameters: text is the string with text to
be replaced, oldText is the text to be replaced, and newText is the replacement text. Keep in mind
that this function must be case-sensitive: if you are replacing 'dog' with 'fox', then the 'DOG' in
'MY DOG JONESY' won’t be replaced."""

def findAndReplace(text, oldText, newText):
    # a variable to hold the text that was replaced
    replacedText = ''
    
    index = 0
    
    while index < len(text):
    # If index i in text is the start of the oldText pattern, add
    # the replacement text:
        if text[index:index + len(oldText)] == oldText:
            # Add the replacement text:
            replacedText += newText
            # Increment i by the length of oldText:
            index += len(oldText)
     # Otherwise, add the characters at text[i] and increment i by 1:
        else:
            replacedText += text[index]
            index += 1
    return replacedText

print(findAndReplace("The book of good is good", "good", "godies"))