# Print Capitalized Names
names = ["john smith", "jay santi", "eva kuki"]
capitalized_names = [name.title() for name in names]
for name in capitalized_names:
    print(name)

# Print strings length
usernames = ["john 1990", "alberta1970", "magnola2000"]

for username in usernames:
    print(f"{username} has {len(username)} characters")
    
# Print sum of numbers
def sum_numbers(numbers):
    total = 0
    for number in numbers:
        total += float(number)
    return total

user_entries = ['10', '19.1', '20']

print(sum_numbers(user_entries))

