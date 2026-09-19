from commands import files, apps, system
from commands import organizer
from commands import storage

HELP_TEXT = """
...
"""


def handle(command):
    print(f"Debug: '{command}'")
    command = command.strip()
    cmd = command.lower()

    if cmd == "help":
        print(HELP_TEXT)
        return

    if storage.handle(cmd, command):
        return

    if files.handle(cmd, command):
        return

    if apps.handle(cmd, command):
        return

    if system.handle(cmd, command):
        return

    if organizer.handle(cmd, command):
        return

    print(f"Unknown command: {command}")
    print("Type 'help' to see available commands.")