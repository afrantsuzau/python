import os

notebook_path = os.path.dirname(__file__) + "/files/notes.txt"

def append(note, file_path=notebook_path):
    """Write a note to the notebook."""
    with open(file_path, "a") as file:
        file.writelines(note + "\n")
        
def list(file_path=notebook_path):
  """List all notes in the notebook."""
  notes_humanized = []
  with open(file_path, "r") as file:
      notes = file.readlines()
      for index, note in enumerate(notes):
          note = note.strip('\n')
          notes_humanized.append(f"#{index + 1}. {note}")
          print(f"#{index + 1}: {note}")
  return notes_humanized
          
def delete(note_index, file_path=notebook_path):
    """Delete a note from the notebook."""
    with open(file_path, "r+") as file:
        lines = file.readlines()
        del lines[note_index]
        file.seek(0)
        file.truncate()
        file.writelines(lines)
        
def edit(note_index, file_path=notebook_path):
    """Edit a note in the notebook."""
    note_input = input("Enter a note: ")
    with open(file_path, "r+") as file:
        lines = file.readlines()
        for index, line in enumerate(lines):
            if index == note_index:
                lines[index] = note_input + "\n"
        file.seek(0)
        file.writelines(lines)