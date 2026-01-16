"""
Program Name: Lambda, Map and Filter Example
Description:
This program uses:
1. lambda and map() to square each number in a list
2. filter() to select squared values greater than 10
"""

# Original list of numbers
numbers = [1, 2, 3, 4, 5]

# Use map() and lambda to square each number
squared_numbers = list(map(lambda x: x * x, numbers))

# Use filter() and lambda to get values greater than 10
greater_than_ten = list(filter(lambda x: x > 10, squared_numbers))

# Display results
print("Original List:", numbers)
print("Squared Numbers:", squared_numbers)
print("Squared Numbers Greater Than 10:", greater_than_ten)
