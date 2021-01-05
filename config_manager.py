# Bring packages onto path
from sys import path as syspath
from pathlib import Path
syspath.append(Path(__file__).parent.absolute())

# Read the config files & parse for input
import configparser
configparser = configparser.ConfigParser()
config_file_path = str(Path(__file__).parent.absolute()) + "/.config"
configparser.read(config_file_path)

# GLOBAL CONSTANTS to be accessed everywhere
FOLDER_PATH = configparser.get('GENERAL', 'FOLDER_PATH')
EDITOR = configparser.get('GENERAL', 'EDITOR')