'''
9.Write a program that reads a CSV file containing employee data (name, department, salary) and prints the average salary per department.
'''

# Open the CSV file in read mode
file = open("E:/The British College/Level- 4 [ Computing]/Semester- 1/FOCPP Foundation of Computing (Programming)/by-weekly assignment/by_weekly assgnment solution/Assignment_3-week5_6 Solution/problem09/employees.csv", "r")

# Read all lines
lines = file.readlines()

# Close the file
file.close()

# Dictionary to store total salary per department
department_salary = {}

# Dictionary to store employee count per department
department_count = {}

# Loop through each line
for line in lines:
    # Remove newline and split by comma
    name, department, salary = line.strip().split(",")
    
    # Convert salary to float
    salary = float(salary)
    
    # Add salary to department total
    if department in department_salary:
        department_salary[department] += salary
        department_count[department] += 1
    else:
        department_salary[department] = salary
        department_count[department] = 1

# Print average salary per department
print("Average Salary per Department:")
for dept in department_salary:
    avg_salary = department_salary[dept] / department_count[dept]
    print(f"{dept}: {avg_salary:.2f}")
