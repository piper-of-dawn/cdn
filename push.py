import os

def add_commit_push():
    # Navigate to the project directory
    # os.chdir('C:\git\cdn')
    
    # Check if git is initialized in the project directory
    # try:
    #     with open('.git', 'r') as _:
    #         pass  # File exists, ignore it
    # except FileNotFoundError:
    #     print("Error: This doesn't appear to be a Git repository.")
    #     return
    
    # Add file board.txt
    os.system('echo "Hello World!" > board.txt')
    
    # Stage the changes
    os.system('git add .')
    
    # Commit the changes
    os.system('git commit -m "Added board.txt"')
    
    # Push the changes to the remote repository
    os.system('git push origin main')

add_commit_push()
