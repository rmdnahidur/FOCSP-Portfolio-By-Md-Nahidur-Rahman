"""
Program Name: List Comprehension Example
Description:
This program uses a one-line list comprehension to
find numbers between 1 and 100 that are divisible
by both 3 and 5.
"""

# One-line list comprehension
numbers = [x for x in range(1, 101) if x % 3 == 0 and x % 5 == 0]

# Display result
print("Numbers divisible by both 3 and 5:")
print(numbers)
