from collections import Counter

message = input("Enter a message: ").lower()

counts = Counter()

for char in message:
    if char.isalpha():
        counts[char] += 1

most_common = counts.most_common(6)

for letter, count in most_common:
    print(letter, ":", count)
