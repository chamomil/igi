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


class ClassA:
    def __init__(self):
        super().__init__()
        self.a = 1

    def method_a(self):
        return self.a


class ClassB:
    def __init__(self):
        super().__init__()
        self.b = 2

    def method_b(self):
        return self.b


class ClassC(ClassB, ClassA):
    def __init__(self):
        super().__init__()


def main():
    xml_ser = Serializer().get_serializer("xml")
    val = ClassC
    # txt = function()()
    # print(txt.__qualname__)
    # print(type(txt.__code__))
    b = xml_ser.dumps(val)
    print(b)
    d = xml_ser.loads(b)
    print(d().method_a())


if __name__ == '__main__':
    main()
