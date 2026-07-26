from tools.apps import open_app


def handle(cmd, command):
    if cmd.startswith("open "):
        app = command[5:].strip()
        print(open_app(app))
        return True

    return False