# Friday — Linux Terminal Assistant

Friday is a lightweight command-line assistant for Linux with an interactive `Friday >` interface for system monitoring, file management, storage utilities, and launching applications.

![Friday Linux Assistant Demo](./assets/Demo.gif)

## Installation

```bash
git clone <repository-url>
cd friday

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

Run Friday with Python:

```bash
python3 friday.py
```

Or make the script executable to run directly from the Linux terminal:

```bash
chmod +x friday
./friday
```

## Usage

```text
$ ./friday
Friday > health
Friday > disk
Friday > clean downloads
Friday > open firefox
```

Enter commands at the `Friday >` prompt.

## Commands

| Category | Commands |
| :--- | :--- |
| System | `health`, `cpu`, `ram`, `disk`, `battery`, `uptime` |
| Files | `pwd`, `ls`, `cd`, `tree`, `cat`, `mkdir`, `touch`, `cp`, `mv`, `rm`, `find`, `search` |
| Utilities | `find large files`, `clean downloads`, `open <app>` |

## Structure

```text
friday/
├── friday.py
├── friday
├── router.py
├── commands/
├── tools/
└── requirements.txt
```

## Requirements

Linux, Python 3, Bash.

## License

MIT
