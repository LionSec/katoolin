# Katoolin 3

[![Licence](https://img.shields.io/badge/Licence-GNU_GPL_v2.0-blue)](https://github.com/0xGuigui/Katoolin3/blob/master/LICENCE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)

Install Kali Linux tools on your Debian/Ubuntu distribution.

## Requirements

- Python 3.10 or higher
- Debian or Ubuntu based system

## Installation

Clone the repository and run the script:

```bash
git clone https://github.com/0xGuigui/Katoolin3.git
cd Katoolin3
chmod +x katoolin3.py
sudo ./katoolin3.py
```

## Usage

Once the script is running, you can navigate using the following commands:

- **0**: Install all Kali Linux tools
- **Back**: Go back to the previous menu
- **GoHome**: Return to the main menu
- **Exit**: Close the script

*Note: As a standard behavior or this tool, installing 'armitage' will automatically install 'metasploit'.*

## Features

- Add Kali Linux repositories
- Remove Kali Linux repositories
- Install Kali Linux tools (individually or in bulk)

## Tested Systems

- Ubuntu
- Debian
- ZorinOS

## Important Note

Before performing a system update, it is highly recommended to remove all Kali Linux repositories using the menu option to prevent potential package conflicts.

## Project Status

This project is a modernization of the original Katoolin by LionSec. It has been updated to support Python 3 and fix various compatibility issues with modern distributions. While the core logic remains similar, the codebase is being actively improved for better stability and maintainability.

## FAQ

**Can I use this on any Linux distribution?**
This script is specifically designed for Debian-based systems (Ubuntu, Debian, etc.). Usage on other distributions is not supported and may cause issues.

**Why a separate repository?**
The original repository appears unmaintained. This fork exists to provide necessary updates and fixes while retaining credit to the original author.

**Is it safe?**
The script automates the installation of robust tools. However, adding third-party repositories always carries some risk. Use with caution and ensure you understand the changes being made to your package manager sources.

**Reporting Issues**
For issues specific to this version, please open an issue on the [GitHub repository](https://github.com/0xGuigui/Katoolin3/issues).

## License

This project is licensed under the GNU General Public License v2.0.

## Authors

- **LionSec** (Original Author)
- **0xGuigui** (Maintainer)
