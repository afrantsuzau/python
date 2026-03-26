def password_validator(password):
    """Check if the password is strong enough."""
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    return True

def print_green(message):
    """Print green text."""
    print(f"\033[92m{message}\033[0m")

def print_red(message):
    """Print red text."""
    print(f"\033[91m{message}\033[0m")
  
print_green("Welcome to the Password Validator app!")
input = input("Please enter a password to validate:")

if password_validator(input):
    print_green("Your password is strong enough!")
else:
    print_red("Your password is quite weak!")