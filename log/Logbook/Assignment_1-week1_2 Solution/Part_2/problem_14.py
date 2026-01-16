'''
14.Write a Python program that accepts a string and calculates the number of digits and letters. 
'''
# Take string input from the user
text = input("Enter a string: ")

# Initialize counters
letters = 0
digits = 0

# Loop through each character in the string
for char in text:
    if char.isalpha():  # Check if character is a letter
        letters += 1
    elif char.isdigit():  # Check if character is a digit
        digits += 1

# Display the results
print("Letters:", letters)
print("Digits:", digits)
