'''
2. Write a program to merge the contents of two text files into a third file. The third file 
should contain the combined contents of both, separated by a line "----- End of File 1 -----".
'''

# Open first file in read mode
file1 = open("E:/The British College/Level- 4 [ Computing]/Semester- 1/FOCPP Foundation of Computing (Programming)/by-weekly assignment/by_weekly assgnment solution/Assignment_3-week5_6 Solution/problem02/file1.txt", "r")
content1 = file1.read()
file1.close()

# Open second file in read mode
file2 = open("E:/The British College/Level- 4 [ Computing]/Semester- 1/FOCPP Foundation of Computing (Programming)/by-weekly assignment/by_weekly assgnment solution/Assignment_3-week5_6 Solution/problem02/file2.txt", "r")
content2 = file2.read()
file2.close()

# Open third file in write mode
file3 = open("E:/The British College/Level- 4 [ Computing]/Semester- 1/FOCPP Foundation of Computing (Programming)/by-weekly assignment/by_weekly assgnment solution/Assignment_3-week5_6 Solution/problem02/merged_file.txt", "w")

# Write content of first file
file3.write(content1)

# Write separator line
file3.write("\n----- End of File 1 -----\n")

# Write content of second file
file3.write(content2)

# Close the third file
file3.close()

# Print success message
print("Files merged successfully into merged_file.txt")
