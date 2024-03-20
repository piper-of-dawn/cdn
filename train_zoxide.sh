#!/bin/bash

# Function to visit folders recursively
visit_folder() {
    local folder="$1"
    # Check if the argument is a directory
    if [ -d "$folder" ]; then
        # Loop through each item in the directory
        for item in "$folder"/*; do
            if [ -d "$item" ]; then
                echo "Entering folder: $item"
                # Change directory into the folder
                cd "$item" || exit
                # Recursive call to visit subfolders
                visit_folder "$item"
                # Change back to the parent directory after visiting subfolders
                cd ..
            fi
        done
    fi
}

# Start visiting from /mnt/
visit_folder "/mnt/"
