import numpy as np
import scipy.stats as stats
import pandas as pd

def compute_stats(series: pd.Series, name: str):
    stats_dict = {
        'Name': name,
        'Minimum': np.min(series),
        'Q1': series.quantile(0.25),
        'Median': np.median(series),
        'Q3': series.quantile(0.75),
        'Maximum': np.max(series),
        'Range': np.ptp(series),
        'Mean': np.mean(series),
        'Standard deviation': np.std(series),
        'Sum': np.sum(series),
        'Coefficient of variation': stats.variation(series),
        'Median Absolute Deviation': stats.median_abs_deviation(series),
        'Kurtosis': stats.kurtosis(series),
        'Skewness': stats.skew(series)
    }    
    return stats_dict
