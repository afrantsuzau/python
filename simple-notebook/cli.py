# Description: A simple console notebook app.
from modules import console, notebook

console.print_greetings("Welcome to the Simple Console Notebook app!")
console.print_help()

while True:
    user_option = input("\nEnter an option: ").strip().lower()
    if user_option.startswith("add"):
        notebook.append(note=console.get_note(user_option))
    elif user_option.startswith("list"):
        notebook.list()
    elif user_option.startswith("delete"):
        if console.int_validator(console.get_note_index(user_option)):
          notebook.delete(note_index=console.get_note_index(user_option))
        else:
          console.print_error("Invalid value for index. Please try again.")
    elif user_option.startswith("edit"):
        if console.int_validator(console.get_note_index(user_option)):
          note_input = input("Enter a note: ")
          notebook.edit(note_index=console.get_note_index(user_option), note=note_input)
        else:
          console.print_error("Invalid value for index. Please try again.")
    elif user_option.startswith("help"):
        console.print_help()
    elif user_option.startswith("exit") or user_option.startswith("quit"):
        break
    else:
        console.print_error("Invalid option. Please try again.")
