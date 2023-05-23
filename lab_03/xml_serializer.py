from encoder import Encoder
import re


class XmlSerializer:
    @classmethod
    def load(cls, file):
        return cls.loads(file.read())

    @classmethod
    def dump(cls, obj, file):
        file.write(cls.dumps(obj))

    @classmethod
    def dumps(cls, obj):
        return cls._dumps(Encoder.encode(obj))

    @classmethod
    def _dumps(cls, obj):
        if isinstance(obj, int | float | bool | str | None):
            obj_type = type(obj).__name__
            return f"<{obj_type}>{obj}</{obj_type}>"
        elif isinstance(obj, list):
            return f"<list>{[cls.dumps(i) for i in obj]}</list>"
        elif isinstance(obj, dict):
            result = ", ".join([f'"{key}": {cls.dumps(value)}' for key, value in obj.items()])
            return f'{{{result}}}'
        else:
            return "<null>"

    @classmethod
    def loads(cls, string: str):
        return Encoder.decode(cls._loads(string, 0)[0])

    @classmethod
    def _loads(cls, string: str, start):
        if string.startswith("<str>"):
            return cls._get_str(string, start)
        elif string.startswith(("<int>", "<float>")):
            return cls._get_num(string, start)
        elif string.startswith("<bool>"):
            return cls._get_bool(string, start)
        elif string.startswith("<NoneType>"):
            return None, start + 25
        elif string[start] == '[':  # for list
            return cls._get_list(string, start)
        elif string[0] == '{':  # for dict
            return cls._get_dict(string, start)
        else:
            return string

    @staticmethod
    def _get_str(string, start):
        start += 5
        end = start + 1
        while string[end] != "<":
            end += 1
        return string[start:end], end + 6

    @staticmethod
    def _get_num(string, start):
        num_type = string.startswith("<int>")
        if num_type:
            start += 5
        else:
            start += 7

        end = start + 1
        while len(string) > end and (string[end].isdigit() or string[end] in ('.', '-')):
            end += 1

        num = string[start:end]
        if num_type:
            return int(num), end + 6
        return float(num), end + 8

    @staticmethod
    def _get_bool(string, start):
        start += 6
        end = start + 5
        if string[start] == "T":
            end -= 1
        result = string[start:end]
        return result == "True", end + 7

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
