import cmd

from tools.files import pwd, ls, cd, find, search, tree
from tools.file_ops import mkdir, touch, rm,cat,cp,mv


def handle(cmd, command):
    if cmd == "pwd":
        print(pwd())
        return True

    if cmd == "ls":
        print(ls())
        return True

    if cmd == "cd":
        print(cd("~"))
        return True

    if cmd.startswith("cd "):
        print(cd(command[3:].strip()))
        return True

    if cmd.startswith("find "):
        print(find(command[5:].strip()))
        return True

    if cmd.startswith("mkdir "):
        print(mkdir(command[6:].strip()))
        return True

    if cmd.startswith("touch "):
        print(touch(command[6:].strip()))
        return True

    if cmd.startswith("rm "):
        print(rm(command[3:].strip()))
        return True

    if cmd.startswith("cat "):
        print(cat(command[4:].strip()))
        return True
    
    if cmd.startswith("cp "):
        parts = command.split(maxsplit=2)

        if len(parts) != 3:
            print("Usage: cp <source> <destination>")
            return True

        print(cp(parts[1], parts[2]))
        return True
    
    if cmd.startswith("mv "):
        parts = command.split(maxsplit=2)

        if len(parts) != 3:
            print("Usage: mv <source> <destination>")
            return True

        print(mv(parts[1], parts[2]))
        return True

    


    if cmd == "tree":
        tree()
        return True

    if cmd.startswith("tree "):
        tree(command[5:].strip())
        return True
    
    
    
    if cmd.startswith("search "):
        parts = command.split(maxsplit=2)

        if len(parts) == 2:
            print(search(parts[1]))
            return True

        if len(parts) == 3:
            print(search(parts[2], parts[1]))
            return True
    
    return False