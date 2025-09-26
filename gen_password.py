import secrets
import string
import argparse

def generate_password(length):
    alphabet = string.ascii_letters + string.digits
    password = "".join(secrets.choice(alphabet) for _ in range(length))
    print(f"Password: {password}")

def valid_length(length):
    try:
        ilength = int(length)

        if ilength < 4 or ilength > 128:
            raise argparse.ArgumentTypeError("The length of the password that can be generated is between 4 and 128")
        else:
            return ilength
    except ValueError:
        raise argparse.ArgumentTypeError(f"Invalid value passed as length {length}")

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Generate a password for your convienience")

    parser.add_argument("length", type=valid_length, help="Length of password")

    args = parser.parse_args()
    print(args.length)

    try:
        generate_password(parser.parse_args().length)
    except Exception as e:
        print("An exception has occured: " + e)