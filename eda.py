import numpy as np
from scipy.stats import skew, kurtosis
from tabulate import tabulate

def summarize_array(arr):
    stats = {
        "Mean": np.mean(arr),
        "Std Dev": np.std(arr),
        "Skewness": skew(arr),
        "Kurtosis": kurtosis(arr),
        "Median": np.median(arr),
        "Q5": np.percentile(arr, 5),
        "Q25": np.percentile(arr, 25),
        "Q50": np.percentile(arr, 50),
        "Q75": np.percentile(arr, 75),
        "Q95": np.percentile(arr, 95),
        "Q99.9": np.percentile(arr, 99.9),
        "Minimum": np.min(arr),
        "Maximum": np.max(arr),
        "Range": np.ptp(arr),
        "Sum": np.sum(arr)
    }
    
    # Rounding the statistics to 4 decimal places
    stats = {key: round(value, 4) for key, value in stats.items()}
    
    # Preparing data for tabulation
    table = [[key, value] for key, value in stats.items()]
    
    # Generating the tabulated string
    tabulated_str = tabulate(table, headers=["Statistic", "Value"], tablefmt="grid")
    
    return tabulated_str
def summarize_multiple_arrays(arrays_dict):
    # Initialize the header and table list
    headers = ["Statistic"]
    table = []
    
    # List of statistics to calculate
    stats_names = [
        "Mean", "Std Dev", "Skewness", "Kurtosis", "Median",
        "Q5", "Q25", "Q50", "Q75", "Q95", "Q99.9",
        "Minimum", "Maximum", "Range", "Sum"
    ]
    
    # Calculate statistics for each array
    for name, arr in arrays_dict.items():
        headers.append(name)
        stats = {
            "Mean": np.mean(arr),
            "Std Dev": np.std(arr),
            "Skewness": skew(arr),
            "Kurtosis": kurtosis(arr),
            "Median": np.median(arr),
            "Q5": np.percentile(arr, 5),
            "Q25": np.percentile(arr, 25),
            "Q50": np.percentile(arr, 50),
            "Q75": np.percentile(arr, 75),
            "Q95": np.percentile(arr, 95),
            "Q99.9": np.percentile(arr, 99.9),
            "Minimum": np.min(arr),
            "Maximum": np.max(arr),
            "Range": np.ptp(arr),
            "Sum": np.sum(arr)
        }
        
        # Round the statistics to 4 decimal places
        stats = {key: round(value, 4) for key, value in stats.items()}
        
        # Add statistics to the table
        if not table:  # Initialize table with statistics names
            table = [[stat] for stat in stats_names]
        
        for i, stat in enumerate(stats_names):
            table[i].append(stats[stat])
    
    # Generating the tabulated string
    tabulated_str = tabulate(table, headers=headers, tablefmt="grid")
    
    return tabulated_str
