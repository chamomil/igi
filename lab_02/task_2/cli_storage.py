from storage import Storage
import re


class CliStorage:  # class to build interaction between storage and terminal
    _storage: Storage

    def __init__(self):
        self._storage = Storage()

    def run(self):
        self.set_username()
        self.command()

    def set_username(self):
        username = input("Enter username: ")
        self._storage.set_username(username)

    def command(self):
        while True:
            command_text = input("\n\tEnter a command: ")
            commands = re.findall(r'\b\w+\b', command_text)

            if commands[0] == "add":
                self.add_handler(commands)
            elif commands[0] == "remove":
                self.remove_handler(commands)
            elif commands[0] == "find":
                self.find_handler(commands)
            elif commands[0] == "list":
                self.list_handler()
            elif commands[0] == "grep":
                self.grep_handler(commands)
            elif commands[0] == "save":
                self.save_handler()
            elif commands[0] == "load":
                self.load_handler()
            elif commands[0] == "switch":
                self.run()
            elif commands[0] == "exit":
                return
            else:
                print("Wrong command")

    def add_handler(self, commands):
        if len(commands) == 0:
            print("Error: no arguments in command 'add'")
        else:
            self._storage.add(commands)
            print("Successfully added arguments to storage")

    def remove_handler(self, commands):
        commands.pop(0)
        if len(commands) == 0:
            print("Error: no arguments in command 'remove'")

        try:
            self._storage.remove(commands)
            print("Successfully removed argument from storage")
        except:
            print("No such element in storage")

    def find_handler(self, commands):
        commands.pop(0)
        if len(commands) == 0:
            print("Error: no arguments in command 'find'")

        for key in commands:
            if self._storage.find(key):
                print(key)
            else:
                print(f"No such key as {key}")

    def list_handler(self):
        list_all = self._storage.list_all()

        if len(list_all) == 0:
            print("Storage is empty")
        else:
            print(list_all)

    def grep_handler(self, commands):
        commands.pop(0)
        regex = "".join(commands)

        try:
            list_of_found = self._storage.grep(regex)
            if len(list_of_found) == 0:
                print("No such elements")
            else:
                for element in list_of_found:
                    print(element)
        except:
            print("Regular expression is incorrect or absent")

    def save_handler(self):
        self._storage.save()
        print("Successfully saved")

    def load_handler(self):
        try:
            self._storage.load()
            print("Successfully loaded")
        except:
            print("Error, no saved data for this user")
