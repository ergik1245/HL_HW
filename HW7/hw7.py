import functools


def shout(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper


def positive_only(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)) or isinstance(arg, bool):
                raise ValueError(f"Аргумент {arg!r} має бути додатним числом")
            if arg <= 0:
                raise ValueError(f"Аргумент {arg!r} має бути додатним числом")
        return func(*args, **kwargs)
    return wrapper