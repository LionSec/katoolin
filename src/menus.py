from style import C_BLUE, C_GREEN, C_RED, C_RESET, print_header

def print_separator() -> None:
    print("\n" + "-" * 64 + "\n")



def help_menu() -> None:
    print_header("Commands")
    print(f"{C_GREEN}back{C_RESET}   \tGo back")
    print(f"{C_GREEN}gohome{C_RESET} \tGo to the main menu")
    print(f"{C_GREEN}shell{C_RESET}  \tOpen system shell")
    print(f"{C_GREEN}help{C_RESET}   \tShow this help menu")
    print(f"{C_GREEN}exit{C_RESET}   \tExit the script")


def main_banner() -> None:
    banner = fr"""
{C_BLUE}
 $$\   $$\           $$\                         $$\ $$\            $$$$$$\  
 $$ | $$  |          $$ |                        $$ |\__|          $$ ___$$\ 
 $$ |$$  / $$$$$$\ $$$$$$\    $$$$$$\   $$$$$$\  $$ |$$\ $$$$$$$\  \_/   $$ |
 $$$$$  /  \____$$\_$$  _|  $$  __$$\ $$  __$$\ $$ |$$ |$$  __$$\   $$$$$ / 
 $$  $$<   $$$$$$$ | {C_RED}Kali-Linux tools installer{C_BLUE} |$$ |$$ |$$ |  $$ |  \___$$\ 
 $$ |\$$\ $$  __$$ | $$ |\$$\ $$ |  $$|$$ | $$ |$$ |$$ |$$ |  $$ |\$$\   $$ |
 $$ | \$$\\$$$$$$$ | \$$$$  |\$$$$$$  |\$$$$$$  |$$ |$$ |$$ |  $$ |\$$$$$$  |
 \__|  \__|\_______|  \____/  \______/  \______/ \__|\__|\__|  \__| \______/ V3.1
{C_RESET}
"""
    print(banner)
    print(f" {C_GREEN}+ -- -- +=[ Original Script by: LionSec | Homepage: www.neodrix.com {C_RESET}")
    print(f" {C_GREEN}+ -- -- +=[ Rewrites and maintained by: 0xGuigui{C_RESET}")
    print(f" {C_GREEN}+ -- -- +=[ Latest update: 1/12/2026{C_RESET}")
    print("")
    print(f"{C_RED}[W] Before updating and upgrading your system, please remove all Kali-linux repositories to avoid any kind of problem.{C_RESET}")
    print(f"{C_RED}[W] In some cases, Kali-Linux repositories can destabilize your system or worse, completely destroy it.{C_RESET}")
    print("")


CLASSICMENU_INFO = ''' 
ClassicMenu Indicator is a notification area applet (application indicator) for the top panel of Ubuntu's Unity desktop environment.

It provides a simple way to get a classic GNOME-style application menu for those who prefer this over the Unity dash menu.

Like the classic GNOME menu, it includes Wine games and applications if you have those installed.

For more information , please visit : http://www.florian-diesch.de/software/classicmenu-indicator/

'''
