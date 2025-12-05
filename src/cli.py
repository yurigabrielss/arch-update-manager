import argparse
import json
from .updater import run_yay_updates
from .parser import parse_updates

def main():
    parser = argparse.ArgumentParser(description="ArchSecure Update Manager")
    sub = parser.add_subparsers(dest="command")

    parser_check = sub.add_parser("check", help="Check for available updates")
    parser_check.add_argument(
        "--json",
        action="store_true",
        help="Output results in JSON format"
    )

    sub.add_parser("upgrade", help="Upgrade packages (not implemented yet)")

    args = parser.parse_args()

    if args.command == "check":
        text = run_yay_updates()
        pkgs = parse_updates(text)

        if getattr(args, "json", False):
            print(json.dumps(pkgs, indent=4, ensure_ascii=False))
        else:
            print_table(pkgs)

    elif args.command == "upgrade":
        print("Upgrade não implementado ainda.")
    else:
        parser.print_help()

def print_table(pkgs):

    RED = "\033[31m"
    GREEN = "\033[32m"
    BLUE = "\033[34m"
    WHITE = "\033[37m"
    RESET = "\033[0m"


    if not pkgs:
        print("No updates available.")
        return

    print("Package".ljust(20), "Old".ljust(15), "New".ljust(15))
    print("-" * 50)

    for p in pkgs:
        pkg_color = WHITE + p["pkg"] + RESET
        old_color = RED + p["old"] + RESET
        arrow = BLUE + "→" + RESET
        new_color = GREEN + p["new"] + RESET

        print(
            pkg_color.ljust(20 + 9),
            old_color.ljust(15 + 9),
            arrow,
            new_color
        )

