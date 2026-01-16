'''
2.Write a function named safe_int_input() that continuously prompts the user for an integer value until a valid integer is entered.
If the user enters something invalid, catch the exception and prompt again.
'''

# Define a function to get safe integer input from the user
def safe_int_input():
    while True:  # loop will continue until a valid integer is entered
        try:
            user_input = int(input("Enter an integer: "))  # try to convert input to integer
            return user_input  # if conversion is successful, return the integer
        except ValueError:  # handle invalid input
            print("Error: That is not a valid integer. Please try again.")  # show error message

# Main program starts here
print("Welcome! This program asks for an integer safely.")

# Call the function and store the result
number = safe_int_input()

# Print the valid integer entered by the user
print(f"You entered the valid integer: {number}")
