# Ask the user for the total number of students
students = int(input("How many students? "))

# Ask the user for the required size of each group
group_size = int(input("Required group size? "))

# Calculate the number of complete groups using integer division
groups = students // group_size

# Calculate how many students are left over using modulus
leftover = students % group_size

# Check if only one student is left to adjust grammar
if leftover == 1:
    print(f"There will be {groups} groups with {leftover} student left over.")
else:
    print(f"There will be {groups} groups with {leftover} students left over.")
