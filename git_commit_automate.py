import os
import subprocess
import PySimpleGUI as sg

# Set up the layout
layout = [
    [sg.Text('Select Files:'), sg.Input(key='files'), sg.FilesBrowse()],
    [sg.Text('Commit Message:'), sg.Input(key='msg')],
    [sg.Button('Commit')]
]

# create the window
window = sg.Window('Git Branch Automation', layout)

while True:
    # Obtain folder from user input
    event, values = window.read()

    # When the user closes the window, exit the GUI
    if event == sg.WINDOW_CLOSED:
        break

    if event == "Commit":
        # obtain the file paths
        file_paths = values['files'].split(';')

        # obtain the commit message
        message = values['msg']

        # add the files
        for file_path in file_paths:
            file_name = os.path.basename(file_path)
            subprocess.call(['git', 'add', file_name])

        # commit locally
        subprocess.call(['git', 'commit','-m', message]) 

        # commit to remote
        subprocess.call(['git','push'])

        # display popup indicating success
        sg.popup('Commit made!')

        # clear the fields for new entry from user
        window['files'].update('')
        window['msg'].update('')

# close window
window.close()
