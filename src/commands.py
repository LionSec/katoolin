import os
import subprocess
from logger import logger

from typing import List, Tuple

def run_shell(cmd: str) -> bool:
    """Run a shell command and return True if successful."""
    # Use the shell because many menu entries are plain one-liners.
    logger.debug(f"Running shell command: {cmd}")
    return subprocess.run(cmd, shell=True).returncode == 0


def run_shell_capture(cmd: str) -> tuple[int, str]:
    """Run a shell command and return (return_code, stdout). Stderr is merged into stdout."""
    # Capture output so we can show warnings from apt.
    logger.debug(f"Running shell command (capture): {cmd}")
    proc = subprocess.run(
        cmd,
        shell=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    # We log stdout if it's not empty, but we might not want to print it twice if the caller does.
    # However, existing behavior printed it. Let's keep printing but maybe via logger? 
    # The original code used print(proc.stdout, end=""). 
    # For interactive tools (apt), we want the user to see output.
    if proc.stdout:
        print(proc.stdout, end="") 
        
    return proc.returncode, proc.stdout or ""

def exec_system_command(cmd: str) -> int:
    """
    Execute a system command securely using subprocess.
    Returns the return code.
    """
    logger.info(f"Executing: {cmd}")
    try:
        # We use shell=True because we have complex commands with pipes/&& from tools.json
        # Check=False allows us to handle the error code manually
        result = subprocess.run(cmd, shell=True, check=False)
        if result.returncode != 0:
            logger.error(f"Command failed with code {result.returncode}: {cmd}")
        return result.returncode
    except Exception as e:
        logger.error(f"Error executing command '{cmd}': {e}")
        return -1

def install_tools(commands: List[str]) -> None:
    """
    Smartly install a list of tools.
    Aggregates 'apt-get install' commands for performance.
    Runs other commands sequentially.
    """
    apt_packages: List[str] = []
    other_commands: List[str] = []

    for cmd in commands:
        cmd = cmd.strip()
        # Check for simple apt-get install commands
        if cmd.startswith("apt-get install ") and "&&" not in cmd and ";" not in cmd and "|" not in cmd:
            pkg_part = cmd.replace("apt-get install", "").strip()
            pkgs = [p for p in pkg_part.split() if not p.startswith("-")]
            apt_packages.extend(pkgs)
        else:
            other_commands.append(cmd)

    # 1. Run aggregated apt install with fallback
    if apt_packages:
        # Remove duplicates
        apt_packages = list(set(apt_packages))
        logger.info(f"Aggregating installation for {len(apt_packages)} packages...")
        full_apt_cmd = f"apt-get install -y {' '.join(apt_packages)}"
        
        # Try aggregated install
        ret = exec_system_command(full_apt_cmd)
        
        if ret != 0:
            # Fallback to sequential installation
            logger.warning("Aggregated installation failed. Falling back to sequential installation...")
            print("\033[1;33mAggregated installation failed. Retrying packages one by one...\033[1;m")
            
            for pkg in apt_packages:
                ret_seq = exec_system_command(f"apt-get install -y {pkg}")
                # We log errors individually but continue
                if ret_seq != 0:
                     logger.error(f"Failed to install package: {pkg}")

    # 2. Run others sequentially
    for cmd in other_commands:
        # Continue execution even if one fails
        exec_system_command(cmd)

def uninstall_tools(commands: List[str]) -> None:
    """
    Uninstall tools that were installed via apt-get.
    Ignores non-apt commands for safety.
    """
    apt_packages: List[str] = []

    for cmd in commands:
        cmd = cmd.strip()
        # Check for simple apt-get install commands
        if cmd.startswith("apt-get install ") and "&&" not in cmd and ";" not in cmd and "|" not in cmd:
            pkg_part = cmd.replace("apt-get install", "").strip()
            pkgs = [p for p in pkg_part.split() if not p.startswith("-")]
            apt_packages.extend(pkgs)
            
    if not apt_packages:
        logger.warning("No apt packages found to uninstall in the provided commands.")
        return

    # Remove duplicates
    apt_packages = list(set(apt_packages))
    logger.info(f"Uninstalling {len(apt_packages)} packages...")
    
    # Run aggregated remove
    full_remove_cmd = f"apt-get remove -y {' '.join(apt_packages)}"
    exec_system_command(full_remove_cmd)
    
    # Autoremove cleanup
    logger.info("Running autoremove to clean up dependencies...")
    exec_system_command("apt-get autoremove -y")

def open_shell() -> None:
    """Open an interactive shell."""
    print("\033[1;33mStarting shell... Type 'exit' to return to Katoolin3.\033[1;m")
    user_shell = os.environ.get("SHELL", "/bin/bash")
    try:
        subprocess.run(user_shell)
    except Exception as e:
        logger.error(f"Failed to open shell: {e}")
