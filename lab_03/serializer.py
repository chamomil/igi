from json_serializer import JsonSerializer


class Serializer:
    @staticmethod
    def get_serializer(answer):
        if answer == "json":
            return JsonSerializer()
        else:
            raise ValueError("Incorrect input of serializer's type")
