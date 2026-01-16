'''
10. Create a class Student with the attributes such as id, name, address, admission year, level, section. Instantiate the object of class to take input for all the attributes and display the output. 
'''
# Define the Student class
class Student:
    def __init__(self, student_id, name, address, admission_year, level, section):
        self.student_id = student_id
        self.name = name
        self.address = address
        self.admission_year = admission_year
        self.level = level
        self.section = section

    # Method to display student details
    def display_info(self):
        print("\nStudent Information:")
        print("ID:", self.student_id)
        print("Name:", self.name)
        print("Address:", self.address)
        print("Admission Year:", self.admission_year)
        print("Level:", self.level)
        print("Section:", self.section)

# Main program
# Take input from user
student_id = input("Enter Student ID: ")
name = input("Enter Name: ")
address = input("Enter Address: ")
admission_year = input("Enter Admission Year: ")
level = input("Enter Level: ")
section = input("Enter Section: ")

# Create Student object
student1 = Student(student_id, name, address, admission_year, level, section)

# Display student information
student1.display_info()
