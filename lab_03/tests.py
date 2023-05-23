import math
import unittest
from serializer import Serializer
import json


def return_5():
    return 5


def recursion(x):
    if x < 2:
        return 1

    return recursion(x - 1) * x


def square(value):
    return value * value


def sqrt(value):
    return math.sqrt(value)


def function_use_return_5():
    return return_5()


GLOBAL_VAR = 10


def function_use_global_value():
    return GLOBAL_VAR


# ------------------------classes----------------------

class ClassWithValue:
    a = 1


class ClassWithStaticAndClassMethods:
    b = 4

    @staticmethod
    def test_static():
        return 5

    @classmethod
    def test_class(cls):
        return cls.b

    _temperature = 5

    @property
    def temperature(self):
        return self._temperature


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



class MyTestCase(unittest.TestCase):
    def test_primitives(self):
        json_ser = Serializer().get_serializer("json")
        self.assertEqual(json.dumps(18), json_ser.dumps(18))
        self.assertEqual(json.dumps(18.5), json_ser.dumps(18.5))
        self.assertEqual(json.dumps(False), json_ser.dumps(False))
        self.assertEqual(json.dumps("hello"), json_ser.dumps("hello"))
        self.assertEqual(json.dumps(None), json_ser.dumps(None))

    def test_collections(self):
        json_ser = Serializer().get_serializer("json")
        test_list = [1, 2, 3]
        test_tuple = ("jjj", "kkkk")
        test_set = {True, False}
        test_dict = {"another thing": test_list, "hello": [23, 22]}
        test_frozenset = frozenset([33, 65])
        self.assertEqual(test_list, json_ser.loads(json_ser.dumps(test_list)))
        self.assertEqual(test_tuple, json_ser.loads(json_ser.dumps(test_tuple)))
        self.assertEqual(test_set, json_ser.loads(json_ser.dumps(test_set)))
        self.assertEqual(test_frozenset, json_ser.loads(json_ser.dumps(test_frozenset)))
        self.assertEqual(test_dict, json_ser.loads(json_ser.dumps(test_dict)))

    def test_funcs(self):
        json_ser = Serializer().get_serializer("json")
        self.assertEqual(return_5(), json_ser.loads(json_ser.dumps(return_5))())
        self.assertEqual(recursion(1), json_ser.loads(json_ser.dumps(recursion))(1))
        self.assertEqual(square(1), json_ser.loads(json_ser.dumps(square))(1))
        self.assertEqual(sqrt(1), json_ser.loads(json_ser.dumps(sqrt))(1))
        self.assertEqual(function_use_return_5(), json_ser.loads(json_ser.dumps(function_use_return_5))())
        self.assertEqual(function_use_global_value(), json_ser.loads(json_ser.dumps(function_use_global_value))())

    def test_class(self):
        json_ser = Serializer().get_serializer("json")
        self.assertEqual(ClassWithValue.a, json_ser.loads(json_ser.dumps(ClassWithValue)).a)
        self.assertEqual(ClassWithStaticAndClassMethods.test_static(), json_ser.loads(
            json_ser.dumps(ClassWithStaticAndClassMethods)).test_static())
        self.assertEqual(ClassWithStaticAndClassMethods.test_class(), json_ser.loads(
            json_ser.dumps(ClassWithStaticAndClassMethods)).test_class())
        self.assertEqual(ClassWithStaticAndClassMethods().temperature, json_ser.loads(
            json_ser.dumps(ClassWithStaticAndClassMethods))().temperature)
        self.assertEqual(ClassC().method_a(), json_ser.loads(json_ser.dumps(ClassC))().method_a())
        self.assertEqual(ClassC().method_b(), json_ser.loads(json_ser.dumps(ClassC))().method_b())
        self.assertEqual(ClassC().method_a(), json_ser.loads(json_ser.dumps(ClassC())).method_a())


if __name__ == '__main__':
    unittest.main()
