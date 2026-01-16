'''
3. Write a program that searches for a specific word in a text file and prints the line numbers where that word occurs.
'''
# Ask user to enter the word to search
search_word = input("Enter the word to search: ")

# Open the text file in read mode
file = open("E:/The British College/Level- 4 [ Computing]/Semester- 1/FOCPP Foundation of Computing (Programming)/by-weekly assignment/by_weekly assgnment solution/Assignment_3-week5_6 Solution/problem03/sample.txt", "r")

# Read all lines from the file
lines = file.readlines()

# Close the file
file.close()

# Variable to check if word is found
found = False

# Loop through each line with line number
line_number = 1
for line in lines:
    # Check if search word is in the line
    if search_word.lower() in line.lower():
        print("Word found at line number:", line_number)
        found = True

    # Increase line number
    line_number += 1

# If word is not found
if not found:
    print("Word not found in the file.")
