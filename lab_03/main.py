
from makarenko_serializer.serializer import Serializer

def top_level():
    a = 10

    def closure():
        nonlocal a
        a += 1
        return a

    return closure

def double_result(func):
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        return value * 2

    return wrapper


@double_result
def doubled():
    return 5


def main():
    ser = Serializer.create_serializer("json")
    print (ser.dumps({"hello": 23, "efwf": 86}))

main()
