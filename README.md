# Arch Update Manager

**Arch Update Manager** is a lightweight Python CLI tool designed to help Arch Linux users **check for updates** and **upgrade packages** with ease. It explores automation, safe update handling, and command-line workflow design.

---

Disclaimer: This repository is part of a personal study initiative.
The implementation focuses on exploring concepts and experimenting with techniques, and it should not be considered production-ready software.

## Features

- ✅ Check for available package updates (official repos + AUR via `yay`)  
- ✅ Upgrade all packages automatically (`--noconfirm` for unattended upgrades)  
- ✅ Smart default: `archupdate` runs a check and prompts for upgrade if updates exist  
- ✅ Output options: human-readable table or JSON  

---

## Installation

> Recommended: using [pipx](https://pipxproject.github.io/pipx/) to keep the CLI isolated from system Python.

sudo pacman -S python-pipx
pipx install --editable .

---

## Project Structure

- `cli.py` → main CLI logic  
- `updater.py` → interacts with yay, performs upgrades  
- `parser.py` → parses yay output  
- `__init__.py` → package initializer

