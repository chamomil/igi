from storage import Storage
from pathlib import Path


class CliStorage:  # class to build interaction between storage and terminal
    _storage: Storage

    def __init__(self):
        self._storage = Storage()

    def run(self):
        self.set_username()
        self.load_last()
        self.command()

    def set_username(self):
        while True:
            username = input("Enter username: ")
            if len(username) == 0:
                print("empty input")
                continue
            break
        self._storage.set_username(username)

    def load_last(self):
        path = Path(self._storage.get_username() + '.pkl')
        if path.exists():
            answer = input("Do you wish to load data for this user? Enter 'y' to load: ")
            if answer == 'y':
                self.load_handler()

    def command(self):
        while True:
            command_text = input("\nEnter a command: ")
            commands = command_text.split(" ")
            action = commands.pop(0)
            if action == "add":
                self.add_handler(commands)
            elif action == "remove":
                self.remove_handler(commands)
            elif action == "find":
                self.find_handler(commands)
            elif action == "list":
                self.list_handler()
            elif action == "grep":
                self.grep_handler(commands)
            elif action == "save":
                self.save_handler()
            elif action == "load":
                self.load_handler()
            elif action == "switch":
                self.switch_handler()
            elif action == "help":
                self.help_handler()
            elif action == "exit":
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
        if len(commands) == 0:
            print("Error: no arguments in command 'remove'")
            return

        try:
            self._storage.remove(commands)
            print("Successfully removed argument from storage")
        except:
            print("No such element in storage")

    def find_handler(self, commands):
        if len(commands) == 0:
            print("Error: no arguments in command 'find'")
            return

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


    def switch_handler(self):
        answer = input("Do you wish to save your data before switching? Enter 'y' to save it: ")
        if answer == "y":
            self.save_handler()
        raise Exception('switched to another user')

    def help_handler(self):
        print("\tadd\t\tadds one or more elements to container")
        print("\tremove\tremoves one or more elements from container")
        print("\tfind\tfinds one or more elements in container (if the container doesn't contain such an element the\n"
              "\t\t\tinfo will be printed)")
        print("\tlist\tlists all the elements kept in container")
        print("\tgrep\tby the given regex searches for elements in container")
        print("\tsave\tsaves data to file")
        print("\tload\tloads data from file")
        print("\tswitch\tswitches to choosing another user")
        print("\texit\tstops the program")
