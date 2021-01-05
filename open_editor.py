# Bring packages onto path
from sys import path as syspath
from pathlib import Path
syspath.append(Path(__file__).parent.absolute())

from config_manager import EDITOR, FOLDER_PATH

# Running the open_cmd in Bash
from subprocess import run

def open_project_in_editor(project):
    path = FOLDER_PATH + project
    run([EDITOR, path])