from pathlib import Path

def pwd():
    return str(Path.cwd())


def ls():
    files = [
    f for f in Path.cwd().iterdir()
    if not f.name.startswith(".")
]

    files = sorted(
    files,
    key=lambda f: (not f.is_dir(), f.name.lower())
)
    
    


    if not files:
        return "Directory is empty."

    return "\n".join(
        f"{'📁' if f.is_dir() else '📄'} {f.name}"
        for f in files
    )


def cd(path):
    try:
        new_path = Path(path).expanduser().resolve()

        if not new_path.exists():
            return "Directory does not exist."

        if not new_path.is_dir():
            return "Not a directory."

        import os
        os.chdir(new_path)

        return f"Current directory: {new_path}"

    except Exception as e:
        return str(e)


def find(filename):
    home = Path.home()

    for file in home.rglob(filename):
        return str(file)

    return "File not found."

from pathlib import Path

def tree(path=".", prefix=""):
    path = Path(path).expanduser()

    if not path.exists():
        return "Directory does not exist."

    if not path.is_dir():
        return "Not a directory."

    print(f"📁 {path.name if path.name else path}")

    _tree(path, "")

    return ""


def _tree(directory, prefix):
    items = sorted(
        directory.iterdir(),
        key=lambda x: (not x.is_dir(), x.name.lower())
    )

    for index, item in enumerate(items):
        connector = "└── " if index == len(items) - 1 else "├── "

        icon = "📁" if item.is_dir() else "📄"

        print(prefix + connector + icon + " " + item.name)

        if item.is_dir():
            extension = "    " if index == len(items) - 1 else "│   "
            _tree(item, prefix + extension)
            

from pathlib import Path
import fnmatch


def search(pattern, directory="."):
    directory = Path(directory).expanduser()

    if not directory.exists():
        return "Directory does not exist."

    if not directory.is_dir():
        return "Not a directory."

    results = []

    for file in directory.rglob("*"):
        if fnmatch.fnmatch(file.name.lower(), pattern.lower()) or pattern.lower() in file.name.lower():
            results.append(file)

    if not results:
        return "No matching files found."

    return "\n".join(str(f) for f in results)