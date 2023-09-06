# katoolin3 🐍
Automatically install all Kali linux tools

> Now works on arch linux! 🎉🥳🎈

# Supported repositories 🐧
### debian or derived
- kali linux
- parrot
- backbox

### arch linux or derived
- blackarch
- archstrike

# Features 🛠️
- Add linux repositories based on your distribution
- Install tools

# Dependences 📦
### Using executable:
- You dont need any dependence

### Using virtual environment for development:
| derived from debian | derived from arch linux |
| --- | --- |
| python3             | python                  |
| python3-poetry      | python-poetry           |
| glibc               | libc6                   |
| git                 | git                     |

# Download 📥
### Using executable from releases:
- Download here: [releases](https://github.com/b166erbot/katoolin/releases)
### Using git for development:
- `mkdir ~/git && cd ~/git`
- `git clone https://github.com/b166erbot/katoolin`

# How to run ▶️
### Using Executable:
- Set execute permission once: `chmod +x katoolin3`
- run: `sudo ./katoolin3`

### Using virtual environment for development:
1. runs once: `poetry install`
2. `poetry shell`
3. ```sudo `which python3` katoolin3.py```

# Build the executable by yourself 📦💼
### build
> I assume you already ran the `poetry install` command
1. `poetry shell`
2. `pyinstaller main.spec`
>the executable will be in the dist folder
### execute
1. `cd dist`
2. `chmod +x katoolin3`
3. `sudo ./katoolin3`

# Usage 📋
1. Install the repositories.
2. choice one or more repositories for your distribution.
3. Select the programs you want and click in install button.
- Done!

# Bugs? 🐞

- [go to the issues tab and report](https://github.com/b166erbot/katoolin/issues)