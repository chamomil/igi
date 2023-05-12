import json
from serializer import Serializer


def main():
    json_ser = Serializer().get_serializer("json")
    val = "abc"
    b = json_ser.dumps(val)
    print(b)
    d = json_ser.loads(b)
    print(d)
    a = json.dumps(val)
    print(a)
    c = json.loads(a)
    print(c)



if __name__ == '__main__':
    main()
