# Function to convert a decimal number to binary
def to_binary(number):
    # bin() returns a string like '0b101', so we remove the '0b' with [2:]
    return bin(number)[2:]

# Ask the user to enter a positive integer
num = int(input("Enter a positive integer: "))

# Call the function and display the result
print("Binary:", to_binary(num))
