import PySimpleGUI as sg

'''
This program accounts for equations in the format of:
ax + b = cx + d
'''

# define the layout of the GUI
layout = [
    [sg.Text("Enter values:")],
    [sg.Input(key='a'), sg.Text("x + "), sg.Input(key='b'), sg.Text("= "), sg.Input(key='c'), sg.Text("x + "), sg.Input(key='d'), ],
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
        left_x_term = float(values['a'])
        left_non_x_term = float(values['b'])
        right_x_term = float(values['c'])
        right_non_x_term = float(values['d'])

        # calculate
        # combine like terms
        combined_x_term = left_x_term - right_x_term
        combined_non_x_term = right_non_x_term - left_non_x_term

        # divide
        result = combined_non_x_term / combined_x_term
    

        # show result
        sg.popup(result)

        # clear input fields
        window['a'].update('')
        window['b'].update('')
        window['c'].update('')
        window['d'].update('')

# close window
window.close()