#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

"""
missing.py: Check if all packages in katoolin3s
            package list are in the repository.

Invoke with: sudo PYTHONPATH=.. ./missing.py
"""

import apt

import katoolin3

if __name__ == "__main__":
    katoolin3.Sources.install()

    try:
        katoolin3.Apt.update()

        with apt.Cache() as cache:
            for pkg in katoolin3.get_all():
                try:
                    cache[pkg]
                except KeyError:
                    print(pkg)

    finally:
        katoolin3.Sources.uninstall()
        katoolin3.Apt.update()
