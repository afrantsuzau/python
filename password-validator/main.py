# Strong password validator tool
def password_validator(password):
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    return True
  
print("Welcome to the Password Validator app!")
input = input("Please enter a password to validate:")

if password_validator(input):
    print("Your password is strong enough!")
else:
    print("Your password is invalid!")