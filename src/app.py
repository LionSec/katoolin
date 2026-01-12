import os
import sys
import traceback

from categories import run_categories_menu
from commands import run_shell_capture
from menus import CLASSICMENU_INFO, help_menu, main_banner, print_separator
from repo import add_kali_key, remove_kali_repo, show_sources_list, write_kali_repo


def setup():
    # Root is required for apt and repo changes.
    if os.geteuid() != 0:
        print(
            "You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting.")
        return False
    os.system("clear")
    return True


def repo_menu():
    while True:
        print("")
        print("1) Add kali linux repositories")
        print("2) Update")
        print("3) Remove all kali linux repositories")
        print("4) View the contents of sources.list file")
        print("")
        repo = input(
            "\033[1;32mWhat do you want to do ?> \033[1;m")
        if repo == "1":
            if not add_kali_key():
                print(
                    "\033[1;31m\nFailed to add Kali repository key.\n\033[1;m")
                print_separator()
                continue
            repo_status = write_kali_repo()
            if repo_status == "added":
                print(
                    "\033[1;32m\nKali repositories have been added.\n\033[1;m")
            elif repo_status == "exists":
                print(
                    "\033[1;33m\nKali repositories are already present.\n\033[1;m")
            else:
                print(
                    "\033[1;31m\nFailed to add Kali repositories.\n\033[1;m")
            print_separator()
        elif repo == "2":
            rc, output = run_shell_capture("apt-get update")
            if rc == 0 and "W:" not in output and "E:" not in output:
                print("\033[1;32m\nUpdate completed.\n\033[1;m")
            elif rc == 0:
                print("\033[1;33m\nUpdate completed with warnings.\n\033[1;m")
            else:
                print("\033[1;31m\nUpdate failed.\n\033[1;m")
            print_separator()
        elif repo == "3":
            removed = remove_kali_repo()
            if removed:
                print(
                    "\033[1;31m\nAll kali linux repositories have been deleted !\n\033[1;m")
            else:
                print(
                    "\033[1;33m\nNo Kali repositories were found.\n\033[1;m")
            print_separator()
        elif repo == "back":
            return
        elif repo == "gohome":
            return
        elif repo == "exit" or repo == "quit":
            print("Shutdown requested...Goodbye...")
            sys.exit()
        elif repo == "4":
            show_sources_list()
            print_separator()
        else:
            print(
                "\033[1;31mSorry, that was an invalid command!\033[1;m")


def main():
    try:
        if not setup():
            return
        main_banner()

        while True:
            print("1) Add Kali repositories & Update")
            print("2) View Categories")
            print("3) Install classicmenu indicator")
            print("4) Install Kali menu")
            print("5) Help")
            print("")

            option0 = input("\033[1;36mkat > \033[1;m")
            if option0 == "exit" or option0 == "quit":
                print("Shutdown requested...Goodbye...")
                sys.exit()
            elif option0 == "1":
                repo_menu()
            elif option0 == "2":
                run_categories_menu()
            elif option0 == "3":
                print(CLASSICMENU_INFO)
                repo = input(
                    "\033[1;32mDo you want to install classicmenu indicator ? [y/n]> \033[1;m")
                if repo == "y":
                    cmd1 = os.system(
                        "add-apt-repository ppa:diesch/testing && apt-get update")
                    cmd = os.system(
                        "sudo apt-get install classicmenu-indicator")
            elif option0 == "help":
                print("")
                help_menu()
            elif option0 == "4":
                repo = input(
                    "\033[1;32mDo you want to install Kali menu ? [y/n]> \033[1;m")
                if repo == "y":
                    cmd1 = os.system("apt-get install kali-menu")
            elif option0 == "5":
                help_menu()
            else:
                print("\033[1;31mSorry, that was an invalid command!\033[1;m")
    except KeyboardInterrupt:
        print("Shutdown requested...Goodbye...")
    except Exception:
        traceback.print_exc(file=sys.stdout)
    sys.exit(0)
