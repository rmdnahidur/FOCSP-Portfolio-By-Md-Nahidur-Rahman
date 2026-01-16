'''
5.Create a program named advanced_calculator with functions to perform the following:
A. Square root
B. Absolute value
C. Floor division
D. Percentage (first number as a percent of the second)
E. Average of two numbers
Each should accept the required parameters and return the computed result.
'''
import math

def square_root(x):
    return math.sqrt(x)

def absolute_value(x):
    return abs(x)

def floor_division(a, b):
    return a // b

def percentage(a, b):
    return (a / b) * 100

def average(a, b):
    return (a + b) / 2

# Example usage
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Square root of", num1, ":", square_root(num1))
print("Absolute value of", num1, ":", absolute_value(num1))
print("Floor division of", num1, "by", num2, ":", floor_division(num1, num2))
print(num1, "as percentage of", num2, ":", percentage(num1, num2), "%")
print("Average of", num1, "and", num2, ":", average(num1, num2))
