import time
from typing import Callable, Any


def measure_execution(func: Callable, *args: Any, **kwargs: Any) -> dict:
    """
    Measures the execution time of a given function.

    Args:
        func (Callable): The function to measure.
        *args (Any): Positional arguments to pass to the function.
        **kwargs (Any): Keyword arguments to pass to the function.

    Returns:
        dict: Contains the result of the function and the execution time.
    """
    start_time = time.time()
    result = func(*args, **kwargs)  # Call the function with args and kwargs
    end_time = time.time() - start_time
    return {
        "result": result,
        "response_time": end_time,  # Keep as float for precision
    }
