#!/usr/bin/python3
"""Entry point of the command interpreter"""


import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage

class_list = {
        'BaseModel': BaseModel
        }


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
        elif line not in class_list:
            print("** class doesn't exist **")
        else:
            instance = class_list[line]()
            instance.save()
            print(instance.id)

    def do_show(self, line):
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in class_list:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            try:
                instance = storage.all()[f"{args[0]}.{args[1]}"]
                print(instance)
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in class_list:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            try:
                del(storage.all()[f"{args[0]}.{args[1]}"])
                storage.save()
            except KeyError:
                print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances"""
        all_instances = storage.all()
        class_instances = []

        if line and not line in class_list:
                print("** class doesn't exist **")
                return False
        else:
            for instance in all_instances.values():
                if line:
                    if instance.__class__.__name__ == line:
                        class_instances.append(str(instance))
                else:
                    class_instances.append(str(instance))
        print(class_instances)

    def do_update(self, line):
        """Updates an instance based on class name and id"""





    def help_show(self):
        print('\n'.join(["Prints the string representation of an instance",
                "based on class name and id"]))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
