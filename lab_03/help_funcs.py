import inspect


def get_class(func):
    clas = getattr(inspect.getmodule(func),
                   func.__qualname__.split(".<locals>", 1)[0].rsplit(".", 1)[0])
    if isinstance(clas, type):
        return clas
