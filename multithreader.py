from concurrent.futures import ThreadPoolExecutor
from typing import Callable, Any
import time
import os
from itertools import islice

def chunk_iterable(iterable, n):
    """
    Chunks an iterable into smaller iterables of n elements.

    Args:
        iterable: The input iterable.
        n: The desired size of each chunk.

    Returns:
        A generator yielding iterables, where each has at most n elements.  Returns an empty generator if the input is empty.

    """
    it = iter(iterable)
    while True:
        chunk = list(islice(it, n))
        if not chunk:
            return
        yield chunk
        

NUM_CORES = os.cpu_count()
print(f"Number of CPU cores: {NUM_CORES}")
def timeit(func):
    """
    A simple decorator to measure the execution time of a function.
    """
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"Execution time of {func.__name__}: {elapsed_time:.6f} seconds")
        return result
    return wrapper

class ThreadPool:
    def __init__(self, num_threads: int):
        """
        Initialize the thread pool with the specified number of threads.
        """
        self.executor = ThreadPoolExecutor(max_workers=NUM_CORES-1)

    def submit(self, func: Callable, *args: Any, **kwargs: Any):
        """
        Submit a function with its arguments to the thread pool.

        Args:
            func (Callable): The function to execute.
            *args (Any): Positional arguments for the function.
            **kwargs (Any): Keyword arguments for the function.

        Returns:
            concurrent.futures.Future: A future representing the result of the computation.
        """
        return self.executor.submit(func, *args, **kwargs)

    def shutdown(self, wait: bool = True):
        """
        Shutdown the thread pool, optionally waiting for tasks to complete.

        Args:
            wait (bool): If True, wait for all running tasks to finish before shutting down.
        """
        self.executor.shutdown(wait=wait)


@timeit
def main():

    def example_task(a, b):
        print(f"Adding {a} and {b}")
        for _ in range(1_000_000):
            pass
        return a + b
    # Create a thread pool with 4 threads
    pool = ThreadPool(num_threads=4)

    # Submit tasks to the pool
    futures = [
        pool.submit(example_task, i, i + 1) for i in range(10)
    ]

    # Collect results
    results = [future.result() for future in futures]

    print("Results:", results)

    # Shutdown the thread pool
    pool.shutdown()

main()
