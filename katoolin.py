from core.resources import main_opts, sub_opts, categories, tool_command, banner

import re
import os
from textwrap import fill
from enum import Enum, unique
from pprint import pprint
from math import ceil
from sys import exit


@unique
class Context(Enum):
    ON_START = 1
    ON_SUB_MENU = 2
    ON_CATEGORY = 8
    ON_ADD_AND_UPDATE = 3
    ON_VIEW_CATEGORIES = 4
    ON_INSTALL_KALI_MENU = 5
    ON_INSTALL_CLASSIC_MENU = 6
    ON_INPUT_CONFIRM = 7


class Katoolin:

    def __init__(self):
        self.prompt = "\nkat> "
        self.category = None
        self.context = Context.ON_START
        self.source_file = '/etc/apt/sources.list'
        self.banner = banner

    @property
    def home_opts(self):
        return main_opts

    @property
    def sub_opts(self):
        return sub_opts

    @property
    def categories(self):
        return categories

    @staticmethod
    def _add_index(data):
        for d in range(len(data)):
            data[d] = f"[{d + 1}]-{data[d]}"
        return data
    
    @staticmethod
    def exit():
        exit()
    
    @property
    def tool_command(self):
        return tool_command
    
    @property
    def tools(self):
        tools = [i for i in self.tool_command[self.category].keys()]
        return tools

    @staticmethod
    def clear_screen():
        os.system('clear')
    
    def _get_menu(self):
        """
        Returns a menu which is a list of options,
        based on the current context of the application
        """
        if self.context == Context.ON_START:
            return self.home_opts[:]
        elif self.context == Context.ON_SUB_MENU:
            return self.sub_opts[:]
        elif self.context == Context.ON_VIEW_CATEGORIES:
            return self.categories[:]
        elif self.context == Context.ON_CATEGORY:
            options = self.tools[:]
            options.append("Install All Tools")
            return options

    def print_menu(self):
        """
        Displays the available options in a nicely formatted way.
        """

        data = self._add_index(self._get_menu())
        per_row = 2 if len(data) // 2 > 0 else len(data)
        index = 0
        row_num = 1 if per_row < 2 else ceil(len(data) / per_row)
        for _ in range(row_num):
            for _ in range(per_row):
                try:  # EAFP
                    print(data[index], end='\t   '.expandtabs(len(max(data, key=lambda x: len(x))) - len(data[index])))
                    index += 1
                except:
                    pass
            print()
    
    def get_input(self):
        """
        Prompts user for input based on the current context.
        """
        if self.context == Context.ON_INPUT_CONFIRM:
            prompt = "\nDo you wish to proceed?_Y/N: "
            data = input(prompt).lower()
        return data 
    
    def common_commands(self, *, command, prev_context=None):
        """
        Handles commands common among different contexts.
        """
        if command in ['cls', 'clear'] and self.context == Context.ON_START:
            self.clear_screen()
            print(self.banner)
            self.print_menu()
        elif command in ['cls', 'clear'] and self.context != Context.ON_START:
            self.clear_screen()
            self.print_menu()
        elif command == 'back':
            self.context = prev_context
        elif command == 'home':
            self.context = Context.ON_START
            self.clear_screen()
            print(self.banner)
            self.print_menu()
        elif command == 'exit':
            self.exit()
        else:
            print("Invalid command or input.")

    @property
    def categories_index(self):
        """
        Creates an index in which the various categories maps
        to it's option number.
        """
        categories = self.categories
        keys_ = [i for i in range(1, len(categories)+1)]
        _index = {}
        for key, value in zip(keys_, categories):
            _index[key] = value
        print(_index)
        return _index
    
    @property
    def tools_index(self):
        """
        Creates an index in which the various tools in each category maps
        to it's option number.
        """
        category = self.category
        tools = self.tools
        _index = {}
        keys_ = [i for i in range(1, len(tools)+1)]
        for key, value in zip(keys_, tools):
            _index[key] = value
        
        return _index
    

    def install_classic_menu(self):
        """
        Handles classic menu installation
        """
        info = """
ClassicMenu Indicator is a notification area applet (application indicator) for 
the top panel of Ubuntu's Unity desktop environment.
It provides a simple way to get a classic GNOME-style application menu for those
who prefer this over the Unity dash menu.
Like the classic GNOME menu, it includes Wine games and applications if you have those installed.
For more information, please visit http://www.florian-diesch.de/software/classicmenu-indicator
        
        """
        print(fill(info.lstrip(), 78, initial_indent="\n")) # print some info
        self.context = Context.ON_INPUT_CONFIRM # change context to recieve data
        input_ = self.get_input() # get input
        if input_ == 'y':
            os.system("add-apt-repository ppa:diesch/testing && apt-get update")
            os.system("sudo apt-get install classicmenu-indicator")
        else:
            print("Operation cancelled!")
        self.context = Context.ON_START
    
    def install_kali_menu(self):
        """
        Handles the installation of kali menu
        """
        print("\nThis process will install the kali-menu package")
        self.context = Context.ON_INPUT_CONFIRM
        input_ = self.get_input()
        if input_ == 'y':
            os.system('sudo apt-get install kali-menu')
        else:
            print("Operation Aborted!")
        self.context = Context.ON_START
    
    @staticmethod
    def help():
        """
        Help utility
        """
        doc = """
        [About]
            Katoolin 3.0v is a linux tool for installing useful packages and tools.
            Written in Python by LionSec | Homepage: www.neodrix.com upgraded by
            teddbug-S | Unicorn Inc. https://github.com/unicorninc/

        [Usage]
            Choose an option by entrying it's number, this might lead
            to other sub-menus as well and it's still same process.

            Option 1 will lead you to a sub menu where you can update
            and also add new Kali repositories to your source.list file

            Option 2 provides you with a set of categories you can choose tools from,
            selecting a category lists the tools available and you can just go ahead to install.

            Option 3 installs the classic menu indicator package, also provides little but
            useful information about it.

            Option 4 installs the Kali menu package.

            Option 5 lead you here!

            Some useful commands are
                - home  [takes you back to the home screen]
                - back [takes you back to the previous screen]
                - cls ['clear screen' clears the screen and displays the menu]
                -exit [exit the program]
        
        """
        print(doc)
    
    def add_kali_repos(self):
        """
        Adds Kali repositories to /etc/apt/sources.list
        """
        os.system("apt-key adv --keyserver pool.sks-keyservers.net --recv-keys ED444FF07D8D0BF6")
        os.system("echo '# Kali linux repositories | Added by Katoolin\ndeb http://"
            f"kali.org/kali kali-rolling main contrib non-free' >> {self.source_file}")
        print("Repositories added successfully.")
    
    @staticmethod
    def update_repos():
        """
        Updates user's packages
        """
        os.system('apt-get update -m')
    
    def remove_kali_repos(self):
        """
        Removes all Kali repositories from the source file.
        """
        lines_to_remove = [
            '# Kali linux repositories | Added by Katoolin\n',
            'deb http://kali.org/kali kali-rolling main contrib non-free\n'
        ]
        try:
            with open(self.source_file) as sf:
                contents = sf.readlines()
                new_contents = [line for line in contents if line not in lines_to_remove]
                with open(self.source_file, 'w+') as sf:
                   sf.writelines(new_contents)
            print("Removed Successfully.")
        except FileNotFoundError:
            print(f"\nHmm, can't find the file {self.source_file}")
        except FileExistsError:
            print("\nThat's wierd!")
        except IOError:
            print("Oops, an error occured, file might be in use by another program.")
    
    def read_source_file(self):
        """
        Uses system's cat tool to display file contents
        """
        os.system(f"cat {self.source_file}")

    def edit_source_file(self):
        """
        Opens file with the GNU nano to edit 
        """
        os.system(f"nano {self.source_file}")

    def do_tool_install(self, tool):
        """
        Extracts and executes the appropriate command needed to install the tool
        """
        if tool:
            command = self.tool_command.get(self.category).get(tool)
            if command:
                os.system(command)
            else:
                print(f"\nOops we're very sorry, {tool} not available.")
        else:
            os.system(f"apt-get install -y {' '.join(self.tools)}")

    def do_home(self):
        """
        Handles the home screen
        """
        self.clear_screen()
        print(self.banner)
        self.print_menu()
        while self.context == Context.ON_START:
            self.prompt = "\nkat> "   
            prompt = input(self.prompt).lower()
            if prompt == '1':
                self.context = Context.ON_SUB_MENU
            elif prompt == '2':
                self.context = Context.ON_VIEW_CATEGORIES
            elif prompt == '3':
                self.install_classic_menu()
            elif prompt == '4':
                self.install_kali_menu()
            elif prompt == '5':
                self.help()
            else:
                self.common_commands(command=prompt, prev_context=Context.ON_START)

    def do_sub_menu(self):
        """
        Handles the sub menu
        """
        if self.context == Context.ON_SUB_MENU:
            self.clear_screen()
            self.print_menu()
            while self.context == Context.ON_SUB_MENU:
                self.prompt = "\nkali@kat> "
                prompt = input(self.prompt).lower()
                # adding kali repos to source file
                if prompt == '1':
                    self.context = Context.ON_INPUT_CONFIRM # change context
                    print("\nThis will add Kali Linux repositories to your system.")
                    _input = self.get_input() # get confirmation
                    if _input == 'y':
                        self.add_kali_repos()
                    else:
                        print("Operation arborted!")
                    self.context = Context.ON_SUB_MENU
                # update repos
                elif prompt == '2':
                    print("\nUpdating your packages")
                    self.context = Context.ON_INPUT_CONFIRM
                    _input = self.get_input()
                    if _input == 'y':
                        self.update_repos()
                    else:
                        print("Operation aborted!")
                    self.context = Context.ON_SUB_MENU
                # removing kali repos from source file
                elif prompt == '3':
                    self.context = Context.ON_INPUT_CONFIRM
                    print('\nThis process will remove all Kali repos added to' 
                    'your source file by this tool')
                    _input = self.get_input()
                    if _input == 'y':
                        self.remove_kali_repos()
                    else:
                        print("Operation aborted!")
                    self.context = Context.ON_SUB_MENU # return back to sub menu's context
                # reading contents from the source file
                elif prompt == '4':
                    self.read_source_file()
                # editing source file personally
                elif prompt == '5':
                    self.edit_source_file()
                else:
                    self.common_commands(command=prompt, prev_context=Context.ON_START)

    def do_view_categories(self):
        """
        Handles the viewing categories
        """
        if self.context == Context.ON_VIEW_CATEGORIES: # check if it's time to play
            self.clear_screen() # clear screen
            self.print_menu() # print catgories
            while self.context == Context.ON_VIEW_CATEGORIES:
                self.prompt = "\ncategories@kat> " # change the prompt
                prompt = input(self.prompt) # prompt
                if prompt in [ str(i) for i in range(1, len(self.categories)+1)]:
                    self.category = self.categories_index.get(int(prompt))
                    self.context = Context.ON_CATEGORY
                else:
                    self.common_commands(command=prompt, prev_context=Context.ON_START)
    
    def do_category(self):
        """
        Handles the processes of each category and it's tools
        """
        if self.context == Context.ON_CATEGORY:
            self.clear_screen()
            self.print_menu()
            while self.context == Context.ON_CATEGORY:
                self.prompt = f"\n{self.category.replace(' ', '_').lower()}_@kat> "
                prompt = input(self.prompt)
                if prompt in [str(i) for i in range(1, len(self.tools)+1)]:
                    tool = self.tools_index[int(prompt)]
                    self.context = Context.ON_INPUT_CONFIRM
                    print(f"\n{tool} is going to be installed")
                    _input = self.get_input()
                    if _input == 'y':
                        self.do_tool_install(tool)
                    else:
                        print("Operation aborted!")
                    self.context = Context.ON_CATEGORY
                elif prompt == str(len(self.tools)+1):
                    tool = 0
                    self.do_tool_install(tool)
                else:
                    self.common_commands(command=prompt, prev_context=Context.ON_VIEW_CATEGORIES)
    
    def main(self):
        """
        Main funtion of the Katoolin tool
        """
        if os.getuid():
            self.clear_screen()
            print("\nPlease, this tool requires sudo priviledges."
            "\nYou can enable it by running 'sudo su' first.\n")
        else:
            while True:
                try:
                    self.do_home()
                    self.do_view_categories()
                    self.do_category()
                    self.do_sub_menu()
                except KeyboardInterrupt:
                    print("[-] Keyboard interrupt, please use the exit command.")



if __name__ == '__main__':
    kt = Katoolin()
    kt.main()
