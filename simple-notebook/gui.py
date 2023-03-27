import PySimpleGUI as sg

label = sg.Text("Type in a new note", font=("Helvetica", 25))
input_field = sg.InputText(tooltip = "Enter the note" ,font=("Helvetica", 15))
add_button = sg.Button("Add", font=("Helvetica", 15))

window = sg.Window('Simple Notebook', layout = [[label], [input_field, add_button]])
window.read()
print("Hello World!")
window.close()
