import types


class JsonSerializer:

    def dumps(self, obj):
        if isinstance(obj, bool):
            return str(obj).lower()
        elif isinstance(obj, int | float):
            return str(obj)
        elif isinstance(obj, str):
            return f'"{obj}"'
        elif isinstance(obj, list):
            result = ", ".join([self.dumps(i) for i in obj])
            return f"[{result}]"
        elif isinstance(obj, tuple):
            return '{"tuple": ' + f"{self.dumps(list(obj))}" + "}"
        elif isinstance(obj, set):
            return '{"set": ' + f"{self.dumps(list(obj))}" + "}"
        elif isinstance(obj, frozenset):
            return '{"frozenset": ' + f"{self.dumps(list(obj))}" + "}"
        elif isinstance(obj, dict):
            result = ", ".join([f"{self.dumps(i)}: {self.dumps(obj[i])}" for i in obj.keys()])
            return "{" + result + "}"
        elif isinstance(obj, types.FunctionType):
            return '{"function": ' + f'["{obj.__closure__}", "{obj.__code__}", "{obj.__defaults__}", ' \
                                     f'"{obj.__dict__}", "{obj.__doc__}", "{obj.__globals__}", "{obj.__name__}"]' + "}"
        else:
            return "null"

    def loads(self, string: str):
        if string.isnumeric():
            return float(string)
        elif string[0] == '"' or string[0] == "'":
            return string.strip('"\'')
        elif string == "true" or string == "false":
            return string == "true"
        elif string == "null":
            return
        elif string[0] == '[':  # for list
            elements = string[1:-1].split(", ")
            return [self.loads(i) for i in elements]
        elif string[0] == '{':  # for dict
            return self._get_dict(string[1:-1].split(": "))

    def _get_dict(self, string):
        try:
            if string[0] == '"set"':
                return set(self.loads(string[1]))
            elif string[0] == '"tuple"':
                return tuple(self.loads(string[1]))
            elif string[0] == '"frozenset"':
                return frozenset(self.loads(string[1]))
            elif string[0] == '"function"':
                return
        except TypeError:
            return {self.loads(string[0]): self.loads(string[1])}
        return {self.loads(string[0]): self.loads(string[1])}