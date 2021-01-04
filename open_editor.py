from config_manager import EDITOR, FOLDER_PATH

# Running the open_cmd in Bash
from subprocess import run

def open_project_in_editor(project):
    path = FOLDER_PATH + project
    run([EDITOR, path])