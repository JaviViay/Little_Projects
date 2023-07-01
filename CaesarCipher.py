#banner
print("\033[92m .--." + "              ___ __ _  ___  ___  __ _ _ __")
print("/.-. '----------." + " / __/ _` |/ _ \/ __|/ _` | '__|")
print("|'-' .--^--^^--^´" + "| (_| (_| |  __/\__ \ (_| | |")
print(" '--'" + "             \___\__,_|\___||___/\__,_|_|   \033[0m")

#enter the text to be encrypted
text = str(input("Enter the text: "))
#enter the number of positions to shift the characters
times = int(input("How many times to desplace?: "))
#initialize an empty string for the output
output = ""

#iterate over each character in the input text
for character in text:
    #check if the character is a letter
    if character.isalpha():
        #get the unicode code point of the character
        code = ord(character)
        code += times

        #handle wrapping around for uppercase letters
        if character.islower():
            if code > ord("z"):
                code -= 26
            elif code < ord("a"):
                code += 26

        #handle wrapping around for uppercase letters
        elif character.isupper():
            if code > ord("Z"):
                code -= 26
            elif code < ord("A"):
                code += 26

        #convert the modified code point back to a character and add it to the output string
        output += chr(code)
    #if the character is not a letter, simply add it to the output string
    else:
        output += character

#print the encrypted text
print("\033[33m" + output + "\033[0m")