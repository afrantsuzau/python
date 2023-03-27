import PySimpleGUI as sg

enter_feet_text = sg.Text("Enter the feet", font=("Helvetica", 15))
enter_feet_input = sg.InputText(tooltip="Enter the feet", font=("Helvetica", 15))

enter_inches_text = sg.Text("Enter the inches", font=("Helvetica", 15))
enter_inches_input = sg.InputText(tooltip="Enter the inches", font=("Helvetica", 15))

convert_button = sg.Button("Convert", font=("Helvetica", 15))

window = sg.Window("GUI Convertor", layout=[[enter_feet_text, enter_feet_input], [enter_inches_text, enter_inches_input], [convert_button]])
window.read()
window.close()