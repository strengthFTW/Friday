from tools.system import (
    cpu_usage,
    ram_usage,
    disk_usage,
    battery,
    uptime,
    health,
)

COMMANDS = {
    "cpu": cpu_usage,
    "ram": ram_usage,
    "disk": disk_usage,
    "battery": battery,
    "uptime": uptime,
    "health": health,
}


def handle(cmd, command):
    if cmd in COMMANDS:
        print(COMMANDS[cmd]())
        return True

    return False