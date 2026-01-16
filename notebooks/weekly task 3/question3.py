# Ask the user to enter a new password
password1 = input("Enter a new password: ")

# Ask the user to confirm the password
password2 = input("Confirm your password: ")

# Check if the two passwords do NOT match
if password1 != password2:
    print("Error: Passwords do not match")

# Check if the password length is less than 8 or more than 12 characters
elif len(password1) < 8 or len(password1) > 12:
    print("Error: Password must be between 8 and 12 characters")

# If both conditions above are false, the password is valid
else:
    print("Password Set")
