from pathlib import Path

UNITS = ["B", "KB", "MB", "GB", "TB"]


def format_size(size):
    unit = 0
    while size >= 1024 and unit < len(UNITS) - 1:
        size /= 1024
        unit += 1
    return f"{size:.2f} {UNITS[unit]}"


def parse_size(value):
    value = value.upper()

    if value.endswith("KB"):
        return float(value[:-2]) * 1024

    if value.endswith("MB"):
        return float(value[:-2]) * 1024**2

    if value.endswith("GB"):
        return float(value[:-2]) * 1024**3

    if value.endswith("TB"):
        return float(value[:-2]) * 1024**4

    return 100 * 1024**2  # Default: 100 MB


def find_large_files(directory="~", minimum="100MB"):
    root = Path(directory).expanduser()

    if not root.exists():
        return "Directory not found."

    minimum_size = parse_size(minimum)
    files = []

    for file in root.rglob("*"):
        if file.is_file():
            try:
                size = file.stat().st_size
                if size >= minimum_size:
                    files.append((size, file))
            except PermissionError:
                continue

    files.sort(reverse=True)

    if not files:
        return "No large files found."

    lines = []
    for size, file in files:
        lines.append(f"{format_size(size):>10}  {file}")

    return "\n".join(lines)