'''
11.Write a program to implement a class called employee with attributes such as empid, name, address, contact_number, spouse name, number_of_child, salary. Instantiate this class to input the values for multiple employees and write it in a file “employees.csv”. Allow the user of your program to see the list of employees and their details as well. Try to use the concept of try/except too in the program. 
'''

import csv

# Define Employee class
class Employee:
    def __init__(self, empid, name, address, contact_number, spouse_name, number_of_child, salary):
        self.empid = empid
        self.name = name
        self.address = address
        self.contact_number = contact_number
        self.spouse_name = spouse_name
        self.number_of_child = number_of_child
        self.salary = salary

# Function to input employee data safely
def input_employee():
    while True:
        try:
            empid = input("Enter Employee ID: ")
            name = input("Enter Name: ")
            address = input("Enter Address: ")
            contact_number = input("Enter Contact Number: ")
            spouse_name = input("Enter Spouse Name: ")
            number_of_child = int(input("Enter Number of Children: "))
            salary = float(input("Enter Salary: "))
            break
        except ValueError:
            print("Invalid input! Please enter correct data types.")
    return Employee(empid, name, address, contact_number, spouse_name, number_of_child, salary)

# List to store multiple employees
employee_list = []

# Ask user how many employees to enter
while True:
    try:
        n = int(input("How many employees do you want to enter? "))
        break
    except ValueError:
        print("Please enter a valid number.")

# Input employee data
for i in range(n):
    print(f"\nEnter details for Employee {i+1}:")
    emp = input_employee()
    employee_list.append(emp)

# Write employee data to CSV file
with open("E:/The British College/Level- 4 [ Computing]/Semester- 1/FOCPP Foundation of Computing (Programming)/by-weekly assignment/by_weekly assgnment solution/Assignment_3-week5_6 Solution/problem11/employees.csv", "w", newline="") as file:
    writer = csv.writer(file)
    # Write header
    writer.writerow(["EmpID", "Name", "Address", "Contact Number", "Spouse Name", "Number of Children", "Salary"])
    # Write employee details
    for emp in employee_list:
        writer.writerow([emp.empid, emp.name, emp.address, emp.contact_number, emp.spouse_name, emp.number_of_child, emp.salary])

# Display employee list
print("\nEmployee List:")
print("{:<10} {:<20} {:<20} {:<15} {:<20} {:<10} {:<10}".format(
    "EmpID","Name","Address","Contact","Spouse","Children","Salary"
))
for emp in employee_list:
    print("{:<10} {:<20} {:<20} {:<15} {:<20} {:<10} {:<10}".format(
        emp.empid, emp.name, emp.address, emp.contact_number, emp.spouse_name, emp.number_of_child, emp.salary
    ))

print("\nAll employee details have been saved to 'employees.csv'")
