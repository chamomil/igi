
from makarenko_serializer.encoder import Encoder

def ed(obj):
    return Encoder.decode(Encoder.encode(obj))

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
    enc = Encoder.encode(top_level())
    print(enc)
    dec = Encoder.decode(enc)
    print(dec.__closure__[0].cell_contents)
    dec()
    print(dec)

main()
