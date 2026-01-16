def encrypt(message):
    no_spaces = message.replace(" ", "")
    return no_spaces[::-1]


# Test program
text = input("Enter a message: ")
print("Encrypted:", encrypt(text))
