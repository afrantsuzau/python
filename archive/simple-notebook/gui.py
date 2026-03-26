import PySimpleGUI as sg
import time
import os
from modules import notebook

images_path = os.path.dirname(__file__) + "/images/"

sg.theme("DarkAmber")

label = sg.Text("Type in a new note", font=("Helvetica", 25))
clock = sg.Text("", key="clock")
input_field = sg.InputText(tooltip="Enter the note", key="note")
add_button = sg.Button(tooltip="Add new note", image_source=images_path +
                       "add.png", size=2, mouseover_colors=("White"), key="Add")
exit_button = sg.Button("Exit", button_color=("white", "red"), key="Exit")
list_box = sg.Listbox(values=notebook.list(), size=[
                      60, 10], key="list", enable_events=True)
edit_button = sg.Button("Edit", key="Edit")
delete_button = sg.Button("", image_source=images_path +
                          "delete.png", size=2, mouseover_colors=("White"), key="Delete")

layout = [
    [sg.Column([[label], [clock]])],
    [sg.Column([[input_field, add_button]])],
    [sg.Column([[list_box, edit_button, delete_button]])],
    [exit_button]
]

window = sg.Window('Simple Notebook',
                   layout=layout,
                   font=("Helvetica", 15)
                   )

while True:
  event, values = window.read(timeout=250)
  window["clock"].update(time.strftime("%d/%m/%Y %H:%M:%S"))
  print("Event:", event, "Values:", values)
  match event:
    case "Add":
      notebook.append(note=values["note"])
      window['list'].update(values=notebook.list())
    case "Edit":
      try:
        notebook.edit(note_index=notebook.find_index(
            values["list"][0]), note=values["note"])
        window['list'].update(values=notebook.list())
      except IndexError:
        sg.popup("Please select a note to edit",
                 title="Error", font=("Helvetica", 20))
    case "Delete":
      try:
        notebook.delete(note_index=notebook.find_index(values["list"][0]))
        window['list'].update(values=notebook.list())
        window["note"].update(value="")
      except IndexError:
        sg.popup("Please select a note to delete",
                 title="Error", font=("Helvetica", 20))
    case "list":
      window["note"].update(values["list"][0])
    case "Exit" | sg.WIN_CLOSED:
      break

window.close()
