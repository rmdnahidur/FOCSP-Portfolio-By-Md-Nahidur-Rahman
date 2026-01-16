# Ask the user to enter a new password
password1 = input("Enter a new password: ")

# Ask the user to confirm the password
password2 = input("Confirm your password: ")

# Check if both passwords are the same
if password1 == password2:
    # Display success message if passwords match
    print("Password Set")
else:
    # Display error message if passwords do not match
    print("Error: Passwords do not match")
