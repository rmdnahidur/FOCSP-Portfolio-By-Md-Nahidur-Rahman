'''
12.Write a function called common_letters that takes two words and returns a sorted list of all unique letters
 that appear in both words.
'''
# Function to find common letters between two words
def common_letters(word1, word2):
    # Convert both words into sets to get unique letters
    set1 = set(word1)
    set2 = set(word2)

    # Find common letters using intersection
    common = set1.intersection(set2)

    # Return the letters in a sorted list
    return sorted(common)

# Example use
result = common_letters("apple", "grape")
print("Common letters:", result)
