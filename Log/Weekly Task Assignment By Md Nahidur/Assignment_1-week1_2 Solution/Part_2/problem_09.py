'''
9.Write a program that asks the user to enter a number between 1 and 7, and displays the corresponding day
 of the week (1 for Sunday, 2 for Monday, etc.).
'''
# Take number input from the user
day_number = int(input("Enter a number between 1 and 7: "))

# List of days
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# Check if number is valid and display the day
if 1 <= day_number <= 7:
    print("The day is:", days[day_number - 1])
else:
    print("Invalid input! Please enter a number between 1 and 7.")
