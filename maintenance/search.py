#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
search.py: Search the Kali repostiories.

Invoke with: sudo PYTHONPATH=.. ./search.py
"""

import os
import shlex
import katoolin3

if __name__ == "__main__":
    with katoolin3.APTManager(silent=True) as apt_mgr:
        while True:
            search = shlex.quote(input("Search: "))

            if search:
                if apt_mgr.has_package(search):
                    os.system(f"apt show {search}")
                else:
                    os.system(f"apt search {search}")
