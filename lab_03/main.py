import types
from serializer import Serializer


def function(string=(12, 11)):

    def text(num=12):
        print(string)
        print(num)

        def text2(num=12):
            print(string)
            print(num)
        return text2
    return text


def main():
    json_ser = Serializer().get_serializer("json")
    val = {"hello": 2, "hi": 3}
    txt = function()()
    # print(txt.__qualname__)
    # print(type(txt.__code__))
    b = json_ser.dumps(txt)
    print(b)
    d = json_ser.loads(b)
    d()


if __name__ == '__main__':
    main()
