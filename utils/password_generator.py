import secrets
import string

def generate_password(length, use_numbers=False, use_symbols=False):
    characters = string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    password = "".join(secrets.choice(characters) for _ in range(length))
    print(f"Password: {password}")
