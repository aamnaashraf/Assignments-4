import random
import string
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def print_colored(text, color):
    """Prints text in the specified color."""
    print(color + text + Style.RESET_ALL)

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    """Generates a random password based on user preferences."""
    characters = ""
    if use_letters:
        characters += string.ascii_letters  # Adds uppercase and lowercase letters
    if use_numbers:
        characters += string.digits  # Adds numbers (0-9)
    if use_symbols:
        characters += string.punctuation  # Adds symbols (!, @, #, etc.)

    if not characters:
        print_colored("Error: You must select at least one character type!", Fore.RED)
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_generator():
    print_colored("Welcome to the Password Generator! 🔐", Fore.CYAN)
    print_colored("Let's create a strong and secure password for you.", Fore.LIGHTYELLOW_EX)

    try:
        # Get password length
        length = int(input("\nEnter the length of the password (e.g., 12): "))
        if length < 4:
            print_colored("Password length should be at least 4 characters.", Fore.RED)
            return

        # Get character types
        print("\nSelect character types to include in the password:")
        use_letters = input("Include letters? (y/n): ").strip().lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

        # Generate password
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        if password:
            print_colored("\nYour generated password is:", Fore.LIGHTGREEN_EX)
            print_colored(password, Fore.LIGHTBLUE_EX + Style.BRIGHT)
            print_colored("\nKeep it safe and secure! 😊", Fore.LIGHTMAGENTA_EX)

    except ValueError:
        print_colored("Invalid input! Please enter a valid number for password length.", Fore.RED)

# Run the password generator
password_generator()