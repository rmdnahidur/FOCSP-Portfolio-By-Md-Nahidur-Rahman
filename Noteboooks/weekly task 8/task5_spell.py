import sys
import string

if len(sys.argv) < 2:
    print("Error: No file provided")
    sys.exit()

filename = sys.argv[1]


DICTIONARY = set(["this", "is", "a", "simple", "test", "file", "with", "words"])

try:
    with open(filename, 'r') as f:
        text = f.read().lower()

    # Remove punctuation
    for p in string.punctuation:
        text = text.replace(p, "")

    words = text.split()
    unknown_words = [word for word in words if word not in DICTIONARY]

    if unknown_words:
        print("Unknown words:", ", ".join(unknown_words))
    else:
        print("No unknown words found")
except FileNotFoundError:
    print("Error: File not found")
