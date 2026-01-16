'''
1.Write a function that takes a string as input and returns:
The number of digits,
The number of alphabets
The number of special characters in that string.
'''
def count_chars(text):
    digits = 0
    letters = 0
    special = 0

    for ch in text:
        if ch >= '0' and ch <= '9':
            digits += 1
        elif (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z'):
            letters += 1
        else:
            special += 1

    print("Digits:", digits)
    print("Alphabets:", letters)
    print("Special Characters:", special)

# Get input from user
text = input("Enter a string: ")
count_chars(text)
