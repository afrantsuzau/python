import PySimpleGUI as sg
from modules import notebook

label = sg.Text("Type in a new note", font=("Helvetica", 25))
input_field = sg.InputText(tooltip="Enter the note", key = "note")
add_button = sg.Button("Add")
exit_button = sg.Button("Exit", button_color=("white", "red"))
list_box = sg.Listbox(values=notebook.list(), size=[60, 10], key = "list", enable_events=True)
edit_button = sg.Button("Edit")

window = sg.Window('Simple Notebook',
                    layout = [
                        [label],
                        [input_field, add_button],
                        [list_box, edit_button],
                        [exit_button]
                    ],
                    font = ("Helvetica", 15)
                  )

while True:
  event, values = window.read()
  print("Event:", event, "Values:", values)
  match event:
    case "Add":
      notebook.append(note=values["note"])
    case "Exit" | sg.WIN_CLOSED:
      break
    
window.close()