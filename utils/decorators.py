import time
import functools


def _timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        begin = time.perf_counter_ns()
        func(*args, **kwargs)
        end = time.perf_counter_ns()
        print(f"Time to solve: {end - begin: .0f} ns")
    return wrapper