#!/usr/bin/env python3

import apt

cache = apt.Cache()
got = set()

def find_deps(pkg):
    global got
    print(pkg)
    obj = cache[pkg]
    
    if pkg in got or obj.is_installed:
        return

    got |= set([pkg])


    for dep in obj.candidate.dependencies:
        if dep.rawtype.lower().endswith("depends"):
            for elem in dep:
                find_deps(elem.name)

find_deps("p0f")
