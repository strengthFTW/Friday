import psutil
from datetime import timedelta


def cpu_usage():
    return f"CPU Usage: {psutil.cpu_percent(interval=1)}%"


def ram_usage():
    memory = psutil.virtual_memory()
    used = memory.used / (1024 ** 3)
    total = memory.total / (1024 ** 3)

    return (
        f"RAM Usage: {memory.percent}%\n"
        f"Used: {used:.2f} GB / {total:.2f} GB"
    )


def disk_usage():
    disk = psutil.disk_usage("/")
    used = disk.used / (1024 ** 3)
    total = disk.total / (1024 ** 3)

    return (
        f"Disk Usage: {disk.percent}%\n"
        f"Used: {used:.2f} GB / {total:.2f} GB"
    )


def uptime():
    boot = psutil.boot_time()
    uptime_seconds = int(__import__("time").time() - boot)

    return f"Uptime: {timedelta(seconds=uptime_seconds)}"


def battery():
    batt = psutil.sensors_battery()

    if batt is None:
        return "Battery information not available."

    status = "Charging" if batt.power_plugged else "Discharging"

    return (
        f"Battery: {batt.percent}%\n"
        f"Status: {status}"
    )


def health():
    return "\n\n".join([
        cpu_usage(),
        ram_usage(),
        disk_usage(),
        uptime(),
        battery()
    ])