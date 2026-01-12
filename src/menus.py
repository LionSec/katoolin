def print_separator():
    print("\n" + "-" * 64 + "\n")


def help_menu():
    print("****************** +Commands+ ******************\n")
    print("\033[1;32mback\033[1;m \t\033[1;33mGo back\033[1;m")
    print("\033[1;32mgohome\033[1;m\t\033[1;33mGo to the main menu\033[1;m")
    print("\033[1;32mhelp\033[1;m \t\033[1;33mShow this help menu\033[1;m")
    print("\033[1;32mExit\033[1;m\t\033[1;33mExit the script\033[1;m")


def main_banner():
    banner = r"""
 $$\   $$\           $$\                         $$\ $$\            $$$$$$\  
 $$ | $$  |          $$ |                        $$ |\__|          $$ ___$$\ 
 $$ |$$  / $$$$$$\ $$$$$$\    $$$$$$\   $$$$$$\  $$ |$$\ $$$$$$$\  \_/   $$ |
 $$$$$  /  \____$$\\_$$  _|  $$  __$$\ $$  __$$\ $$ |$$ |$$  __$$\   $$$$$ / 
 $$  $$<   $$$$$$$ | \033[1;34mKali-Linux tools installer\033[1;m |$$ |$$ |$$ |  $$ |  \___$$\ 
 \033[1;34m$$ |\$$\ $$  __$$ | $$ |$$\ $$ |  $$ |$$ |  $$ |$$ |$$ |$$ |  $$ |$$\   $$ |
 $$ | \$$\\$$$$$$$  | \$$$$  |\$$$$$$  |\$$$$$$  |$$ |$$ |$$ |  $$ |\$$$$$$  |
 \__|  \__|\_______|  \____/  \______/  \______/ \__|\__|\__|  \__| \______/ V3.0\033[1;m
"""
    print(banner)
    print("")
    print(" \033[1;32m+ -- -- +=[ Original Script by: LionSec | Homepage: www.neodrix.com \033[1;m")
    print(" \033[1;32m+ -- -- +=[ Rewrites and maintained by: 0xGuigui\033[1;m")
    print(" \033[1;32m+ -- -- +=[ Latest update: 1/12/2026\033[1;m")
    print("")
    print("")
    print("\033[1;91m[W] Before updating and upgrading your system, please remove all Kali-linux repositories to "
          "avoid any kind of problem.\033[1;m")
    print("\033[1;91m[W] In some cases, Kali-Linux repositories can destabilize your system or worse, completely "
          "destroy it.\033[1;m")
    print("")


CLASSICMENU_INFO = ''' 
ClassicMenu Indicator is a notification area applet (application indicator) for the top panel of Ubuntu's Unity desktop environment.

It provides a simple way to get a classic GNOME-style application menu for those who prefer this over the Unity dash menu.

Like the classic GNOME menu, it includes Wine games and applications if you have those installed.

For more information , please visit : http://www.florian-diesch.de/software/classicmenu-indicator/

'''
