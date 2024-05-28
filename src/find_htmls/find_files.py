import os
import fnmatch

def find_html_files(directory: str) -> list:
    "Finds all HTML and HTML5 files in the given directory and its subdirectories."

    html_files = []
    formats = ['html', 'html5']

    # List all files in the folder
    files = os.listdir(directory)

    # Print the list of files
    html_files = [file for file in files if file.split('.')[-1] in formats]

    return html_files
