import secrets
import string
import sys
import argparse

def generate_password(length):
    alphabet = string.ascii_letters + string.digits
    password = "".join(secrets.choice(alphabet) for _ in range(length))
    print(f"Password: {password}")

if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print("Usage: gen_password.py <length_of_password>")
        sys.exit(1)
    
    parser = argparse.ArgumentParser(description="Generate a password for your convienience")
    parser.add_argument("length", type=int, help="Length of password")

    try:
        generate_password(parser.parse_args().length)
    except Exception as e:
        print("An exception has occured: " + e)