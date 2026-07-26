from tools.storage import find_large_files


def handle(cmd, command):

    if cmd == "find large files":
        print(find_large_files())
        return True

    if cmd.startswith("find large files "):
        args = command.split()[3:]

        if len(args) == 1:
            arg = args[0]

            if arg.upper().endswith(("KB", "MB", "GB", "TB")):
                print(find_large_files(minimum=arg))
            else:
                print(find_large_files(directory=arg))

            return True

        if len(args) >= 2:
            print(find_large_files(args[0], args[1]))
            return True

    return False