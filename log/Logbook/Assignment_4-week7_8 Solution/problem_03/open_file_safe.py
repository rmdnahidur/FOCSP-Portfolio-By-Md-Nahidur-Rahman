'''
3.Write a program to open a file specified by the user.
If the file doesn’t exist, handle the FileNotFoundError gracefully and display an appropriate message.
'''

# Ask the user to enter the filename
filename = input("Enter the name of the file to open: ")

# Try to open the file
try:
    with open(filename, 'r') as file:  # open file in read mode
        content = file.read()  # read the content of the file
        print("\nFile content:\n")
        print(content)  # print the content of the file
except FileNotFoundError:  # handle the case when file does not exist
    print(f"Error: The file '{filename}' does not exist. Please check the filename and try again.")
