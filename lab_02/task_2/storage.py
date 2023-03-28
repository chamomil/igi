import re
import pickle


class Storage:
    __username: str
    __set_of_elements: set

    def set_username(self, username):
        self.__username = username
        self.__set_of_elements = set()

    def get_username(self):
        return self.__username

    def add(self, keys):
        for key in keys:
            self.__set_of_elements.add(key)

    def remove(self, keys):
        for key in keys:
            if self.find(key):
                self.__set_of_elements.remove(key)

    def find(self, key):
        return self.__set_of_elements.__contains__(key)

    def list_all(self):
        return self.__set_of_elements

    def grep(self, regex):
        set_of_found = []
        for element in self.__set_of_elements:
            matching = re.findall(regex, element)
            if len(matching) != 0:
                set_of_found.append(element)
        return set_of_found

    def save(self):
        path = self.__username + ".pkl"
        with open(path, 'wb') as file:
            pickle.dump(self.__set_of_elements, file)

    def load(self):
        path = self.__username + ".pkl"
        with open(path, 'rb') as file:
            self.__set_of_elements = self.__set_of_elements | pickle.load(file)
