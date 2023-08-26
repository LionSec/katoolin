# katoolin3
Automatically install all Kali linux tools

> Now works on arch linux!

# How does it work?
[![asciicast](https://asciinema.org/a/o1YteA16HrSGzDL8p9cFsV6hf.svg)](https://asciinema.org/a/o1YteA16HrSGzDL8p9cFsV6hf)

# Features
- Add Kali/Archstrike linux repositories
- Remove Kali/Archstrike repositories
- Install Kali/Archstrike linux tools

# Dependences
### Using executable:
- You dont need any dependence

### Using virtual environment for development:
| derived from debian | derived from arch linux |
| --- | --- |
| python3             | python                  |
| python3-poetry      | python-poetry           |
| git                 | git                     |

# Download:
### Using executable from releases:
- Download here: [releases](https://github.com/b166erbot/katoolin/releases)
### Using git for development:
- ```mkdir ~/git && cd ~/git```
- ```git clone https://github.com/b166erbot/katoolin```

# How to run
### Using Executable:
> Set execute permission once:
- Give the file execute permission: ```chmod +x katoolin3```
> Run:
- sudo ./katoolin3

### Using virtual environment for development:
> Activate the virtual environment and run:
1. runs once: ```poetry install```
2. ```poetry shell```
3. ```sudo `which python3` katoolin3.py```

# Usage
1. Install the repository (automatically installs for your distribution).
2. Select the programs you want and click in install button.
3. Uninstall the repositories to not crash your sistem.

# Bugs?

- [go to the issues tab and report](https://github.com/b166erbot/katoolin/issues)
