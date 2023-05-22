import builtins
import types
from constants import TYPE


class JsonSerializer:

    @classmethod
    def dumps(cls, obj):
        if isinstance(obj, bool):
            return str(obj).lower()
        elif isinstance(obj, int | float):
            return str(obj)
        elif isinstance(obj, str | types.CellType):
            return f'"{obj}"'
        elif isinstance(obj, list):
            return f"[{', '.join([cls.dumps(i) for i in obj])}]"
        elif isinstance(obj, tuple | set | frozenset):
            return cls.dumps(dict(__type=type(obj).__name__.lower(), data=list(obj)))
        elif isinstance(obj, dict):
            result = ", ".join([f'"{key}": {cls.dumps(value)}' for key, value in obj.items()])
            return f'{{{result}}}'
        elif isinstance(obj, types.FunctionType):
            func_dict = '{"function": {"closure": ' + f'{cls.dumps(obj.__closure__)}, "code": ' \
                                                      f'{cls.dumps(obj.__code__)}' + "}}"
            return func_dict
        elif isinstance(obj, types.CodeType):
            attrs = [attributes for attributes in dir(obj) if attributes.startswith("co")]
            return cls.dumps({attr: cls.dumps(getattr(obj, attr)) for attr in attrs})
        else:
            return "null"

    @classmethod
    def loads(cls, string: str):
        return cls._get_instances(cls._loads(string, 0)[0])

    @classmethod
    def _loads(cls, string: str, start):
        if string[start] == '"':
            return cls._get_str(string, start)
        elif string[start].isdigit() or string[start] == '-':
            return cls._get_num(string, start)
        elif string[start] == "t" or string[start] == "f":
            return cls._get_bool(string, start)
        elif string[start] == "n":
            return None, start + 4
        elif string[start] == '[':  # for list
            return cls._get_list(string, start)
        elif string[0] == '{':  # for dict
            return cls._get_dict(string, start)
        else:
            return string

    @staticmethod
    def _get_str(string, start):
        end = start + 1
        while string[end] != '"':
            end += 1
        return string[start + 1: end], end + 1

    @staticmethod
    def _get_num(string, start):
        end = start + 1
        while len(string) > end and (string[end].isdigit() or string[end] == "."):
            end += 1

        num = string[start:end]
        if num.count("."):
            return float(num), end
        return int(num), end

    @staticmethod
    def _get_bool(string, start):
        result = string[start] == "t"
        num_of_letters = 5
        if result:
            num_of_letters = 4
        return result, start + num_of_letters

    @classmethod
    def _get_list(cls, string: str, start):
        end = cls._count_braces(string, start + 1, ('[', ']'))
        arr = []
        index = start + 1

        while index < end - 2:  # end is start for the next part
            while string[index].startswith((' ', ',', '\n')):
                index += 1
            res, index = cls._loads(string, index)
            arr.append(res)

        return arr, end

    @classmethod
    def _get_dict(cls, string: str, start):
        end = cls._count_braces(string, start + 1, ('{', '}'))
        index = start + 1
        result = dict()

        while index < end - 2:
            while string[index].startswith((' ', ',', '\n')):
                index += 1
            key, index = cls._get_str(string, index)

            while string[index].startswith((' ', ',', '\n', ':')):
                index += 1
            value, index = cls._loads(string, index)
            result[key] = value
        return result, end

    @staticmethod
    def _count_braces(string, index, braces_type):
        braces_count = 1
        while braces_count:
            if string[index] == braces_type[0]:
                braces_count += 1
            if string[index] == braces_type[1]:
                braces_count -= 1
            index += 1

        if index == len(string):
            index += 1
        return index

    @classmethod
    def _get_instances(cls, obj):
        if isinstance(obj, list):
            return [cls._get_instances(element) for element in obj]
        elif isinstance(obj, dict):
            obj_type = obj.get("__type")

            if obj_type is None:
                return {key: cls._get_instances(val) for key, val in obj.items()}
            elif obj_type in (TYPE.TUPLE, TYPE.SET, TYPE.FROZENSET):
                data = obj.get("data")
                collection = getattr(builtins, obj.get("__type").lower())
                return collection((cls._get_instances(item) for item in data))

        return obj
