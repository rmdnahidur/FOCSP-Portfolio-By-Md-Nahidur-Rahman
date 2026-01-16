# This function removes the last character from a string
def remove_last_char(text):
    # If the string has 0 or 1 character, just return it as it is
    if len(text) <= 1:
        return text
    # Otherwise, return everything except the last character
    return text[:-1]


# Ask the user to enter a string
user_input = input("Enter a string: ")

# Call the function and print the result
print(remove_last_char(user_input))
