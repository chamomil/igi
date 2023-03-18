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
            command_text = input("Enter a command:\n\t")
            commands = command_text.split(' ')

            if commands[0] == "add":
                commands.pop(0)
                self._storage.add(commands)
                print("Successfully added arguments to storage")

            elif commands[0] == "remove":
                try:
                    self._storage.remove(commands[1])
                    print("Successfully removed argument from storage")
                except:
                    print("No such element in storage")

            elif commands[0] == "find":
                commands.pop(0)

                for key in commands:
                    if self._storage.find(key):
                        print(key)
                    else:
                        print(f"No such key as {key}")

            elif commands[0] == "list":
                list_all = self._storage.list_all()

                if len(list_all) == 0:
                    print("Storage is empty")
                else:
                    print(list_all)

            elif commands[0] == "grep":
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
                    print("Regular expression is incorrect")
