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

import os

def rename_files(directory):
    for filename in os.listdir(directory):
        # Check if the file name starts with alphanumeric ID_
        if filename.startswith("ID_"):
            # Extract the alphanumeric ID_
            id_part = filename.split('_', 1)[1]
            
            # Construct the new file name
            new_filename = os.path.join(directory, id_part)
            
            # Rename the file
            os.rename(os.path.join(directory, filename), new_filename)
            
            print(f'Renamed: {filename} to {id_part}')

# Replace 'path/to/your/files' with the actual path
directory_path = 'path/to/your/files'
rename_files(directory_path)

from scipy import stats
import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt
np.random.seed(1)

n = 20

sample_data = np.random.normal(loc=0, scale=8, size=n)



def gaussian_with_zero_mean(sigma):
    nll = -np.sum(stats.norm.logpdf(sample_data, loc=0, scale=sigma))
    return nll


initParams = [0, 1]

results = minimize(gaussian_with_zero_mean, initParams, method='Nelder-Mead')
print(results.x)
