'''
8.Write a program that reads a text file and reverses the contents of each line, then writes the reversed lines into a new file called reversed.txt.
'''

# Open the input file in read mode
file = open("E:/The British College/Level- 4 [ Computing]/Semester- 1/FOCPP Foundation of Computing (Programming)/by-weekly assignment/by_weekly assgnment solution/Assignment_3-week5_6 Solution/problem08/sample.txt", "r")

# Read all lines from the file
lines = file.readlines()

# Close the input file
file.close()

# Open the output file in write mode
output_file = open("E:/The British College/Level- 4 [ Computing]/Semester- 1/FOCPP Foundation of Computing (Programming)/by-weekly assignment/by_weekly assgnment solution/Assignment_3-week5_6 Solution/problem08/reversed.txt", "w")

# Loop through each line
for line in lines:
    # Remove newline at the end
    line = line.rstrip("\n")
    
    # Reverse the line
    reversed_line = line[::-1]
    
    # Write the reversed line into the new file
    output_file.write(reversed_line + "\n")

# Close the output file
output_file.close()

# Print success message
print("Reversed lines have been written to reversed.txt")
