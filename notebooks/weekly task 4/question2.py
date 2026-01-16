# This function counts how many uppercase and lowercase letters are in a string
def count_case(text):
    upper = 0  # To keep track of uppercase letters
    lower = 0  # To keep track of lowercase letters

    # Go through each character in the text
    for char in text:
        if char.isupper():  # If the character is uppercase
            upper += 1      # Add 1 to the uppercase counter
        elif char.islower():  # If the character is lowercase
            lower += 1       # Add 1 to the lowercase counter

    # Return both counts so we can use them outside the function
    return upper, lower


# Ask the user to enter any string
string = input("Enter a string: ")

# Call the function to count uppercase and lowercase letters
upper, lower = count_case(string)

# Show the results in a friendly way
print("Uppercase letters:", upper)
print("Lowercase letters:", lower)
