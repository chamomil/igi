import re


class Storage:
    __username: str
    __set_of_elements: set

    def set_username(self, username):
        self.__username = username
        self.__set_of_elements = set()

    def add(self, keys):
        for key in keys:
            self.__set_of_elements.add(key)

    def remove(self, key):
        self.__set_of_elements.remove(key)

    def find(self, key):
        return self.__set_of_elements.__contains__(key)

    def list_all(self):
        return self.__set_of_elements

    def grep(self, regex):
        set_of_found = list(self.__set_of_elements.copy())
        for element in set_of_found:
            matching = re.findall(regex, element)
            if len(matching) is 0:
                set_of_found.remove(element)
                set_of_found.append("No such element")
            else:
                set_of_found.remove(element)
                for m in matching:
                    set_of_found.append(m)
        return set_of_found
