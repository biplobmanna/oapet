import prompt
import search
import open_editor

# Start with displaying a prompt to take input
# search_str = prompt.show_search_prompt()

# Take arguments from the command line instead
import sys
arg_list = sys.argv
arg_list.pop(0)
arg_list_str = ""
for arg in arg_list:
    # print(arg)
    arg_list_str = arg_list_str + arg
search_str = arg_list_str.strip()

# Perform Fuzzy Search & get the list of matches
search_matches = search.search_projects(search_str)

# Show the list & get choice
choice = prompt.choose_options_prompt(search_matches)

# Open the choice in your favourite editor
open_editor.open_project_in_editor(search_matches[choice - 1])