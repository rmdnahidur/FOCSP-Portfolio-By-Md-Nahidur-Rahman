'''
1.Write a program that asks the user to enter two numbers and performs division.
Use try…except to handle:
Division by zero
Invalid input (non-numeric values)
Print appropriate error messages in each case.
'''

# Ask user to input the first number
try:
    num1 = float(input("Enter the first number: "))  # convert input to float
except ValueError:  # handle non-numeric input
    print("Error: Please enter a valid number for the first input.")
    exit()  # stop the program if input is invalid

# Ask user to input the second number
try:
    num2 = float(input("Enter the second number: "))  # convert input to float
except ValueError:  # handle non-numeric input
    print("Error: Please enter a valid number for the second input.")
    exit()  # stop the program if input is invalid

# Perform division using try-except to handle division by zero
try:
    result = num1 / num2
    print(f"The result of {num1} divided by {num2} is: {result}")
except ZeroDivisionError:  # handle division by zero
    print("Error: Division by zero is not allowed.")
