
import os
import shutil
import math

# Colors
C_RESET = "\033[0m"
C_BOLD = "\033[1m"
C_CYAN = "\033[1;36m"
C_GREEN = "\033[1;32m"
C_YELLOW = "\033[1;33m"
C_RED = "\033[1;31m"
C_BLUE = "\033[1;34m"
C_WHITE = "\033[1;37m"

# Box drawing characters
BOX_TL = "╔"
BOX_TR = "╗"
BOX_BL = "╚"
BOX_BR = "╝"
BOX_H = "═"
BOX_V = "║"
BOX_L = "╠"
BOX_R = "╣"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(text):
    """Prints a styled header."""
    width = min(shutil.get_terminal_size().columns, 100)
    print(f"\n{C_CYAN}{'='*width}")
    print(f"{text.center(width)}")
    print(f"{'='*width}{C_RESET}\n")

def wait_for_input():
    """Waits for user input to continue."""
    print(f"\n{C_YELLOW}Press Enter to continue...{C_RESET}")
    input()

def print_status(text, status_type="info"):
    """Prints a status message."""
    if status_type == "success":
        print(f"{C_GREEN}[+] {text}{C_RESET}")
    elif status_type == "warn":
        print(f"{C_YELLOW}[!] {text}{C_RESET}")
    elif status_type == "error":
        print(f"{C_RED}[-] {text}{C_RESET}")
    else:
        print(f"{C_BLUE}[*] {text}{C_RESET}")

def print_menu(title, items, tools_mode=False, clear_screen=True):
    """
    Prints a menu in a nice box grid.
    items: list of (key, label) tuples.
    tools_mode: If True, auto-appends '0) Install All', 'back', 'gohome', 'shell'.
    """
    if clear_screen:
        clear()

    # Determine dimensions
    term_width = shutil.get_terminal_size().columns
    if term_width < 40:
        term_width = 80
        
    # Cap width to keep it readable, but at least enough to hold basic content
    box_width = min(term_width - 4, 100) 
    
    # Calculate title padding
    title_space = box_width - 2
    styled_title = f"{C_BOLD}{C_BLUE} {title} {C_RESET}"
    
    # We need visible length for center calculation, excluding color codes
    # Approximate visible length
    
    print(f"{C_CYAN}{BOX_TL}{BOX_H * title_space}{BOX_TR}{C_RESET}")
    # Title row
    # To center the title properly with color codes, we just print a header or reuse the box logic
    # For simplicity, let's just use the box border for the title area?
    # Actually, a simple centered title inside the box looks good.
    
    # Let's rebuild the items list to include extra tools if needed
    menu_items = list(items)
    
    extra_options = []
    if tools_mode:
        extra_options.append(("0", "Install All Tools"))
    
    # Standard navigation
    extra_options.append(("back", "Go back"))
    extra_options.append(("gohome", "Go to main menu"))
    extra_options.append(("shell", "Open system shell"))

    # Calculate Grid
    # Find max length of "key) label"
    max_len = 0
    all_display_items = [] # list of (key, label, display_str_len)
    
    for key, label in menu_items:
        s = f"{key}) {label}"
        max_len = max(max_len, len(s))
        all_display_items.append((key, label))
        
    # Column width needs some padding
    col_width = max_len + 4
    # content width inside box is box_width - 4 (borders + spacing)
    available_width = box_width - 4
    
    num_cols = max(1, available_width // col_width)
    
    # Print Title centered
    # We manually pad because .center() counts ANSI codes
    visible_title_len = len(title) + 2 # +2 for spaces
    pad_left = (box_width - 2 - visible_title_len) // 2
    pad_right = (box_width - 2) - visible_title_len - pad_left
    
    print(f"{C_CYAN}{BOX_V}{C_RESET}" + " " * pad_left + f"{C_BOLD}{C_WHITE} {title} {C_RESET}" + " " * pad_right + f"{C_CYAN}{BOX_V}{C_RESET}")
    print(f"{C_CYAN}{BOX_L}{BOX_H * (box_width - 2)}{BOX_R}{C_RESET}")
    
    # Print Empty Line
    print(f"{C_CYAN}{BOX_V}{C_RESET}" + " " * (box_width - 2) + f"{C_CYAN}{BOX_V}{C_RESET}")

    # Print Items
    num_items = len(all_display_items)
    num_rows = math.ceil(num_items / num_cols)
    
    for r in range(num_rows):
        row_str = f"{C_CYAN}{BOX_V}{C_RESET} "
        current_len = 1 # padding space
        
        for c in range(num_cols):
            idx = r * num_cols + c
            if idx < num_items:
                key, label = all_display_items[idx]
                
                # Construct colored string
                item_str = f"{C_GREEN}{key}){C_RESET} {label}"
                visible_len = len(key) + 2 + len(label)
                
                row_str += item_str
                
                # Padding to fill column
                padding = col_width - visible_len
                # If last column, we might have more space to fill to reach the right border
                if c == num_cols - 1:
                   padding = (box_width - 3) - current_len - visible_len
                
                row_str += " " * padding
                current_len += visible_len + padding
            else:
                # Empty cell
                # padding = (box_width - 3) - current_len 
                # wait, if it's empty we just fill to the end if it is the last one?
                pass
                
        # Final adjustment to ensure right border alignment
        # It's safer to calculate exactly how much space is left
        # We used visual lengths.
        # Let's simplify:
        # We print columns of fixed width.
        pass
        
    # Re-do print loop with simpler logic
    # rows of strings
    rows_to_print = []
    for r in range(num_rows):
        row_items = []
        for c in range(num_cols):
            idx = r * num_cols + c
            if idx < num_items:
                row_items.append(all_display_items[idx])
        rows_to_print.append(row_items)

    for row_items in rows_to_print:
        line_content = " " # Start padding
        visible_len = 1
        
        for i, (key, label) in enumerate(row_items):
             item_len = len(key) + 2 + len(label)
             
             # Render item
             line_content += f"{C_GREEN}{key}){C_RESET} {label}"
             
             # Calculate padding
             # If it's not the last item in the visual row (based on num_cols), use col_width
             # But if it is the last item in the *actual* row, we just padding to the end?
             # No, grid alignment looks better if we respect col_width always, except maybe for the last column?
             # Let's use fixed col_width for all except the last column in the grid
             
             if i < num_cols - 1:
                 pad = col_width - item_len
                 line_content += " " * pad
                 visible_len += item_len + pad
             else:
                 # Last column, we don't pad with spaces yet, we handle right align at the end
                 visible_len += item_len
        
        # Fill rest of line to reach box_width - 2
        remaining = (box_width - 2) - visible_len
        line_content += " " * remaining
        
        print(f"{C_CYAN}{BOX_V}{C_RESET}{line_content}{C_CYAN}{BOX_V}{C_RESET}")

    # Output Extra Options Separator
    print(f"{C_CYAN}{BOX_L}{BOX_H * (box_width - 2)}{BOX_R}{C_RESET}")
    
    # Extra Options Logic (similar grid or list?)
    # A list 2-per-row usually fits well for these standard options
    
    # Let's put Install All separate if it exists
    if tools_mode:
        k, l = extra_options[0]
        line = f" {C_YELLOW}{k}){C_RESET} {l}"
        vlen = 1 + len(k) + 2 + len(l)
        rem = (box_width - 2) - vlen
        print(f"{C_CYAN}{BOX_V}{C_RESET}{line}{' ' * rem}{C_CYAN}{BOX_V}{C_RESET}")
        extra_options.pop(0)

    # Remaining options (back, gohome, shell)
    # 3 items. 3 cols?
    
    # Reuse row printing logic specifically for these 3
    # They fit in 1 row usually
    
    line_content = " "
    vlen = 1
    
    # We distribute them evenly? Or just default grid?
    # Let's try to fit them all in one row if possible
    # Calculate total length
    total_len_extras = sum(len(k)+2+len(l) for k,l in extra_options) + (len(extra_options)-1)*4 # +spacing
    
    if total_len_extras < (box_width - 4):
         # Fit in one row centered or spread?
         # Spread looks nice
         # actually let's just use the same row logic but with dynamic spacing
         pass
    
    # Simplest: Just print them
    # For now let's just use the same grid logic but maybe 3 cols
    ex_cols = 3
    ex_col_width = (box_width - 4) // 3
    
    row_str = " "
    curr_vlen = 1
    for i, (key, label) in enumerate(extra_options):
         txt = f"{C_YELLOW}{key}){C_RESET} {label}"
         txt_len = len(key) + 2 + len(label)
         
         row_str += txt
         
         if i < len(extra_options) - 1:
             pad = ex_col_width - txt_len
             if pad < 2: pad = 2 # minimum spacing
             row_str += " " * pad
             curr_vlen += txt_len + pad
         else:
             curr_vlen += txt_len
             
    rem = (box_width - 2) - curr_vlen
    # if rem < 0, our calc was wrong and it will look broken, but usually fine
    if rem < 0: rem = 0
    
    print(f"{C_CYAN}{BOX_V}{C_RESET}{row_str}{' ' * rem}{C_CYAN}{BOX_V}{C_RESET}")

    print(f"{C_CYAN}{BOX_BL}{BOX_H * (box_width - 2)}{BOX_BR}{C_RESET}")
    print()

