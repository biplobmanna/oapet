# Read the config files & parse for input
import configparser
configparser = configparser.ConfigParser()
config_file_path = r'.config'
configparser.read(config_file_path)

PROJECT_PATH = configparser.get('FOLDER_PATH', 'PROJECT_PATH')

# print("PROJECT_PATH = " + PROJECT_PATH)