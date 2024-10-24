import numpy as np

def weighted_average(array, weights):
    """
    Calculate the weighted average of a NumPy array with given weights.

    Parameters:
    array (np.ndarray): The input array.
    weights (np.ndarray): The weights vector.

    Returns:
    float: The weighted average.
    """
    array = np.asarray(array)
    weights = np.asarray(weights)
    
    # Normalize weights
    normalized_weights = weights / np.sum(weights)
    
    return np.sum(array * normalized_weights)


import json
from tabulate import tabulate

def json_to_markdown_table(file_path):
    # Read the JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    # Extract the keys and values
    headers = list(data.keys())
    values = [list(data.values())]
    
    # Create the markdown table using tabulate
    markdown_table = tabulate(values, headers, tablefmt="github")
    
    return markdown_table

from rapidfuzz import process

def find_nearest_match(input_str, candidates):
    """
    Find the nearest matching string from an iterable of strings.
    
    Args:
    input_str (str): The input string to match.
    candidates (iterable): An iterable of candidate strings.
    
    Returns:
    str: The string from the iterable that best matches the input string.
    """
    # Find the best match using rapidfuzz's process.extractOne
    match, score, _ = process.extractOne(input_str, candidates)
    
    return match

