# Function to check if a number is between 0 and 100 (inclusive)
def is_valid(number):
    # If the number is 0 or higher and 100 or lower, it is valid
    if 0 <= number <= 100:
        return True
    else:
        return False

# Ask the user to enter an integer
num = int(input("Enter an integer: "))

# Use the function to check if the number is valid
result = is_valid(num)

# Print True if valid, False if not
print(result)
