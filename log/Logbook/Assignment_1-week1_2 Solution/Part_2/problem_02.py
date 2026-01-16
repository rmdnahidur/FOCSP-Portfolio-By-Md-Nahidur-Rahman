'''
2.Write a program that asks for two integers and displays the remainder and quotient after dividing the first by the second.
'''
# Take input from the user
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# Calculate quotient and remainder
quotient = num1 // num2
remainder = num1 % num2

# Display the results
print("Quotient:", quotient)
print("Remainder:", remainder)
