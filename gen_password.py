import secrets
import string
import argparse

def generate_password(length, use_symbols=False):
    characters = string.ascii_letters + string.digits
    if use_symbols:
        characters += string.punctuation
    password = "".join(secrets.choice(characters) for _ in range(length))
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
    
    parser = argparse.ArgumentParser(
        description="""
        Generate a password for your convienience.

        Generate your secure password of 8 characters simply by running: python gen_password.py
        
        Examples:
            python gen_password.py --length 12 -l
            python gen_password.py -- symbols -s
        """,
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument(
        "--length", "-l",
        type=valid_length,
        default=8, 
        help="Length of password"
    )
    parser.add_argument(
        "--symbols", "-s",
        action="store_true",
        help="Include symbols on your password"
    )

    arguments = parser.parse_args()
    print(arguments.symbols)
    try:
        generate_password(arguments.length, arguments.symbols)
    except Exception as e:
        print("An exception has occured: " + e)
