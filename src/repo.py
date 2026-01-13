import os
from typing import List, Tuple
from logger import logger

from commands import run_shell

REPO_PATH = "/etc/apt/sources.list.d/katoolin.list"
SOURCES_LIST_PATH = "/etc/apt/sources.list"
KALI_KEY_PATH = "/usr/share/keyrings/kali-archive-keyring.gpg"
REPO_LINE = (
    "deb [signed-by=/usr/share/keyrings/kali-archive-keyring.gpg] "
    "https://http.kali.org/kali kali-rolling main contrib non-free\n"
)


def show_sources_list() -> None:
    files = [
        (SOURCES_LIST_PATH, "sources.list"),
        (REPO_PATH, "katoolin.list"),
    ]
    found = False
    for path, label in files:
        if not os.path.exists(path):
            continue
        found = True
        print("\033[1;36m[%s]\033[1;m %s\n" % (label, path))
        try:
            with open(path, "r") as src:
                print(src.read())
        except IOError as e:
            logger.error(f"Unable to read {path}: {e}")
            print("\033[1;31mUnable to read %s.\033[1;m\n" % path)
    if not found:
        logger.warning("No sources list files found")
        print("\033[1;33mNo sources list files were found.\033[1;m")


def add_kali_key() -> bool:
    # Install the Kali archive key so apt trusts the repo.
    logger.info("Adding Kali-Linux key...")
    cmd = (
        "wget -q -O - https://archive.kali.org/archive-key.asc | "
        "gpg --dearmor | tee %s >/dev/null" % KALI_KEY_PATH
    )
    if not run_shell(cmd):
        logger.error("Failed to download or install GPG key")
        return False
    try:
        os.chmod(KALI_KEY_PATH, 0o644)
    except OSError as e:
        logger.error(f"Failed to chmod key file: {e}")
        return False
    logger.info("Key added successfully")
    return True


def write_kali_repo() -> str:
    if os.path.exists(REPO_PATH):
        return "exists"
    try:
        with open(REPO_PATH, "w") as repo_file:
            repo_file.write("# Kali linux repositories | Added by Katoolin\n")
            repo_file.write(REPO_LINE)
    except IOError as e:
        logger.error(f"Failed to write repo file: {e}")
        return "error"
    return "added"


def remove_kali_repo() -> bool:
    removed_repo = False
    if os.path.exists(REPO_PATH):
        os.remove(REPO_PATH)
        removed_repo = True
    delete_list = [
        "# Kali linux repositories | Added by Katoolin\n",
        "deb http://http.kali.org/kali kali-rolling main contrib non-free\n",
        REPO_LINE,
    ]
    try:
        with open(SOURCES_LIST_PATH, "r") as fin:
            lines = fin.readlines()
        with open(SOURCES_LIST_PATH, "w") as fout:
            for line in lines:
                if line in delete_list:
                    removed_repo = True
                    continue
                fout.write(line)
    except IOError as e:
        logger.error(f"Failed to clean sources.list: {e}")
        return False
    return removed_repo
