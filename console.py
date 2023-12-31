#!/usr/bin/python3

import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program using Ctrl+D or EOF"""
        return True

    def emptyline(self):
        """Called when an empty line is entered"""
        pass



if __name__ == '__main__':
    HBNBCommand().cmdloop()
