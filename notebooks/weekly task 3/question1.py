# Ask the user to enter their name and remove any extra spaces
name = input("Enter your name: ").strip()

# Check if the user did not enter anything
if name == "":
    # Greet with a default name if input is empty
    print("Hello, Stranger!")
else:
    # Greet the user using the name they entered
    print("Hello,", name)
