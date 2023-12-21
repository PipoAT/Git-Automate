import subprocess
import PySimpleGUI as sg

# Set up the layout
layout = [
    [sg.Text('Local Folder:'), sg.Input(key='folder'), sg.FolderBrowse()],
    [sg.Text('Name of new branch:'), sg.Input(key='branch')],
    [sg.Button('Create Branch')]
]

# create the window
window = sg.Window('Git Branch Automation', layout)

while True:
    # Obtain folder from user input
    event, values = window.read()

    # When the user closes the window, exit the GUI
    if event == sg.WINDOW_CLOSED:
        break

    if event == "Create Branch":
        # obtain the local folder for init
        local_folder = values['folder']

        # obtain the branch name
        branch_name = values['branch']

        # set up the branch
        subprocess.call(['git', 'checkout', '-b', branch_name], cwd=local_folder)

        # push the branch to remote
        subprocess.call(['git', 'push', '--set-upstream', 'origin', branch_name], cwd=local_folder)

        # display popup indicating success
        sg.popup('Branch created!')

        # clear the fields for new entry from user
        window['folder'].update('')
        window['branch'].update('')



# close window
window.close()
