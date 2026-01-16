def unique_letters(text):
    return sorted(set(text))


# Test program
word = input("Enter a word: ")
print(unique_letters(word))
