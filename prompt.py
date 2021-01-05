# Bring packages onto path
from sys import path as syspath
from pathlib import Path
syspath.append(Path(__file__).parent.absolute())

# Import the search function to get the list of all the files
from search import search_projects

def show_search_prompt():
    # Any other ideas for minimal-cool-project
    return input('?: ')

def choose_options_prompt(projects):
    # Uff, a new line only, eh?
    print()
    index = 1
    for project in projects:
        print("( " + str(index) + ".) " + project)
        index += 1
    try:
        choice = int(input("\nChoose: "))
        # Sanity check on choice
        if choice >= index or choice <= 0 :
            raise("Foolish choice lad...")
    except:
        # Don't you dare supply rubbish
        print("\nFoolish choice lad...\n")
        exit(0)
    return choice


# choose_options_prompt(search_projects('home'))