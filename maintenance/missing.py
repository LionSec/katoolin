#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

"""
missing.py: Check if all packages in katoolin3s
            package list are in the repository.

Invoke with: sudo PYTHONPATH=.. ./missing.py
"""

import katoolin3

if __name__ == "__main__":
    katoolin3.Sources.install()

    try:
        apt_mgr = katoolin3.APTManager()
        apt_mgr.update()

        for pkg in katoolin3.get_all():
            if not apt_mgr.has_package(pkg):
                print(pkg)

    finally:
        katoolin3.Sources.uninstall()
        apt_mgr.update()
