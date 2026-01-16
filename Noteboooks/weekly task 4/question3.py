# Ask the user to enter their name and remove any extra spaces at the start or end
name = input("Enter your name: ").strip()

# Check if the user entered nothing
if name == "":
    # If no name was entered, greet them as "Stranger"
    print("Hello, Stranger!")
else:
    # If a name was entered, capitalize the first letter and greet them
    print("Hello,", name.capitalize())
