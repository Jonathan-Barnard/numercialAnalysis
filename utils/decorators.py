import time
import functools
import numpy as np


def _timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        begin = time.perf_counter()
        value = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Time to solve: {end - begin:.4f} s")
        return value
    return wrapper

def _timerStatistics(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        times = []
        for _ in range(10):
            begin = time.perf_counter()
            value = func(*args, **kwargs)
            end = time.perf_counter()
            times.append(end-begin)
        print(
            "====================\n"
            f"| {func.__name__} |\n"
            "==== Statistics ====\n\n" 
            f"Average: {np.mean(times):.4f} s\n"
            f"Standard deviation: {np.std(times):.4f} s\n"
            f"Maximum: {np.max(times):.4f} s\n"
        )
        return value
    return wrapper