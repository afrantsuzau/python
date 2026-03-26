import PySimpleGUI as sg
import converter as c

enter_feet_text = sg.Text("Enter the feet")
enter_feet_input = sg.InputText(tooltip="Enter the feet", default_text="0")

enter_inches_text = sg.Text("Enter the inches")
enter_inches_input = sg.InputText(tooltip="Enter the inches", default_text="0")

result_text = sg.Text("Result")
result_value = sg.Text("", key="result")

convert_button = sg.Button("Convert")

layout = [
  [enter_feet_text, enter_feet_input], 
  [enter_inches_text, enter_inches_input], 
  [convert_button], 
  [result_text, result_value]
]

window = sg.Window("GUI Convertor", layout=layout, font=("Helvetica", 15))

while True:
  event, values = window.read()
  print("Event:", event, "Values:", values)
  match event:
    case "Convert":
      feet = int(values[0])
      inches = int(values[1])
      result_value = c.convert_to_meters(feet, inches)
      window["result"].update(value=f"{result_value}")
    case sg.WIN_CLOSED:
      break

window.close()