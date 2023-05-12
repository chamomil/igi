class JsonSerializer:
    @staticmethod
    def dumps(obj):
        if isinstance(obj, bool):
            return str(obj).lower()
        elif isinstance(obj, int | float):
            return str(obj)
        elif isinstance(obj, str):
            return '"' + obj + '"'
        else:
            return str(obj)

    @staticmethod
    def loads(string: str):
        if string.isnumeric():
            return float(string)
        elif string[0] == '"':
            return string.replace('"', '')
        else:
            return bool(string)