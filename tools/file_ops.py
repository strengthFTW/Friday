from pathlib import Path

def mkdir(dirname):
    try:
        Path(dirname).expanduser().mkdir(parents=True, exist_ok=True)
        return f"Created directory: {dirname}"
    except Exception as e:
        return str(e)
    
def touch(filename):
    try:
        Path(filename).expanduser().touch(exist_ok=True)
        return f"Created file: {filename}"
    except Exception as e:
        return str(e)
    
def rm(filename):
    try:
        Path(filename).expanduser().unlink()
        return f"Deleted {filename}"
    except Exception as e:
        return str(e)
    
def cat(filename):
    try:
        path = Path(filename).expanduser()

        if not path.exists():
            return "File not found."

        if path.is_dir():
            return "That's a directory."

        return path.read_text()

    except Exception as e:
        return str(e)

import shutil
from pathlib import Path

def cp(src, dst):
    try:
        shutil.copy2(
            Path(src).expanduser(),
            Path(dst).expanduser()
        )
        return "Copied successfully."
    except Exception as e:
        return str(e)
    
def mv(src, dst):
    try:
        shutil.move(
            str(Path(src).expanduser()),
            str(Path(dst).expanduser())
        )
        return "Moved successfully."
    except Exception as e:
        return str(e)