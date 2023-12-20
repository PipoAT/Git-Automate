import subprocess
import PySimpleGUI as sg

# Set up the layout
layout = [
    [sg.Text('Local Folder:'), sg.Input(key='folder'), sg.FolderBrowse()],
    [sg.Text('Remote Repo:'), sg.Input(key='remote')],
    [sg.Button('Initialize')]
]

# Set up the window
window = sg.Window('Git Automation', layout)

while True:
    # Obtain folder from user input
    event, values = window.read()

    # When the user closes the window, exit the GUI
    if event == sg.WINDOW_CLOSED:
        break

    if event == 'Initialize':
        # obtain the local folder for init
        local_folder = values['folder']

        # obtain the remote repo
        remote_url = values['remote']

        # initialize the local Git repo
        subprocess.call(['git', 'init'], cwd=local_folder)

        # add all files from the local Git repo
        subprocess.call(['git', 'add', '-A'], cwd=local_folder)

        # commit all files from local Git repo
        subprocess.call(['git', 'commit', '-m', 'Project init'], cwd=local_folder)

        # set branch to main
        subprocess.call(['git', 'branch', '-M', 'main'], cwd=local_folder)

        # add the remote repo
        subprocess.call(['git', 'remote', 'add', 'origin', remote_url], cwd=local_folder)

        # push to the remote repo
        subprocess.call(['git', 'push', '-u', 'origin', 'main'], cwd=local_folder)

        # display popup indicating success
        sg.popup('Repository initialized successfully!')

        # clear the fields for new entry from user
        window['folder'].update('')
        window['remote'].update('')

# Close the window on user exit
window.close()
