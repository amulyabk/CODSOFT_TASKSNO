
import random
import string

print("===== PASSWORD GENERATOR =====")

length = int(input("Enter password length (minimum 8): "))

if length < 8:
    print("Password length must be at least 8!")

else:
    characters = (
        string.ascii_uppercase +
        string.ascii_lowercase +
        string.digits +
        string.punctuation
    )

    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    password += random.choices(
        characters, k=length - 4
    )

    random.shuffle(password)

    password = ''.join(password)

    print("Generated Password:", password)
