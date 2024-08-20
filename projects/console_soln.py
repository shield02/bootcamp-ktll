#!/usr/bin/python3
"""
A module to be used a command prompt for
the running the entire application
"""
import cmd
from shlex import split
from . import storage


class AirBNBCommand(cmd.Cmd):
    """
    The cmd is a Python module for creating a program
    that serve as a command line interpreter.
    """
    intro = "Welcome to the AirBNB command program"
    prompt = "(airbnb) >>> "
    __classes = {"BaseModel",}

    def do_quit(self, line):
        return True
    
    def do_EOF(self, line):
        exit()
    
    def do_emptyline(self, line):
        pass

    def do_create(self, line):
        """ Creates a new instance of BaseModel, save it, and print id."""
        args = split(line, " ")
        if not line:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            obj = eval(args[0])()
            obj.save()
            print(obj.id)
    
    def do_show(self, line):
        """Prints the string representation of an instance."""
        args = split(line, " ")
        if not line:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            objs = storage.all()
            if key in objs:
                print(key)
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on classname and id."""
        args = split(line, " ")
        if not line:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            objs = storage.all()
            if key in objs:
                del objs[key]
            else:
                print("** no instance found **")

    def do_all(self, line):
        """Print all string representation of instance."""
        try:
            args = split(line, " ")
            if args[0] not in self.__classes:
                raise NameError()
            
            obj = storage.all(eval(args[0]))
            for key in obj:
                print(obj[key].__str__())
        except NameError:
            print("** class doesn't exist **")

    def do_update(self, line):
        pass

if __name__ == "__main__":
    AirBNBCommand().cmdloop()
