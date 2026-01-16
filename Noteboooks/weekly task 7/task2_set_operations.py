def letters_in_either(word1, word2):
    return sorted(set(word1) | set(word2))


def letters_in_both(word1, word2):
    return sorted(set(word1) & set(word2))


def letters_in_one_only(word1, word2):
    return sorted(set(word1) ^ set(word2))


# Test program
w1 = input("Enter first word: ")
w2 = input("Enter second word: ")

print("At least one:", letters_in_either(w1, w2))
print("Both:", letters_in_both(w1, w2))
print("Either but not both:", letters_in_one_only(w1, w2))
