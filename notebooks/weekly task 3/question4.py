# List of common passwords that are not allowed
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

# Ask the user to enter a new password
password1 = input("Enter a new password: ")

# Ask the user to confirm the password
password2 = input("Confirm your password: ")

# Check if the two passwords do not match
if password1 != password2:
    print("Error: Passwords do not match")

# Check if the password length is not between 8 and 12 characters
elif len(password1) < 8 or len(password1) > 12:
    print("Error: Password must be between 8 and 12 characters")

# Convert the password to lowercase and check if it is too common
