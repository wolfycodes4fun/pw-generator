import secrets
import string

def generate_password(length, use_symbols=False):
    characters = string.ascii_letters + string.digits
    if use_symbols:
        characters += string.punctuation
    password = "".join(secrets.choice(characters) for _ in range(length))
    print(f"Password: {password}")
