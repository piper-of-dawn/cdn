import os

def add_commit_push():
   
    # Stage the changes
    os.system('git pull')
    os.system('git add .')

    # Commit the changes
    os.system('git commit -m "Usual commit"')
    
    # Push the changes to the remote repository
    os.system('git push origin main')

add_commit_push()
