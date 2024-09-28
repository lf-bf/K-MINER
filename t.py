import json
import PySimpleGUI as sg


file = {"item 1": [{"name": "title 1"}, {"name": "title 2"}], "item 2": [{"name": "title 3"}, {"name": "title 4"}]}


layout = [[sg.Text('items'), sg.Combo(list(file.keys()), enable_events=True, key='some_key', size=(30, 0))],  # there must be items
          [sg.Text('titles'), sg.Combo([], key='other_key', size=(30, 0))]]  # there must be values of selected item
window = sg.Window('testing', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event =='some_key':
        item = values[event]
        title_list = [i["name"] for i in file[item]]
        window['other_key'].update(value=title_list[0], values=title_list)

window.close()

print(type(file))