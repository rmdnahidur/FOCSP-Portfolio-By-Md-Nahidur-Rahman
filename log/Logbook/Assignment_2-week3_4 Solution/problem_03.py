'''
3.Write a function to determine whether a given number is a palindrome number or not.
(Example: 121 → Palindrome, 123 → Not a palindrome)
'''
def is_palindrome(number):
    original = str(number)       # Convert number to string
    reversed_num = original[::-1]  # Reverse the string
    if original == reversed_num:
        print(number, "is a palindrome")
    else:
        print(number, "is not a palindrome")

# Get input from user
num = int(input("Enter a number: "))
is_palindrome(num)
