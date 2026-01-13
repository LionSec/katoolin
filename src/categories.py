import json
import os
import sys
from typing import List, Dict, Any, Optional

from commands import open_shell, exec_system_command, install_tools
from style import print_menu, wait_for_input
from logger import logger

# Path to tools.json
TOOLS_FILE = os.path.join(os.path.dirname(__file__), "tools.json")

def load_tools() -> Dict[str, List[Dict[str, str]]]:
    """Load tools from the JSON file."""
    try:
        with open(TOOLS_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(f"Error loading tools.json: {e}")
        sys.exit(1)

def run_category_menu(category_name: str, tools: List[Dict[str, str]]) -> Optional[str]:
    """Generic menu function for a specific category of tools."""
    while True:
        # Build options for the menu
        options: List[tuple[str, str]] = []
        tools_map: Dict[str, Dict[str, str]] = {}
        
        # 'tools' is a list of dicts: {"name": "...", "command": "..."}
        for i, tool in enumerate(tools):
            key = str(i + 1)
            # Some tools might be unnamed if data is dirty, but we assume it's clean
            name = tool.get("name", "Unknown")
            options.append((key, name))
            tools_map[key] = tool

        print_menu(category_name, options, tools_mode=True)
        print(f"\033[1;32mSelect a tool to install or press (0) to install all {category_name} tools.\n\033[1;m")

        choice = input("\033[1;36mkat > \033[1;m")
        
        if choice == "back":
            return "back"
        elif choice == "gohome":
            return "gohome"
        elif choice == "shell":
            open_shell()
        elif choice == "exit" or choice == "quit":
            sys.exit()
        elif choice == "help":
            print("Available commands:\n"
                  "back\t\tGo back to main menu\n"
                  "gohome\t\tGo to the main menu\n"
                  "exit\t\tExit the program\n"
                  "help\t\tShow this help menu\n")
            wait_for_input()
        elif choice == "0":
             # Install all tools in this category
             logger.info(f"Installing all tools in {category_name}...")
             print(f"\n\033[1;33mInstalling all tools in {category_name}...\033[1;m\n")
             
             commands = [t["command"] for t in tools if t.get("command")]
             if commands:
                 install_tools(commands)
             else:
                 logger.warning("No commands found for this category.")
                 print("No commands found for this category.")
             wait_for_input()
        elif choice in tools_map:
            tool = tools_map[choice]
            cmd = tool.get("command")
            if cmd:
                print(f"\n\033[1;33mExecuting: {cmd}\033[1;m\n")
                exec_system_command(cmd)
            else:
                logger.error("No command defined for this tool.")
                print("\033[1;31mError: No command defined for this tool.\033[1;m")
            wait_for_input()
        else:
            print("\033[1;31mSorry, that was an invalid command!\033[1;m")
            wait_for_input()


def run_categories_menu() -> None:
    """Main categories menu."""
    tools_data = load_tools()
    # tools_data is dict: category_name -> list of tools
    
    # We want a fixed order if possible, roughly matching the original if possible, 
    # but dicts are insertion ordered in modern Python (which json.load preserves).
    # Check if tools.json preserved order.
    categories = list(tools_data.keys())

    while True:
        options: List[tuple[str, str]] = []
        cat_map: Dict[str, str] = {}
        for i, cat in enumerate(categories):
            key = str(i + 1)
            options.append((key, cat))
            cat_map[key] = cat

        print_menu("All Categories", options, tools_mode=True)
        print("\033[1;32mSelect a category or press (0) to install all Kali linux tools .\n\033[1;m")

        option = input("\033[1;36mkat > \033[1;m")

        if option == "back":
            return
        elif option == "gohome":
            return
        elif option == "shell":
            open_shell()
        elif option == "exit" or option == "quit":
            print("Shutdown requested...Goodbye...")
            sys.exit()
        elif option == "help":
            print("Available commands:\n"
                  "back\t\tGo back to main menu\n"
                  "gohome\t\tGo to the main menu\n"
                  "exit\t\tExit the program\n"
                  "help\t\tShow this help menu\n")
            wait_for_input()
        elif option == "0":
            # Install ALL tools from ALL categories
            logger.info("Installing all tools from all categories...")
            print("\n\033[1;33mPreparing to install all tools from all categories...\033[1;m\n")
            all_commands = []
            for cat in categories:
                cat_tools = tools_data[cat]
                for t in cat_tools:
                    if t.get("command"):
                        all_commands.append(t["command"])
            
            if all_commands:
                 install_tools(all_commands)
            else:
                 logger.warning("No tools found.")
                 print("No tools found.")
            wait_for_input()

        elif option in cat_map:
            selected_cat = cat_map[option]
            tools = tools_data[selected_cat]
            result = run_category_menu(selected_cat, tools)
            if result == "gohome":
                return # Propagate gohome to main menu
        else:
             print("\033[1;31mSorry, that was an invalid command!\033[1;m")
             wait_for_input()
