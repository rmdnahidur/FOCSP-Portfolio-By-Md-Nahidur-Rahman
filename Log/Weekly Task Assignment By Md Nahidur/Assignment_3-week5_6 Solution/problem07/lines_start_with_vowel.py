'''
7.Write a program that reads a file and counts how many lines begin with a vowel (A, E, I, O, U).
'''

# Open the text file in read mode
file = open("E:/The British College/Level- 4 [ Computing]/Semester- 1/FOCPP Foundation of Computing (Programming)/by-weekly assignment/by_weekly assgnment solution/Assignment_3-week5_6 Solution/problem07/sample.txt", "r")

# Read all lines from the file
lines = file.readlines()

# Close the file
file.close()

# Initialize counter
vowel_lines = 0

# Loop through each line
for line in lines:
    # Remove leading/trailing whitespace
    line = line.strip()
    
    # Skip empty lines
    if len(line) == 0:
        continue
    
    # Check if first character is a vowel
    if line[0].lower() in "aeiou":
        vowel_lines += 1

# Print the result
print("Number of lines starting with a vowel:", vowel_lines)
