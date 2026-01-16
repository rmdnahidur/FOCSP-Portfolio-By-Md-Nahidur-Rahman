# A list of passwords that are too easy and should not be allowed
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

# Keep asking the user until they enter a valid password
while True:
    # Ask the user to type a new password
    password1 = input("Enter a new password: ")
    
    # Ask the user to type it again to make sure it matches
    password2 = input("Confirm your password: ")

    # If the two passwords are different, show an error
    if password1 != password2:
        print("Error: Passwords do not match\n")

    # If the password is too short or too long, show an error
    elif len(password1) < 8 or len(password1) > 12:
        print("Error: Password must be between 8 and 12 characters\n")

    # If the password is very common, reject it
    elif password1.lower() in BAD_PASSWORDS:
        print("Error: Password is too common\n")

    # If everything is okay, accept the password and stop the loop
    else:
        print("Password Set")
        break
