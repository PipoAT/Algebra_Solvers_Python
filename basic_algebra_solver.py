import PySimpleGUI as sg

'''
This program accounts for equations in the format of:
ax + b = c
'''

# define the layout of the GUI
layout = [
    [sg.Text("Enter values:")],
    [sg.Input(key='a'), sg.Text("x + "), sg.Input(key='b'), sg.Text("= "), sg.Input(key='c')],
    [sg.Button("Calculate"), sg.Button("Exit")]
]

# create the window
window = sg.Window("Python Algebra Calculator", layout)

while True:
    # interact with window
    event, values = window.read()

    # if user closes window or clicks exit
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

    if event == "Calculate":
        # obtain values to solve
        x_term = float(values['a'])
        non_x_term = float(values['b'])
        non_x_after_equals = float(values['c'])

        # solve like an basic algebra problem
        # move non-x terms to one side
        non_x_combined = non_x_after_equals - non_x_term

        # divide
        result = non_x_combined / x_term

        # show result
        sg.popup(result)

        # clear input fields
        window['a'].update('')
        window['b'].update('')
        window['c'].update('')

# close window
window.close()