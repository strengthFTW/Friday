# Friday

> A simple command-line assistant for Linux systems.

**Friday** provides an interactive terminal interface (`Friday >`) to quickly check system status, manage files, clean up directories, analyze disk space, and launch applications.

---

## ⚡ Quick Start

1. **Setup Environment & Install Dependencies**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Run Friday**:
   ```bash
   python friday.py
   # Or using the shell wrapper script:
   ./friday
   ```

---

## 💡 Available Commands

### 📊 System Health & Status
- `health` – Displays overall system report (CPU, RAM, Disk, Uptime, Battery)
- `cpu` – Shows current CPU usage percentage
- `ram` – Displays total & used RAM memory
- `disk` – Displays disk usage on root partition
- `battery` – Shows battery percentage and charging state
- `uptime` – Displays system uptime

### 📁 File Management & Navigation
- `pwd` / `ls` / `cd [path]` – Inspect and change current directory
- `tree [path]` – View directory tree structure visually
- `cat <file>` – View content of a text file
- `mkdir <dir>` / `touch <file>` – Create directories or files
- `cp <src> <dest>` / `mv <src> <dest>` – Copy or move/rename files
- `rm <file>` – Remove a file
- `find <name>` – Search for a file in your home directory
- `search <pattern> [dir]` – Find files matching a pattern in a directory

### 💾 Storage & Utilities
- `find large files [dir] [size]` – Locate large files (e.g., `find large files ~ 100MB`)
- `clean downloads` – Automatically sort `~/Downloads` files into organized subfolders (Pictures, Documents, Code, etc.)
- `open <app>` – Launch a Linux application (e.g., `open firefox`)

---

## 🏗️ Project Structure

```
friday/
├── friday.py          # Interactive shell entry point
├── friday             # Executable bash launcher script
├── router.py          # Command router
├── commands/          # Command handlers (apps, files, organizer, storage, system)
├── tools/             # Low-level system and file utilities
└── requirements.txt   # Python dependencies
```
