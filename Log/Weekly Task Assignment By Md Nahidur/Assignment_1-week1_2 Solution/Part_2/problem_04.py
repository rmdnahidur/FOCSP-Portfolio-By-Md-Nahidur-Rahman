'''
4.Write a program that prompts the user for an age, and prints whether the person is a child (below 13), 
teenager (13–19), or adult (20 and above).
'''
# Take age input from the user
age = int(input("Enter your age: "))

# Check the category
if age < 13:
    print("You are a child.")
elif 13 <= age <= 19:
    print("You are a teenager.")
else:
    print("You are an adult.")
