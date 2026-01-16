'''
6.Write a program that prompts the user for 10 integer inputs and stores only unique values in a list.
 Display the sorted list of unique numbers at the end.
'''
unique_numbers = []  # Empty list to store unique numbers

# Loop to get 10 numbers from the user
for i in range(10):
    num = int(input("Enter a number: "))
    if num not in unique_numbers:  # Check if number is already in the list
        unique_numbers.append(num)

unique_numbers.sort()  # Sort the list in ascending order
print("Sorted list of unique numbers:", unique_numbers)
