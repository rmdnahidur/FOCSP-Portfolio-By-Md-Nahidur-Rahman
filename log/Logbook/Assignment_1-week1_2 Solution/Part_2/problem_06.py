'''
6.Write a program to check whether a given year is a leap year or not.
'''
# Take year input from the user
year = int(input("Enter a year: "))

# Check for leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
