import functools
import time


# template
def decor(func):
    @functools.wraps(func)
    def wr_decor(*args, **kwargs):
        # do something before
        value = func(*args, **kwargs)
        return value
    return wr_decor


def timer(func):
    """Print the runtime of the function"""
    @functools.wraps(func)
    def wr_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        run_time = time.perf_counter() - start_time
        print(f'Finished {func.__name__!r} in {run_time:.4f} sec')
        return value
    return wr_timer

