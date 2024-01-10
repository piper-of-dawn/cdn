from datetime import datetime, timedelta

def convert_date_format(input_date):
    # Convert the input date string to a datetime object
    date_obj = datetime.strptime(input_date, '%Y%m')

    # Find the last day of the month
    last_day_of_month = (date_obj.replace(day=1) + timedelta(days=32)).replace(day=1) - timedelta(days=1)

    # Convert the date to the desired format "DDMMYYYY"
    output_date = last_day_of_month.strftime('%d%m%Y')

    return output_date
    
import os
import pandas as pd
from datetime import datetime

def save_dataframes_to_parquet(dataframes, directory_path):
    """
    Save a list of dataframes to Parquet files in a directory with timestamped filenames.

    Parameters:
    - dataframes (list): List of pandas DataFrames to be saved.
    - directory_path (str): Path to the directory where the files will be saved.

    Returns:
    - None
    """
    # Create a timestamp in the format DDMMYYYY_HHMM
    timestamp = datetime.now().strftime("%d%m%Y_%H%M")
    
    # Create a new directory with the timestamp
    new_directory = os.path.join(directory_path, timestamp)
    os.makedirs(new_directory, exist_ok=True)

    # Save each dataframe to a Parquet file with timestamped filename
    for idx, df in enumerate(dataframes):
        filename = f"dataframe_{idx}_{timestamp}.parquet"
        filepath = os.path.join(new_directory, filename)
        df.to_parquet(filepath)
        print(f"DataFrame {idx} saved to {filepath}")

# Example usage:
# Assuming 'dataframes' is a list containing your pandas DataFrames,
# and 'output_directory' is the path where you want to save the files.
# save_dataframes_to_parquet(dataframes, output_directory)
