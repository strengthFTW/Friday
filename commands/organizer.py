from tools.organizer import clean_downloads


def handle(cmd, command):

    if cmd == "clean downloads":
        print(clean_downloads())
        return True

    return False