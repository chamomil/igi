import unittest
from serializer import Serializer
import json


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
        test_frozenset = frozenset([34.9, 56.1])
        test_dict = {"another thing": test_list}
        self.assertEqual(test_list, json_ser.loads(json_ser.dumps(test_list)))
        self.assertEqual(test_tuple, json_ser.loads(json_ser.dumps(test_tuple)))
        self.assertEqual(test_set, json_ser.loads(json_ser.dumps(test_set)))
        self.assertEqual(test_frozenset, json_ser.loads(json_ser.dumps(test_frozenset)))
        self.assertEqual(test_dict, json_ser.loads(json_ser.dumps(test_dict)))


if __name__ == '__main__':
    unittest.main()
