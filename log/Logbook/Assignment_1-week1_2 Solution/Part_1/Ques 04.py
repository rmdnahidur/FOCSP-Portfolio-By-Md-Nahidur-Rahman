'''
4. The sum of digits in the number 4729.
'''
# Given number
number = 4729

# Find sum of digits
sum_of_digits = 0

# Use loop to add each digit
while number > 0:
    digit = number % 10
    sum_of_digits += digit
    number //= 10

# Display the result
print("The sum of digits is:", sum_of_digits)
