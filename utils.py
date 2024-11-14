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

import os
import markdown

import os
import markdown
from markdown.extensions.toc import TocExtension
from markdown.extensions.tables import TableExtension
from markdown.extensions.math import MathExtension

def convert_markdown_to_html(file_path):
    """
    Converts a Markdown file to HTML and saves it with the same file name.
    Supports Markdown tables and LaTeX expressions.
    
    Parameters:
    file_path (str): Path to the Markdown file
    """
    # Read the Markdown file
    with open(file_path, 'r') as file:
        markdown_content = file.read()
    
    # Configure Markdown extensions
    extensions = [
        TocExtension(),
        TableExtension(),
        MathExtension(enable_dollar_delimiter=True)
    ]
    
    # Convert Markdown to HTML
    html_content = markdown.markdown(markdown_content, extensions=extensions)
    
    # Determine the output file path
    output_file_path = os.path.splitext(file_path)[0] + '.html'
    
    # Save the HTML file
    with open(output_file_path, 'w') as file:
        file.write(html_content)
    
    print(f"Markdown file '{os.path.basename(file_path)}' converted to HTML and saved as '{os.path.basename(output_file_path)}'.")

