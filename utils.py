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

# Example usage:
array = np.array([1, 2, 3, 4])
weights = np.array([0.1, 0.2, 0.3, 0.4])
print(weighted_average(array, weights))  # Output should be 3.0
