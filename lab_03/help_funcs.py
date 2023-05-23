import inspect


def get_class(func):
    clas = getattr(inspect.getmodule(func),
                   func.__qualname__.split(".<locals>", 1)[0].rsplit(".", 1)[0])
    if isinstance(clas, type):
        return clas


def is_iterable(obj):
    return (
        hasattr(obj, "__iter__")
        and hasattr(obj, "__next__")
        and callable(obj.__iter__)
        and obj.__iter__() is obj
    )
