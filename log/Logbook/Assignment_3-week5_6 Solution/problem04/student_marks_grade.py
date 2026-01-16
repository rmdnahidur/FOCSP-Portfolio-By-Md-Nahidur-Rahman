'''
4. Write a program that reads a CSV file containing student names and marks, and prints the data in a well-formatted table, showing name, mark, and grade (A/B/C based on ranges). 
'''

# Open the CSV file in read mode
file = open("E:/The British College/Level- 4 [ Computing]/Semester- 1/FOCPP Foundation of Computing (Programming)/by-weekly assignment/by_weekly assgnment solution/Assignment_3-week5_6 Solution/problem04/students.csv", "r")

# Read all lines from the file
lines = file.readlines()

# Close the file
file.close()

# Print table heading
print("Name\t\tMarks\tGrade")
print("--------------------------------")

# Loop through each line in the CSV file
for line in lines:
    # Remove newline and split by comma
    name, marks = line.strip().split(",")

    # Convert marks to integer
    marks = int(marks)

    # Decide grade based on marks
    if marks >= 70:
        grade = "A"
    elif marks >= 50:
        grade = "B"
    else:
        grade = "C"

    # Print student data in table format
    print(name + "\t\t" + str(marks) + "\t" + grade)

