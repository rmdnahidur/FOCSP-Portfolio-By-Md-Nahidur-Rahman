'''
1.Write a program that reads a text file and prints the number of vowels, consonants, digits, and special characters it contains.
'''

# Open the text file in read mode
file = open("E:/The British College/Level- 4 [ Computing]\Semester- 1/FOCPP Foundation of Computing (Programming)/by-weekly assignment/by_weekly assgnment solution/Assignment_3-week5_6 Solution/problem01/sample.txt", "r")

# Read all text from the file
text = file.read()

# Close the file
file.close()

# Initialize counters
vowels = 0
consonants = 0
digits = 0
special_chars = 0

# Loop through each character in the text
for ch in text:
    # Check for vowels
    if ch.lower() in "aeiou":
        vowels += 1

    # Check for consonants
    elif ch.isalpha():
        consonants += 1

    # Check for digits
    elif ch.isdigit():
        digits += 1

    # Everything else is special character
    else:
        special_chars += 1

# Print the result
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Special Characters:", special_chars)
