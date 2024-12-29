import time

from lawson.common.utils.utils import get_time_now


def measure_execution_time(logger):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            execution_time = end_time - start_time
            logger.info(
                f"[{get_time_now()}] function {func.__name__} took {execution_time:.4f} seconds to execute"
            )
            return result

        return wrapper

    return decorator
