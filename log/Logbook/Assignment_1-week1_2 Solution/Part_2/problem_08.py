'''
8.Write a program to take a character input and display whether it is a vowel or consonant.
'''
# Take a character input from the user
char = input("Enter a single character: ").lower()  # Convert to lowercase

# Check if it is a vowel or consonant
if char in 'aeiou':
    print(char, "is a vowel.")
else:
    print(char, "is a consonant.")
