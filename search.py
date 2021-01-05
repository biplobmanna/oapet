# Get the project_path
from config_manager import FOLDER_PATH

# READ only folders in Project Directory
from os import listdir
from os.path import isdir, join
projects = [
    name 
    for name in listdir(FOLDER_PATH) 
        if isdir(join(FOLDER_PATH, name))
]

# Setup Fuzzy Search
from fuzzysearch import find_near_matches as fnm


def search_projects(search_str=""):
    """
        return matched project names sorted by match-level
        if no search input given
        return all names
    """
    # if empty search string, return all
    if not search_str:
        return projects 
    # List which will contain the matches -- 2D list
    # ['matched_project_name', 'len_of_matched_substr']
    near_matches = []

    # iterate through all the folders & apply fuzzy search
    for project in projects:
        matched_result = fnm(search_str, project, max_l_dist=2)
        if matched_result:
            near_matches.append([project, len(matched_result[0].matched)])
    
    near_matches.sort(reverse=True, key=lambda matches: matches[1])
    return [matches[0] for matches in near_matches]