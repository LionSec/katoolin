#!/usr/bin/env python3

"""
sort.py: Takes katoolin3s package list, sorts it and outputs
         it so that it can be directly copy-and-pasted into
         the source file.

Invoke with: PYTHONPATH=.. ./sort.py
"""

from katoolin3 import PACKAGES

outfile = "sorted.lst"

def sort_out():
    # Not very efficient but who cares
    yield "PACKAGES = {\n"
    for i, cat in enumerate(sorted(PACKAGES.keys())):
        yield f"    \"{cat}\" : [\n"

        for j, pkg in enumerate(sorted(PACKAGES[cat])):
            yield f"        \"{pkg}\""

            if j < len(PACKAGES[cat]) - 1:
                yield ",\n"
            else:
                yield "\n"

        yield "    ]"

        if i < len(PACKAGES) - 1:
            yield ",\n"
        else:
            yield "\n"
    yield "}\n"

with open(outfile, "w") as file:
    for line in sort_out():
        file.write(line)
