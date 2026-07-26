from pathlib import Path
import shutil

FILE_TYPES = {
    "Pictures": [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".webp", ".svg"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".webm"],
    "Documents": [".pdf", ".doc", ".docx", ".ppt", ".pptx", ".xls", ".xlsx", ".txt"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Audio": [".mp3", ".wav", ".flac", ".aac", ".ogg"],
    "Code": [
        ".py", ".java", ".cpp", ".c", ".h",
        ".js", ".ts", ".html", ".css",
        ".json", ".xml", ".yaml", ".yml",
        ".ipynb", ".sql"
    ],
    "Installers": [".deb", ".rpm", ".pkg", ".AppImage", ".exe", ".msi"],
}


def clean_downloads():
    downloads = Path.home() / "Downloads"

    if not downloads.exists():
        return "Downloads folder not found."

    moved = 0

    for item in downloads.iterdir():

        if item.is_dir():
            continue

        extension = item.suffix.lower()

        destination = "Others"

        for folder, extensions in FILE_TYPES.items():
            if extension in extensions:
                destination = folder
                break

        target = downloads / destination
        target.mkdir(exist_ok=True)

        shutil.move(str(item), str(target / item.name))
        moved += 1

    return f"Organized {moved} files."