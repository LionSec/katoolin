#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
search.py: Search the Kali repostiories.

Invoke with: sudo PYTHONPATH=.. ./search.py
"""

import os
import katoolin3

if __name__ == "__main__":
    katoolin3.Sources.install()

    try:
        katoolin3.Apt.update()

        while True:
            search = input("Search: ")

            if len(search) > 0:
                os.system(f"apt show {search}")
    finally:
        katoolin3.Sources.uninstall()
        katoolin3.Apt.update()