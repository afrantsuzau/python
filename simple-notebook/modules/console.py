def int_validator(input_string):
    """Validate input string as integer."""
    try:
        int(input_string)
    except ValueError:
        return False
    else:
        return True

def print_greetings(message):
    """Print greeting text in green."""
    print(f"\033[92m{message}\033[0m")
    
def print_help():
    """Print help text."""
    print("""
    Available options:
      [Add] a note
      [List] all notes
      [Delete] a note
      [Edit] a note
      [Help] (Print this menu)
      [Exit] or [Quit]
    """)

def print_error(message):
    """Print error text in red."""
    print(f"\033[91m{message}\033[0m")
    
def get_note(input_string):
    try:
        input_string.split(' ')[1]
    except:
        note = input("Enter a note: ")
    else:
        note = input_string.split(' ', 1)[1]
    return note
  
def get_note_index(input_string):
    try:
        input_string.split(' ')[1]
    except:
        note_index = int(input("Enter a note number: ")) - 1
    else:
        note_index = int(input_string.split(' ')[1]) - 1
    return note_index
  
if __name__ == "__main__":
  print_greetings("Welcome to the Simple Console Notebook app!")