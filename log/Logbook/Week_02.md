# Week 2 – Variables, Data Types & Basic Python Concepts
# Level 4 – Semester 1 – BSc (Hons) Computing – Leeds Beckett University

# -----------------------------
# 1. Purpose of This Week
# -----------------------------
# Learn Python basics: variables, data types, functions, strings, lists, and user input.

# -----------------------------
# 2. Variables
# -----------------------------
# Variables store data for later use
age = 23
name = "Jon"

# Rules for variable names:
# - Must start with a letter or _
# - Can contain letters, numbers, _
# - Case-sensitive
student_name = "Alice"  # valid
# 1person = "Bob"        # invalid

# -----------------------------
# 3. Assignment
# -----------------------------
average = (10 + 20 + 30) / 3  # compute and assign
age = age + 1                  # update variable
count = 0
count += 1                     # augmented assignment
score = 10
score *= 2

# -----------------------------
# 4. Data Types
# -----------------------------
# Common types: int, float, bool, str
x = 10        # int
x = 10.5      # float
x = "hi"      # str

# Check type
print(type(x))  # <class 'str'>

# -----------------------------
# 5. Functions
# -----------------------------
# Functions are reusable code blocks
print("Hello")      # prints a message
print("Total:", 100)  # prints multiple values

# -----------------------------
# 6. Getting User Input
# -----------------------------
# input() always returns string
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))

# -----------------------------
# 7. Strings
# -----------------------------
# Text enclosed in quotes
s1 = "Hello"
s2 = 'Welcome'
s3 = """This is
a multi-line string"""

# Escape characters
print("Line1\nLine2")  # new line
print("Column1\tColumn2")  # tab
print("He said: \"Hi\"")

# -----------------------------
# 8. String Indexing & Slicing
# -----------------------------
name = "Black Knight"
print(name[0])   # 'B'
print(name[-1])  # 't'

# Slicing
print(name[0:5])  # 'Black'
print(name[:3])   # 'Bla'
print(name[6:])   # 'Knight'

# -----------------------------
# 9. Lists
# -----------------------------
# Store multiple values
names = ["Terry", "John", "Eric"]
scores = [10, 20, 30]

# Lists are mutable
names[0] = "Mark"

# -----------------------------
# 10. Modifying Lists
# -----------------------------
# Add items
names.append("Sam")

# Modify or remove using slicing
scores[2:3] = [50]
scores[-2:] = []

# Length of list or string
print(len(names))
print(len("Hello"))

# -----------------------------
# 11. Summary
# -----------------------------
# - Variables store data
# - Python uses dynamic types
# - Strings store text; lists store multiple values
# - Functions like print() and input() allow interaction
# - Indexing & slicing access parts of strings and lists
