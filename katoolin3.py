#!/usr/bin/python3
import os
import sys

# Ensure src/ is importable when running from the repo root.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from app import main


if __name__ == "__main__":
    main()
