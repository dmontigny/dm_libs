"""This module contains custom debugging helpers"""

import functools
import time


# template from https://realpython.com/lessons/debugging-code-decorators/
def decor(func):
    @functools.wraps(func)
    def wr_decor(*args, **kwargs):
        # do something before
        value = func(*args, **kwargs)
        # do something after
        return value
    return wr_decor


def fix_csv(func):
    """Remove spaces from csv values and use Python engine"""
    @functools.wraps(func)
    def wr_fix_csv(*args, **kwargs):
        # do something before
        value = func(*args, **kwargs)
        # do something after
        return value
    return wr_fix_csv


# from https://realpython.com/lessons/debugging-code-decorators/
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


# from https://realpython.com/lessons/debugging-code-decorators/
def debug(func):
    """Print the function signature and the return value"""
    @functools.wraps(func)
    def wr_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f'{k}={v!r}' for k, v in kwargs.items()]
        signature = ', '.join(args_repr + kwargs_repr)
        print(f'Calling {func.__name__}({signature}')
        value = func(*args, **kwargs)
        print(f'{func.__name__!r} returned {value!r}')
        return value
    return wr_debug


def slowdown(func):
    """Sleep 1 second before calling func"""
    @functools.wraps(func)
    def wr_slowdown(*args, **kwargs):
        time.sleep(1)
        value = func(*args, **kwargs)
        return value
    return wr_slowdown
