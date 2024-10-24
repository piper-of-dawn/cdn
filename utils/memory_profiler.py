import tracemalloc
import statistics
import functools
from tqdm import tqdm
from collections import namedtuple

MemoryStats = namedtuple('MemoryStats', ['mean', 'std_deviation'])

def measure_memory_usage(n):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            memory_differences = []

            for _ in tqdm(range(n), desc="Memory Measurement", unit="call"):
                tracemalloc.start()
                func(*args, **kwargs)
                current, peak = tracemalloc.get_traced_memory()
                tracemalloc.stop()
                memory_differences.append(peak - current)

            average_difference = statistics.mean(memory_differences)
            std_deviation = statistics.stdev(memory_differences)

            print(f"Average Memory Difference: {average_difference} bytes")
            print(f"Standard Deviation: {std_deviation} bytes")

            return MemoryStats(mean=average_difference, std_deviation=std_deviation)

        return wrapper
    return decorator

# Example usage:

@measure_memory_usage(n=5)
def example_function():
    # Your arbitrary function logic here
    for _ in tqdm(range(1000000), desc="Processing", unit="iteration"):
        _ = "a" * 10

# Call the decorated function and get the result as a named tuple
result = example_function()

# Access the mean and standard deviation
print(f"Mean: {result.mean} bytes")
print(f"Standard Deviation: {result.std_deviation} bytes")
