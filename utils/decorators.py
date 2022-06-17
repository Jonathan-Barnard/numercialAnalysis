import time
import functools
import numpy as np


def _timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        begin = time.perf_counter_ns()
        value = func(*args, **kwargs)
        end = time.perf_counter_ns()
        print(f"Time to solve: {end - begin:.0f} ns")
        return value
    return wrapper

def _timerStatistics(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        times = []
        for _ in range(1000):
            begin = time.perf_counter_ns()
            func(*args, **kwargs)
            end = time.perf_counter_ns()
            times.append(end-begin)
        print(
            "====================\n"
            f"| {func.__name__} |\n"
            "==== Statistics ====\n\n" 
            f"Average: {np.mean(times):.0f} ns\n"
            f"Standard deviation: {np.std(times):.0f} ns\n"
            f"Maximum: {np.max(times[5:]):.0f} ns\n"
        )
    return wrapper