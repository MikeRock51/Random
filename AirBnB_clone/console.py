#!/usr/bin/python3
"""Entry point of the command interpreter"""


import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Implementation of the console's commands"""

    prompt = '(hbnb) '

    def do_quit(self, line):
        """Exits the interpreter"""
        return True

    def do_EOF(self, line):
        """Exits the interpreter when it encounters EOF signal"""
        return True

    def emptyline(self):
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel"""
        if not line:
            print('** class name missing **')
        elif line != 'BaseModel':
            print("** class doesn't exist **")
        else:
            instance = BaseModel()
            instance.save()
            print(instance.id)

    def do_show(self, line):
        """


if __name__ == '__main__':
    HBNBCommand().cmdloop()
