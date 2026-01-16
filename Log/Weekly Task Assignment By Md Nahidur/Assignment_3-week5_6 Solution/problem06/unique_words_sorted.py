'''
6.Write a program that reads a text file and writes all unique words (no duplicates) into a new file, sorted alphabetically.
'''

# Open the input text file in read mode
file = open("E:/The British College/Level- 4 [ Computing]/Semester- 1/FOCPP Foundation of Computing (Programming)/by-weekly assignment/by_weekly assgnment solution/Assignment_3-week5_6 Solution/problem06/sample.txt", "r")

# Read the entire content
text = file.read()

# Close the input file
file.close()

# Convert text to lowercase to avoid duplicates like 'Python' and 'python'
text = text.lower()

# Remove punctuation
text = text.replace(".", "")
text = text.replace(",", "")
text = text.replace("!", "")
text = text.replace("?", "")
text = text.replace(":", "")
text = text.replace(";", "")

# Split text into words
words = text.split()

# Get unique words using set
unique_words = set(words)

# Sort words alphabetically
sorted_words = sorted(unique_words)

# Open a new file to write unique sorted words
output_file = open("E:/The British College/Level- 4 [ Computing]/Semester- 1/FOCPP Foundation of Computing (Programming)/by-weekly assignment/by_weekly assgnment solution/Assignment_3-week5_6 Solution/problem06/unique_words.txt", "w")

# Write each word on a new line
for word in sorted_words:
    output_file.write(word + "\n")

# Close the output file
output_file.close()

# Print success message
print("Unique words have been written to unique_words.txt")

