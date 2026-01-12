import os
import subprocess


def run_shell(cmd):
    # Use the shell because many menu entries are plain one-liners.
    return subprocess.run(cmd, shell=True).returncode == 0


def run_shell_capture(cmd):
    # Capture output so we can show warnings from apt.
    proc = subprocess.run(
        cmd,
        shell=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if proc.stdout:
        print(proc.stdout, end="")
    return proc.returncode, proc.stdout or ""


def open_shell():
    print("\033[1;33mStarting shell... Type 'exit' to return to Katoolin3.\033[1;m")
    user_shell = os.environ.get("SHELL", "/bin/bash")
    subprocess.run(user_shell)
