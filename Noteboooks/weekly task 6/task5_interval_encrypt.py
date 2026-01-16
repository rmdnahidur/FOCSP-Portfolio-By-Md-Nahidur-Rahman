import random
import string


def encrypt_with_interval(message):
    message = message.replace(" ", "")
    interval = random.randint(2, 20)

    encrypted = []
    for char in message:
        encrypted.append(char)
        for _ in range(interval - 1):
            encrypted.append(random.choice(string.ascii_lowercase))

    return "".join(encrypted), interval


# Test program
text = input("Enter a message: ")
encrypted_message, used_interval = encrypt_with_interval(text)

print("Encrypted message:", encrypted_message)
print("Interval used:", used_interval)
