'''
1.Write a program to take a number input from the user and display whether the number is positive, negative, or zero.
'''
# Take input from the user
number = float(input("Enter a number: "))

# Check if the number is positive, negative, or zero
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
