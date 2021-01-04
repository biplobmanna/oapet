# Read the config files & parse for input
import configparser
configparser = configparser.ConfigParser()
config_file_path = r'.config'
configparser.read(config_file_path)

# GLOBAL CONSTANTS to be accessed everywhere
FOLDER_PATH = configparser.get('GENERAL', 'FOLDER_PATH')
EDITOR = configparser.get('GENERAL', 'EDITOR')