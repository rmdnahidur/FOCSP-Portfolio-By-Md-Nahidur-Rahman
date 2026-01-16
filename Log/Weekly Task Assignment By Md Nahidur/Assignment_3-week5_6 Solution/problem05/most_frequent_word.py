'''
5.Develop a program that reads a text file and displays the most frequently occurring word along with its number of occurrences.
'''

# Open the text file in read mode
file = open("E:/The British College/Level- 4 [ Computing]/Semester- 1/FOCPP Foundation of Computing (Programming)/by-weekly assignment/by_weekly assgnment solution/Assignment_3-week5_6 Solution/problem05/sample.txt", "r")

# Read all text from the file
text = file.read()

# Close the file
file.close()

# Convert text to lowercase
text = text.lower()

# Remove common punctuation
text = text.replace(".", "")
text = text.replace(",", "")
text = text.replace("!", "")
text = text.replace("?", "")

# Split text into words
words = text.split()

# Dictionary to store word counts
word_count = {}

# Count each word
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Find the most frequent word
most_word = ""
most_count = 0

for word in word_count:
    if word_count[word] > most_count:
        most_word = word
        most_count = word_count[word]

# Display result
print("Most frequent word:", most_word)
print("Number of occurrences:", most_count)
