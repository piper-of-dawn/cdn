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
