import base64
import builtins
import types

from lab_03.constants import TYPE, UNSERIALIZABLE_CODE_TYPES
from lab_03.help_funcs import get_class


class Encoder:

    @classmethod
    def encode(cls, obj):
        if isinstance(obj, bool | int | float | str):
            return obj
        elif isinstance(obj, list):
            return type(obj)((cls.encode(item) for item in obj))
        elif isinstance(obj, tuple | set | frozenset):
            return dict(__type=type(obj).__name__.lower(), data=[cls.encode(item) for item in obj])
        elif isinstance(obj, dict):
            return {key: cls.encode(value) for key, value in obj.items()}
        elif isinstance(obj, types.FunctionType | types.MethodType):
            return cls._func_encode(obj)
        elif isinstance(obj, types.CodeType):
            attrs = [attributes for attributes in dir(obj) if attributes.startswith("co")]
            data = {attr: cls.encode(getattr(obj, attr)) for attr in attrs if attr not in
                    UNSERIALIZABLE_CODE_TYPES}
            return dict(__type=TYPE.CODE, data=data)
        elif isinstance(obj, types.CellType):
            return dict(__type=TYPE.CELL, data=cls.encode(obj.cell_contents))
        elif isinstance(obj, types.ModuleType):
            return dict(__type=TYPE.MODULE, data=obj.__name__)
        elif isinstance(obj, bytes):
            return dict(__type=TYPE.BYTES, data=base64.b64encode(obj).decode("ascii"))

    @classmethod
    def decode(cls, obj):
        if isinstance(obj, list):
            return [cls.decode(element) for element in obj]
        elif isinstance(obj, dict):
            obj_type = obj.get("__type")

            if obj_type is None:
                return {key: cls.decode(val) for key, val in obj.items()}
            elif obj_type in (TYPE.TUPLE, TYPE.SET, TYPE.FROZENSET):
                data = obj.get("data")
                collection = getattr(builtins, obj.get("__type").lower())
                return collection((cls.decode(item) for item in data))
            elif obj_type == TYPE.FUNCTION:
                return cls._get_func(obj)
            elif obj_type == TYPE.CELL:
                return (lambda: cls.decode(obj.get("data"))).__closure__[0]
            elif obj_type == TYPE.CODE:
                return cls._get_code(obj)
            elif obj_type == TYPE.MODULE:
                return __import__(obj.get("data"))
            elif obj_type == TYPE.BYTES:
                return base64.b64decode(obj.get("data").encode("ascii"))

        return obj

    @classmethod
    def _func_encode(cls, obj):
        fclass = get_class(obj)
        closure = (tuple(cell for cell in obj.__closure__ if cell.cell_contents is not fclass)
                   if obj.__closure__ is not None
                   else tuple())
        globs = {
            key: cls.encode(value)
            for (key, value) in obj.__globals__.items()
            if key in obj.__code__.co_names
               and value is not fclass
               and key != obj.__code__.co_name
        }

        function = cls.encode(dict(
            code=obj.__code__,
            name=obj.__name__,
            argdefs=obj.__defaults__,
            closure=closure,
            fdict=obj.__dict__,
            globals=globs,
        ))
        return dict(__type=TYPE.FUNCTION, data=function, is_method=isinstance(obj, types.MethodType))

    @classmethod
    def _get_func(cls, obj):
        func = cls.decode(obj.get("data"))
        fdict = func.pop("fdict")
        result = types.FunctionType(**func)
        result.__dict__.update(fdict)
        result.__globals__.update({result.__name__: result})
        return result

    @classmethod
    def _get_code(cls, obj):
        def f():
            pass

        code_dict = cls.decode(obj.get("data"))
        return f.__code__.replace(**code_dict)
