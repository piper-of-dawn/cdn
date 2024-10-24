import os

def rename_files(directory_path):
    # Get the list of files in the directory
    files = os.listdir(directory_path)

    # Iterate through each file
    for file_name in files:
        # Check if the file name starts with "P0000_"
        if file_name.startswith("P0000_"):
            # Construct the new file name by replacing "P0000_" with your desired prefix
            new_file_name = file_name.replace("P0000_", "NEW_PREFIX_")

            # Construct the full path for both old and new file names
            old_path = os.path.join(directory_path, file_name)
            new_path = os.path.join(directory_path, new_file_name)

            # Rename the file
            os.rename(old_path, new_path)

            print(f'Renamed: {old_path} to {new_path}')

# Replace 'your_directory_path' with the actual path to your directory containing the files
directory_path = 'your_directory_path'
rename_files(directory_path)
