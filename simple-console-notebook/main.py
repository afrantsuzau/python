notebook_path = "files/notes.txt"

def print_help():
    print("Welcome to the Simple Console Notebook app!")
    print("1. [Add] a note")
    print("2. [List] all notes")
    print("3. [Delete] a note")
    print("4. [Edit] a note")
    print("5. [Help] (Print this menu)")
    print("6. [Exit]")

print_help()

while True:
    user_option = input("\nEnter an option: ").strip().lower()

    if user_option.startswith("add"):
        try:
          user_option.split(' ')[1]
        except:
          note_input = input("Enter a note: ")
        else:
          note_input = user_option.split(' ')[1]
        with open(notebook_path, "a") as file:
            file.writelines(note_input + "\n")
    elif user_option.startswith("list"):
        notes_humanized = []
        with open(notebook_path, "r") as file:
            notes = file.readlines()
            for index, note in enumerate(notes):
                note = note.strip('\n')
                notes_humanized.append(f"#{index + 1}. {note}")
                print(f"#{index + 1}: {note}")
    elif user_option.startswith("delete"):
        try:
          user_option.split(' ')[1]
        except:
          note_index = int(input("Enter a note number: ")) - 1
        else:
          note_index = int(user_option.split(' ')[1]) - 1
        with open(notebook_path, "r+") as file:
            lines = file.readlines()
            del lines[note_index]
            file.seek(0)
            file.truncate()
            file.writelines(lines)
    elif user_option.startswith("edit"):
        try:
          user_option.split(' ')[1]
        except:
          note_index = int(input("Enter a note number: ")) - 1
        else:
          note_index = int(user_option.split(' ')[1]) - 1
        note_input = input("Enter a note: ")
        with open(notebook_path, "r+") as file:
            lines = file.readlines()
            for index, line in enumerate(lines):
                if index == note_index:
                    lines[index] = note_input + "\n"
            file.seek(0)
            file.writelines(lines)
        file.close()
    elif user_option.startswith("help"):
        print_help()
    elif user_option.startswith("exit") or user_option.startswith("quit"):
        break
    else:
        print("Invalid option. Please try again.")
