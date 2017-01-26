def alphabet_position(letter):
    position = 0
    if letter.isupper():
        position = ord(letter) - ord('A')
    else:
        position = ord(letter) - ord('a')
    return(position)

def rotate_character(char, rot):
    #if char is not in the alphabet, exit by returning char
    if not char.isalpha():
        return char
    #rotate by the passed number of characters; if number is greater than 26,
    #calculate the proper number to rotate (between 0 and 25)
    currPos = alphabet_position(char)
    newPos = currPos + rot
    if newPos >= 26:
        newPos = newPos % 26
    #calculate new position depending on upper or lower case letters
    if char.isupper():
        finalChar = ord('A') + newPos
    else:
        finalChar = ord('a') + newPos
    return chr(finalChar)

def encrypt(text, rot):
    enc_string = ""
    for char in text:
        enc_string += rotate_character(char, rot)
    return enc_string
