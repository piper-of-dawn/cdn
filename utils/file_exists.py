import os
from difflib import get_close_matches

def check_file_exists(folder, filename):
    files = os.listdir(folder)
    if filename in files:
        return True, []
    else:
        suggestions = get_close_matches(filename, files, n=3, cutoff=0.6)
        return False, suggestions

# Example usage
folder = "path/to/folder"
filename = "example.txt"
exists, suggestions = check_file_exists(folder, filename)
if exists:
    print(f"File '{filename}' exists.")
else:
    print(f"File '{filename}' not found.")
    if suggestions:
        print("Did you mean:", ", ".join(suggestions))
