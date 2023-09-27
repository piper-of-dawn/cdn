import pandas as pd
import os

def concat_csv_files_in_folder(folder_path):
    # List all CSV files in the folder
    csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

    # Initialize an empty Pandas DataFrame to store the concatenated data
    concatenated_df = pd.DataFrame()

    # Loop through each CSV file and concatenate them
    for csv_file in csv_files:
        file_path = os.path.join(folder_path, csv_file)
        df = pd.read_csv(file_path)
        concatenated_df = pd.concat([concatenated_df, df], ignore_index=True)

    return concatenated_df

# Example usage:
folder_path = '/path/to/your/csv/folder'
result_df = concat_csv_files_in_folder(folder_path)
