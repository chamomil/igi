import json
import types

from serializer import Serializer


def func():
    print("hello")


def main():
    json_ser = Serializer().get_serializer("json")
    val = func
    k = val.__code__
    print(type(k))
    b = json_ser.dumps(val)
    print(b)
    # d = json_ser.loads(b)
    # print(d)
    # a = json.dumps(val)
    # print(a)
    # c = json.loads(a)
    # print(c)


if __name__ == '__main__':
    main()
