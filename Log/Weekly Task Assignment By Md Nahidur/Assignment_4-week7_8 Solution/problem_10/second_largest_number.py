"""
Program Name: Second Largest Number
Description:
This program reads a list of numbers from the user
and finds the second largest number.
It handles the following exceptions:
1. User enters fewer than two numbers
2. User enters non-numeric values
"""

try:
    # Take input from user (numbers separated by space)
    user_input = input("Enter numbers separated by space: ")

    # Convert input into a list of integers
    numbers = list(map(int, user_input.split()))

    # Check if there are at least two numbers
    if len(numbers) < 2:
        raise ValueError("Please enter at least two numbers.")

    # Remove duplicates and sort the list
    unique_numbers = list(set(numbers))
    unique_numbers.sort(reverse=True)

    # Check again after removing duplicates
    if len(unique_numbers) < 2:
        raise ValueError("Second largest number does not exist.")

    # Find second largest number
    second_largest = unique_numbers[1]

    print("Second largest number is:", second_largest)

# Handle non-numeric input
except ValueError as e:
    print("Error:", e)
