import os
import sys
import traceback
from typing import List, Tuple, Optional

from categories import run_categories_menu, run_search_menu
from commands import run_shell_capture, exec_system_command
from menus import CLASSICMENU_INFO, help_menu, main_banner, print_separator
from repo import add_kali_key, remove_kali_repo, show_sources_list, write_kali_repo
from style import print_menu, clear, wait_for_input
from logger import logger, setup_logger


def setup() -> bool:
    """Check requirements and setup environment."""
    # Root is required for apt and repo changes.
    if os.geteuid() != 0:
        logger.error("Root privileges required.")
        print(
            "You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting.")
        return False
    clear()
    return True

def repo_menu() -> None:
    """Manage Kali repositories."""
    while True:
        options: List[Tuple[str, str]] = [
            ("1", "Add kali linux repositories"),
            ("2", "Update"),
            ("3", "Remove all kali linux repositories"),
            ("4", "View the contents of sources.list file"),
        ]
        print_menu("Kali Linux Repositories", options, tools_mode=False)
        repo = input(
            "\033[1;32mWhat do you want to do ?> \033[1;m")
        if repo == "1":
            if not add_kali_key():
                logger.error("Failed to add Kali repository key")
                print(
                    "\033[1;31m\nFailed to add Kali repository key.\n\033[1;m")
                print_separator()
            else:
                repo_status = write_kali_repo()
                if repo_status == "added":
                    logger.info("Kali repositories added")
                    print(
                        "\033[1;32m\nKali repositories have been added.\n\033[1;m")
                elif repo_status == "exists":
                    logger.warning("Kali repositories already present")
                    print(
                        "\033[1;33m\nKali repositories are already present.\n\033[1;m")
                else:
                    logger.error("Failed to add Kali repositories")
                    print(
                        "\033[1;31m\nFailed to add Kali repositories.\n\033[1;m")
                print_separator()
            wait_for_input()
        elif repo == "2":
            logger.info("Updating repositories...")
            rc, output = run_shell_capture("apt-get update")
            if rc == 0 and "W:" not in output and "E:" not in output:
                logger.info("Update completed successfully")
                print("\033[1;32m\nUpdate completed.\n\033[1;m")
            elif rc == 0:
                logger.warning("Update completed with warnings")
                print("\033[1;33m\nUpdate completed with warnings.\n\033[1;m")
            else:
                logger.error("Update failed")
                print("\033[1;31m\nUpdate failed.\n\033[1;m")
            print_separator()
            wait_for_input()
        elif repo == "3":
            logger.info("Removing Kali repositories...")
            removed = remove_kali_repo()
            if removed:
                logger.info("Kali repositories removed")
                print(
                    "\033[1;31m\nAll kali linux repositories have been deleted !\n\033[1;m")
            else:
                logger.warning("No Kali repositories found to remove")
                print(
                    "\033[1;33m\nNo Kali repositories were found.\n\033[1;m")
            print_separator()
            wait_for_input()
        elif repo == "back":
            return
        elif repo == "gohome":
            return
        elif repo == "shell":
            from commands import open_shell
            open_shell()
        elif repo == "exit" or repo == "quit":
            logger.info("Shutdown requested")
            print("Shutdown requested...Goodbye...")
            sys.exit()
        elif repo == "4":
            show_sources_list()
            print_separator()
            wait_for_input()
        else:
            print(
                "\033[1;31mSorry, that was an invalid command!\033[1;m")
            wait_for_input()


def main() -> None:
    try:
        setup_logger() # Initialize logger
        if not setup():
            return

        while True:
            # Clear manualy here so we can print banner on top
            clear()
            main_banner()
            
            options: List[Tuple[str, str]] = [
                ("1", "Add Kali repositories & Update"),
                ("2", "View Categories"),
                ("3", "Search for tools"),
                ("4", "Install classicmenu indicator"),
                ("5", "Install Kali menu"),
                ("6", "Help"),
            ]
            # Tell print_menu NOT to clear and NOT to show nav options
            print_menu("Main Menu", options, tools_mode=False, show_navigation=False, clear_screen=False)
            option0 = input("\033[1;36mkat > \033[1;m")
            if option0 == "exit" or option0 == "quit":
                logger.info("Shutdown requested")
                print("Shutdown requested...Goodbye...")
                sys.exit()
            elif option0 == "1":
                repo_menu()
            elif option0 == "2":
                run_categories_menu()
            elif option0 == "3":
                run_search_menu()
            elif option0 == "4":
                print(CLASSICMENU_INFO)
                repo = input(
                    "\033[1;32mDo you want to install classicmenu indicator ? [y/n]> \033[1;m")
                if repo == "y":
                    logger.info("Installing classicmenu-indicator")
                    exec_system_command("add-apt-repository ppa:diesch/testing && apt-get update")
                    exec_system_command("apt-get install classicmenu-indicator")
                wait_for_input()
            elif option0 == "6":
                print("")
                help_menu()
                wait_for_input()
            elif option0 == "5":
                repo = input(
                    "\033[1;32mDo you want to install Kali menu ? [y/n]> \033[1;m")
                if repo == "y":
                    logger.info("Installing kali-menu")
                    exec_system_command("apt-get install kali-menu")
                wait_for_input()
            elif option0 == "help":
                help_menu()
                wait_for_input()
            else:
                print("\033[1;31mSorry, that was an invalid command!\033[1;m")
                wait_for_input()
    except KeyboardInterrupt:
        logger.info("Shutdown requested (KeyboardInterrupt)")
        print("Shutdown requested...Goodbye...")
    except Exception as e:
        logger.critical(f"Unhandled exception: {e}")
        traceback.print_exc(file=sys.stdout)
    sys.exit(0)
