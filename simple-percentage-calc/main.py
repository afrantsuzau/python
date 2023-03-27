# Simple console percentage calculator
def input_float(message):
    while True:
        value = input(message)
        try:
            float(value)
        except ValueError:
            print("Please enter a valid number. Try again.")
        else:
            return float(value)

value = input_float("Enter value: ")
total_value = input_float("Enter total value: ")

def calculate_percentage(total_value, value):
    try :
        return (float(value) / float(total_value)) * 100
    except ZeroDivisionError:
        print("Total value cannot be zero.")
        exit()
        
print(f"{value} is {calculate_percentage(total_value, value)}% of {total_value}")
