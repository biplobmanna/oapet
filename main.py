import prompt
import search
import open_editor

# Start with displaying a prompt to take input
search_str = prompt.show_search_prompt()

# Perform Fuzzy Search & get the list of matches
search_matches = search.search_projects(search_str)

# Show the list & get choice
choice = prompt.choose_options_prompt(search_matches)

# Open the choice in your favourite editor
open_editor.open_project_in_editor(search_matches[choice - 1])