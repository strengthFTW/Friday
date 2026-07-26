#!/usr/bin/env python3
from rich.console import Console
from rich.panel import Panel

console = Console()

console.print(
    Panel.fit(
        "[bold cyan]Friday[/bold cyan]\nYour Linux Assistant",
        border_style="cyan",
    )
)
from router import handle


def main():

    while True:
        command = input("Friday > ")

        if command.lower() == "exit":
            print("Goodbye!")
            break

        handle(command)


if __name__ == "__main__":
    main()
    
    