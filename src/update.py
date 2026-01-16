
import sys
import os
import subprocess
from logger import logger

def check_update() -> None:
    """
    Checks for updates via git.
    If an update is available, prompts the user to pull.
    """
    # Check if we are in a git repo
    if not os.path.isdir(".git"):
        logger.debug("No .git directory found, skipping update check.")
        return

    print("\033[1;34m[*] Checking for updates...\033[1;m")
    try:
        # Fetch remote to get latest changes
        # check=False because if net fails, we just want to ignore updates silently or log debug
        fetch = subprocess.run("git fetch", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if fetch.returncode != 0:
            logger.warning("Failed to fetch updates (network issue?)")
            return

        # Check if behind upstream
        # git rev-list --left-right --count HEAD...@{u}
        # Returns: "ahead_count	behind_count"
        res = subprocess.run("git rev-list --left-right --count HEAD...@{u}", 
                             shell=True, capture_output=True, text=True)
        
        if res.returncode != 0:
            # Often happens if no upstream is tracked
            logger.debug("Could not verify upstream status.")
            return

        counts = res.stdout.strip().split()
        if len(counts) == 2:
            behind = int(counts[1])
            if behind > 0:
                logger.info(f"Update available: {behind} commits behind.")
                print(f"\n\033[1;33m[!] A new version is available! ({behind} commits pending)\033[1;m")
                ans = input("\033[1;32mDo you want to update now? [Y/n] > \033[1;m").strip().lower()
                
                if ans != 'n':
                    logger.info("User requested update")
                    print("\033[1;34m[*] Updating...\033[1;m")
                    pull = subprocess.run("git pull", shell=True)
                    if pull.returncode == 0:
                        print("\033[1;32m[+] Update successful! The script will now exit.\033[1;m")
                        print("\033[1;32m[+] Please restart to apply changes.\033[1;m")
                        sys.exit(0)
                    else:
                        logger.error("Git pull failed")
                        print("\033[1;31m[-] Update failed. Please check git status manually.\033[1;m")
            else:
                logger.debug("Branch is up to date.")
                # Optional: print "Up to date" to confirm check worked? 
                # User asked for "Check at startup", usually silent if nothing, but "Checking..." was printed.
                # Let's verify cleanly.
                print("\033[1;32m[+] System is up to date.\033[1;m\n")

    except Exception as e:
        logger.error(f"Error during update check: {e}")
