import types
from serializer import Serializer


def func(string="hello"):
    def text():
        print(string)
    return text


def main():
    json_ser = Serializer().get_serializer("json")
    val = func
    txt = func("hello")
    k = txt.__name__
    print(k)
    print(type(k))
    # b = json_ser.dumps(val)
    # print(b)
    # d = json_ser.loads(b)
    # print(d)


if __name__ == '__main__':
    main()
