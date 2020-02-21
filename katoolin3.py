#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# katoolin3 - Install Kali packages on your Debian/Ubuntu machine
# Copyright (C) 2019 s-h-3-l-l
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

"""
katoolin3 is a port of katoolin for python3.
"""

__author__ = "s-h-3-l-l"
__credits__ = ["LionSec"]
__license__ = "GPL"

import os
from collections import namedtuple
from math import ceil
import platform
import shlex
import textwrap

try:
    import apt
except ImportError:
    print("Please install the 'python3-apt' package")
    exit(1)

# The list of kali programs available in the repo with the format:
# {
#   category_name : [list of packages in category]
# }
# The category names have to be identical to those on
# https://tools.kali.org/tools-listing !
PACKAGES = {
    "Exploitation Tools" : [
        "armitage",
        "backdoor-factory",
        "beef-xss",
        "cisco-auditing-tool",
        "cisco-global-exploiter",
        "cisco-ocs",
        "cisco-torch",
        "commix",
        "crackle",
        "exploitdb",
        "jboss-autopwn",
        "linux-exploit-suggester",
        "metasploit-framework",
        "msfpc",
        "routersploit",
        "set",
        "shellnoob",
        "sqlmap",
        "thc-ipv6",
        "yersinia"
    ],
    "Forensics Tools" : [
        "bulk-extractor",
        "capstone-tool",
        "chntpw",
        "cuckoo",
        "dc3dd",
        "ddrescue",
        "dumpzilla",
        "extundelete",
        "foremost",
        "galleta",
        "guymager",
        "libdistorm3-3",
        "p0f",
        "pdf-parser",
        "pdfid",
        "peepdf",
        "python-distorm3",
        "python3-capstone",
        "python3-distorm3",
        "regripper",
        "volatility",
        "xplico"
    ],
    "Hardware Hacking" : [
        "android-sdk",
        "apktool",
        "arduino",
        "dex2jar",
        "sakis3g",
        "smali"
    ],
    "Information Gathering" : [
        "ace-voip",
        "amap",
        "apt2",
        "arp-scan",
        "bing-ip2hosts",
        "braa",
        "casefile",
        "cdpsnarf",
        "cisco-torch",
        "copy-router-config",
        "dmitry",
        "dnsenum",
        "dnsmap",
        "dnsrecon",
        "dnstracer",
        "dnswalk",
        "dotdotpwn",
        "enum4linux",
        "enumiax",
        "eyewitness",
        "faraday",
        "fierce",
        "firewalk",
        "fragroute",
        "fragrouter",
        "golismero",
        "goofile",
        "hping3",
        "ident-user-enum",
        "inspy",
        "intrace",
        "ismtp",
        "lbd",
        "masscan",
        "metagoofil",
        "nbtscan-unixwiz",
        "nikto",
        "nmap",
        "ntopng",
        "ntopng-data",
        "ntopng-doc",
        "osrframework",
        "p0f",
        "parsero",
        "qsslcaudit",
        "recon-ng",
        "set",
        "smbmap",
        "smtp-user-enum",
        "sntop",
        "sparta",
        "sslsplit",
        "sslstrip",
        "sslyze",
        "sublist3r",
        "thc-ipv6",
        "theharvester",
        "tlssled",
        "twofi",
        "unicornscan",
        "urlcrazy",
        "wireshark",
        "xplico"
    ],
    "Maintaining Access" : [
        "cryptcat",
        "cymothoa",
        "dbd",
        "dns2tcp",
        "httptunnel",
        "nishang",
        "polenum",
        "powersploit",
        "pwnat",
        "ridenum",
        "sbd",
        "shellter",
        "webshells",
        "weevely",
        "winexe"
    ],
    "Password Attacks" : [
        "brutespray",
        "burpsuite",
        "cewl",
        "chntpw",
        "cisco-auditing-tool",
        "cmospwd",
        "creddump7",
        "crowbar",
        "crunch",
        "gpp-decrypt",
        "hash-identifier",
        "hashcat",
        "hydra",
        "john",
        "johnny",
        "maskprocessor",
        "multiforcer",
        "ncrack",
        "oclgausscrack",
        "patator",
        "polenum",
        "rainbowcrack",
        "rcracki-mt",
        "rsmangler",
        "seclists",
        "sqldict",
        "statsprocessor",
        "thc-pptp-bruter",
        "truecrack",
        "webscarab",
        "wordlists",
        "zaproxy"
    ],
    "Reporting Tools" : [
        "casefile",
        "cherrytree",
        "cutycapt",
        "dos2unix",
        "dradis",
        "metagoofil",
        "nipper-ng",
        "pipal",
    ],
    "Reverse Engineering" : [
        "apktool",
        "dex2jar",
        "edb-debugger",
        "javasnoop",
        "jd-gui",
        "ollydbg",
        "python-distorm3",
        "python3-distorm3",
        "smali",
        "valgrind",
        "yara"
    ],
    "Sniffing & Spoofing" : [
        "bettercap",
        "burpsuite",
        "dnschef",
        "fiked",
        "hamster-sidejack",
        "hexinject",
        "iaxflood",
        "inviteflood",
        "ismtp",
        "isr-evilgrade",
        "mitmproxy",
        "ohrwurm",
        "protos-sip",
        "rebind",
        "responder",
        "rtpbreak",
        "rtpinsertsound",
        "rtpmixsound",
        "sctpscan",
        "siparmyknife",
        "sipp",
        "sipvicious",
        "sniffjoke",
        "sslsplit",
        "sslstrip",
        "thc-ipv6",
        "voiphopper",
        "webscarab",
        "wifi-honey",
        "wireshark",
        "xspy",
        "yersinia",
        "zaproxy"
    ],
    "Stress Testing" : [
        "dhcpig",
        "funkload",
        "iaxflood",
        "inviteflood",
        "ipv6-toolkit",
        "mdk3",
        "reaver",
        "rtpflood",
        "slowhttptest",
        "t50",
        "termineter",
        "thc-ipv6",
        "thc-ssl-dos"
    ],
    "Vulnerability Analysis" : [
        "bbqsql",
        "bed",
        "cisco-auditing-tool",
        "cisco-global-exploiter",
        "cisco-ocs",
        "cisco-torch",
        "copy-router-config",
        "doona",
        "dotdotpwn",
        "jsql",
        "lynis",
        "nmap",
        "ohrwurm",
        "openvas",
        "oscanner",
        "sfuzz",
        "sidguesser",
        "siparmyknife",
        "sqlmap",
        "sqlninja",
        "sqlsus",
        "thc-ipv6",
        "tnscmd10g",
        "unix-privesc-check",
        "yersinia"
    ],
    "Web Applications" : [
        "apache-users",
        "arachni",
        "bbqsql",
        "burpsuite",
        "cutycapt",
        "davtest",
        "dirb",
        "dirbuster",
        "funkload",
        "gobuster",
        "hurl",
        "jboss-autopwn",
        "joomscan",
        "jsql",
        "nikto",
        "padbuster",
        "paros",
        "parsero",
        "plecost",
        "recon-ng",
        "skipfish",
        "sqlmap",
        "sqlninja",
        "sqlsus",
        "uniscan",
        "webscarab",
        "websploit",
        "wfuzz",
        "whatweb",
        "wpscan",
        "xsser",
        "zaproxy"
    ],
    "Wireless Attacks" : [
        "aircrack-ng",
        "airgraph-ng",
        "asleap",
        "bluelog",
        "blueranger",
        "bluesnarfer",
        "bully",
        "cowpatty",
        "crackle",
        "eapmd5pass",
        "fern-wifi-cracker",
        "freeradius-wpe",
        "hostapd-wpe",
        "kalibrate-rtl",
        "killerbee",
        "kismet",
        "mdk3",
        "mfcuk",
        "mfoc",
        "mfterm",
        "multimon-ng",
        "pixiewps",
        "pyrit",
        "reaver",
        "redfang",
        "rtlsdr-scanner",
        "spooftooph",
        "wifi-honey",
        "wifiphisher",
        "wifite"
    ]
}

class Terminal:
    """
    A list of settings for stylish terminal output according to
    http://www.termsys.demon.co.uk/vtansi.htm
    """
    black = "\033[1;30m"
    red = "\033[1;31m"
    green = "\033[1;32m"
    yellow = "\033[1;33m"
    blue = "\033[1;34m"
    magenta = "\033[1;35m"
    cyan = "\033[1;36m"
    white = "\033[1;37m"
    reset = "\033[0m"
    underscore = "\033[4m"

# Just some types used in Selection:
Choice = namedtuple("Choice", ["text", "value", "color"])

class InstallList(list):
    """
    If a list is wrapped in this class it means that
    the items in the list are packages and they shall
    be installed.
    """

class UninstallList(list):
    """
    If a list is wrapped in this class it means that
    the items in the list are packages and they shall
    be uninstalled.
    """

class Selection:
    """
    This class encapsulates the procedure that presents
    a list of options to the user and lets the user select
    one (or more!) of them.
    """
    # Some values with special meaning.
    # These are complex because they have
    # to be different from anything that
    # would make sense in a selection (numbers, strings, etc.)
    ALL = complex(-1, -1)
    BACK = complex(-2, -2)
    HELP = complex(-3, -3)

    def __init__(self, head=None):
        # The list of choices.
        # This is a dict because we wanna
        # forbid relative indexing when
        # negative values are allowed:
        self._options = {}
        self._headline = head
        self._col_thresh = 11
        self._colpad = 2
        self._delchar = "~"
        self._infochar = "?"
        self._repeat = "!!"
        self._prompt = "kat> "

    def _option_string(self, index):
        """
        Given an index for the option storage return
        how the option will be presented
        """
        return "{}) {}".format(index, self._options[index].text)

    def add_choice(self, text, value, color=""):
        """
        Add an option to display
        """
        self._options[len(self._options)] = Choice(text, value, color)

    def __iter__(self):
        """
        Subsequently return the options formatted in columns
        """
        # The number of options in the left column:
        num_left = len(self._options)

        if num_left >= self._col_thresh:
            num_left = ceil(num_left / 2)

        # The maximum length an option on the left has:
        max_left = max(
            map(
                lambda item: len(self._option_string(item[0])),
                filter(
                    lambda item: item[0] < num_left,
                    self._options.items()
                )
            )
        )

        # First the headline
        if self._headline is not None:
            yield ""
            yield Terminal.underscore + self._headline + Terminal.reset

        # Then the columns:
        for i in range(num_left):
            # Left column:
            left = self._option_string(i)
            filler = " " * (max_left - len(left) + self._colpad)
            left = self._options[i].color + left + Terminal.reset

            # Right column:
            right_index = num_left + i

            if right_index in self._options:
                right = self._option_string(right_index)
                right = self._options[right_index].color + right + Terminal.reset
            else:
                right = ""

            yield left + filler + right

        yield ""

    def __len__(self):
        return len(self._options)

    def _parse_selection(self, sel):
        """
        Expects a string like '1,3-5,7'
        and parses it into the corresponding
        numbers [1,3,4,5,7].
        Duplicates are eliminated.
        Negative values are not allowed.
        """
        ret = set()
        sel = sel.replace(" ", "")

        for i in sel.split(","):
            if "-" in i:
                from_, to = map(int, i.split("-"))

                if from_ < 0:
                    raise ValueError()

                ret |= set(range(from_, to + 1))
            else:
                ret |= set([int(i)])

        return ret

    def get_choice(self):
        """
        The selection procedure where all options are listed
        and the user selects 1.
        """
        for option in self:
            print(option)

        while True:
            try:
                n = input(self._prompt)

                if n == self._repeat:
                    for option in self:
                        print(option)
                    continue

                n = int(n)
                return self._options[n].value
            except (ValueError, KeyError):
                print("Invalid input, please try again")

    def get_choices(self):
        """
        The selection procedure where all options are listed
        and the user selects 1 or more.
        This is only used for package selection. Thus the return
        value is a special list that indicates whether the selected
        packages shall be installed or uninstalled.
        """
        for option in self:
            print(option)

        while True:
            try:
                n = input(self._prompt)

                if n == self._repeat:
                    for option in self:
                        print(option)
                    continue

                ret = InstallList()

                if n[-1] == self._infochar:
                    APT.show(self._options[int(n[:-1])].value)
                    continue

                if n[0] == self._delchar:
                    ret = UninstallList()
                    n = n[1:]

                if not n:
                    raise ValueError()

                for i in self._parse_selection(n):
                    ret.append(self._options[i].value)

                return ret
            except (ValueError, KeyError):
                print("Invalid input, please try again")

class StepBack(BaseException):
    """
    A custom exception used in the submenus
    to get to the previous (sub)menu.
    This is also used for transferring
    status messages (only success) between the menu-layers.
    It is the opposite of VisibleError.
    """
    def __init__(self, msg=""):
        super().__init__()
        self._msg = msg

    def has_message(self):
        return self._msg != ""

    def __str__(self):
        """
        This is only used in the innermost submenus
        """
        return Terminal.green + self._msg + Terminal.reset

class VisibleError(Exception):
    """
    A wrapper for an exception whose message will be displayed
    but will not stop the program.

    Invoke this only with
        raise VisibleError() from <Exception>
    to ensure that the __cause__ attribute gets
    set properly.
    """
    def __str__(self):
        return Terminal.red + str(self.__cause__) + Terminal.reset

class APTException(Exception):
    """
    An exception that indicates an error with APTManager.
    """

class APTManager:
    """
    A wrapper class for operations with aptitude
    """
    sources_file = "/etc/apt/sources.list.d/katoolin3.list"

    def __init__(self, silent=False):
        self._cache = None
        self._success_code = 0
        self._silent = silent

    def __enter__(self):
        """
        Installs the sources file and updates the APT cache.
        """
        arch = detect_arch()
        
        if arch:
            arch = "[arch={}]".format(arch)
            
        try:
            with open(self.sources_file, "w") as file:
                file.write("# This file was automatically created by katoolin3. DO NOT MODIFY\n")
                file.write("deb {} http://http.kali.org/kali kali-rolling main contrib non-free\n".format(arch))
        except OSError as e:
            raise VisibleError() from e

        self.update()
        return self

    def __exit__(self, *nil):
        try:
            os.remove(self.sources_file)
        except OSError as e:
            raise VisibleError() from e
        finally:
            self._cache.close()
            # Launch update in background
            os.system("apt-get -m -y -qq update &")

    def __getitem__(self, item):
        """
        This is used to retrieve a package by name.
        """
        return self._cache[item]

    def flush(self):
        """
        Reload new package information into the cache.

        Unfortunately I couldnt find a better way to
        do this. The python3-apt-API seems uncomplete
        on this matter.
        """
        if self._cache is not None:
            self._cache.close()
        self._cache = apt.Cache()

    def update(self):
        if os.system(
                "apt-get -m -y {} update".format("-qq" if self._silent else "-q")
        ) != self._success_code:
            raise VisibleError() from APTException("Apt update failed")

        self.flush()

    def install(self, pkgs):
        """
        Install packages from iterator 'pkgs'
        """
        if self._cache.dpkg_journal_dirty:
            raise VisibleError() from Exception("Your dpkg is in an unsafe state. Run 'sudo dpkg --configure -a' to fix this.")
        
        print("Reading package lists...")
        num = 0

        for pkg in pkgs:
            try:
                if not self._cache[pkg].is_installed:
                    self._cache[pkg].mark_install()
                    
                    if self._cache[pkg].marked_install:
                        num += 1
            except KeyError:
                print("Warning: Could not find package '{}'".format(pkg))
            except SystemError as s:
                print("Error with package {}: {}".format(pkg, s))
                print("Trying to ignore this...")
                self._cache[pkg].mark_delete()

        if num == 0:
            raise StepBack("Nothing to install")

        print("Installing {} package{}...".format(num, 's' if num > 1 else ''))

        try:
            self._cache.commit(fetch_progress=apt.progress.text.AcquireProgress())
        except SystemError as s:
            raise VisibleError() from APTException("Installation of some packages failed ({})".format(s))

        self.flush()

    def remove(self, pkgs):
        """
        Uninstall packages in iterator 'pkgs'
        """
        if self._cache.dpkg_journal_dirty:
            raise VisibleError() from Exception("Your dpkg is in an unsafe state. Run 'sudo dpkg --configure -a' to fix this.")
        
        print("Reading package lists...")
        num = 0

        for pkg in pkgs:
            try:
                if self._cache[pkg].is_installed:
                    self._cache[pkg].mark_delete()
                    num += 1
            except KeyError:
                print("Warning: Could not find package '{}'".format(pkg))
            except SystemError as e:
                raise VisibleError() from e

        if num == 0:
            raise StepBack("Nothing to remove")

        print("Removing {} package{}...".format(num, 's' if num > 1 else ''))

        try:
            self._cache.commit()
        except SystemError as s:
            raise VisibleError() from APTException("Removal failed: " + str(s))

        self.flush()

    def has_package(self, pkg):
        return self._cache.has_key(pkg)

    def _pkg_status(self, pkg):
        """
        Return information about the status of a package.
        pkg = Package object
        """
        if pkg.is_installed:
            yield "Installed"
        else:
            yield "Not installed"

        if pkg.is_upgradable:
            yield "Not up to date"

    def _pkg_categories(self, pkg):
        """
        Return the categories where a package is in (1 or more).
        pkg = package name as string
        """
        for cat in PACKAGES:
            if pkg in PACKAGES[cat]:
                yield cat
                continue

    def _pkg_versions(self, pkg):
        """
        Return all versions.
        pkg = Package object
        """
        for version in pkg.versions:
            yield str(version).split("=")[-1]

    def _pkg_depends(self, pkg):
        """
        Return all dependencies.
        pkg = Package object
        """
        for dep in pkg.candidate.dependencies:
            yield dep.rawstr

    def _pkg_origins(self, pkg):
        """
        Return the origins of the package.
        pkg = Package object
        """
        ret = set()

        for org in pkg.candidate.origins:
            if org.origin:
                ret = ret.union([org.origin])

        return ret

    def show(self, pkg):
        """
        Display some information about a package.
        """
        print("Package: ", pkg)

        if pkg in all_packages():
            print("Category:", ", ".join(self._pkg_categories(pkg)))

        pkg = self._cache[pkg]

        print("Status:  ", ", ".join(self._pkg_status(pkg)))
        print("Version: ", ", ".join(self._pkg_versions(pkg)))
        print("Depends: ", ", ".join(self._pkg_depends(pkg)))
        print("Homepage:", pkg.candidate.homepage)
        print("Repo:    ", ", ".join(self._pkg_origins(pkg)))
        print(textwrap.fill(pkg.candidate.description, width=50))
        print()

    def search(self, key):
        """
        Search for keywords in the apt cache.

        I haven't found a solution with the APT-API.
        """
        key = shlex.quote(key)

        if key:
            os.system("apt search -qq {};".format(key))

def detect_arch(default=""):
    """
    Detect if we are on an 64-bit or 32-bit system
    """
    mapping = {
        "amd64" : "amd64",
        "x86_64" : "amd64",
        "i386" : "i386",
        "x86" : "i386"
    }
    
    try:
        return mapping[platform.machine().lower()]
    except KeyError:
        return default

def print_logo():
    """
    The obligatory ascii art
    """
    print("""
 {f}██{b}╗  {f}██{b}╗ {f}█████{b}╗ {f}████████{b}╗ {f}██████{b}╗  {f}██████{b}╗ {f}██{b}╗     {f}██{b}╗{f}███{b}╗   {f}██{b}╗{s}██████{b}╗
 {f}██{b}║ {f}██{b}╔╝{f}██{b}╔══{f}██{b}╗╚══{f}██{b}╔══╝{f}██{b}╔═══{f}██{b}╗{f}██{b}╔═══{f}██{b}╗{f}██{b}║     {f}██{b}║{f}████{b}╗  {f}██{b}║╚════{s}██{b}╗
 {f}█████{b}╔╝ {f}███████{b}║   {f}██{b}║   {f}██{b}║   {f}██{b}║{f}██{b}║   {f}██{b}║{f}██{b}║     {f}██{b}║{f}██{b}╔{f}██{b}╗ {f}██{b}║ {s}█████{b}╔╝
 {f}██{b}╔═{f}██{b}╗ {f}██{b}╔══{f}██{b}║   {f}██{b}║   {f}██{b}║   {f}██{b}║{f}██{b}║   {f}██{b}║{f}██{b}║     {f}██{b}║{f}██{b}║╚{f}██{b}╗{f}██{b}║ ╚═══{s}██{b}╗
 {f}██{b}║  {f}██{b}╗{f}██{b}║  {f}██{b}║   {f}██{b}║   ╚{f}██████{b}╔╝╚{f}██████{b}╔╝{f}███████{b}╗{f}██{b}║{f}██{b}║ ╚{f}████{b}║{s}██████{b}╔╝
 {b}╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝╚═════╝
""".format(f=Terminal.red, b=Terminal.black, s=Terminal.red), end=Terminal.reset)
    print("""{} ~~~~~{{ Author: s-h-3-l-l | Homepage: https://github.com/s-h-3-l-l }}~~~~~
{}""".format(Terminal.white, Terminal.reset))
    print()

def print_help():
    print("""
The program flow of this program is realized by presenting
a list of options that you can choose from.

When selecting packages you can select
more than one by passing a comma-separated list like
'0,1,2,3' or specifying a range like '12-24' or combining
those two '0,1,3-5,12'.

If you want to remove packages simply prepend '~' before a
string like above.

If you want information about a specific package
presented to you enter the number of the package
followed by a '?'.

If the list of options gets out of sight type '!!'
to print it again.

Packages which you have already installed are shown
in {}this color{}.
""".format(Terminal.black, Terminal.reset))

    input("Press ENTER to continue...")

def all_packages():
    """
    Return all tools subsequently
    """
    for cat in PACKAGES:
        for pkg in PACKAGES[cat]:
            yield pkg

def install_all_packages():
    sel = Selection("Install everything?")
    sel.add_choice("Yes", True)
    sel.add_choice("No", False)

    if sel.get_choice():
        APT.install(all_packages())
        raise StepBack("Installed all packages")

def delete_all_packages():
    sel = Selection("Delete everything?")
    sel.add_choice("Yes", True)
    sel.add_choice("No", False)

    if sel.get_choice():
        APT.remove(all_packages())
        raise StepBack("Removed all packages")

def nice_name(pkg):
    """
    Beautify a package name a bit.
    """
    parts = pkg.split("-")

    # If the package name has no dashes keep it this way
    if len(parts) == 1:
        return parts[0].lower()

    # Remove python indicator in package names
    if parts[0].startswith("python"):
        del parts[0]

    # If the package ends with "-ng" keep it this way
    if parts[-1] == "ng":
        return "-".join(parts)

    return " ".join(parts).title()

def view_packages(cat):
    """
    Display the submenu for installing packages
    from a specific category.
    """
    while True:
        sel = Selection("Select a Package")

        for pkg in sorted(PACKAGES[cat]):
            nice_pkg = nice_name(pkg)

            try:
                if APT[pkg].is_installed:
                    sel.add_choice(nice_pkg, pkg, Terminal.black)
                else:
                    sel.add_choice(nice_pkg, pkg)
            except KeyError:
                pass

        if len(sel) > 1:
            sel.add_choice("ALL", Selection.ALL)
        sel.add_choice("HELP", Selection.HELP)
        sel.add_choice("BACK", Selection.BACK)

        choices = sel.get_choices()
        method = APT.install if isinstance(choices, InstallList) else APT.remove

        try:
            if len(choices) == 1:
                if choices[0] == Selection.BACK:
                    break

                elif choices[0] == Selection.HELP:
                    print_help()
                    continue

                elif choices[0] == Selection.ALL:
                    choices = PACKAGES[cat]

            elif (Selection.HELP in choices
                  or Selection.BACK in choices
                  or Selection.ALL in choices):
                print("Invalid selection")
                continue

            method(choices)

        except VisibleError as v:
            print(v)

        except StepBack as s:
            if s.has_message():
                print(s)

def view_categories():
    """
    Displays the list of categories.
    """
    sel = Selection("Select a Category")

    for cat in sorted(PACKAGES):
        sel.add_choice(cat, cat)

    sel.add_choice("HELP", Selection.HELP)
    sel.add_choice("BACK", Selection.BACK)

    while True:
        choice = sel.get_choice()

        if choice == Selection.BACK:
            raise StepBack()
        elif choice == Selection.HELP:
            print_help()
            continue

        try:
            view_packages(choice)
        except VisibleError as v:
            print(v)
        except StepBack as s:
            if s.has_message():
                print(s)

def list_installed_packages():
    APT.flush()

    for pkg in sorted(set(all_packages())):
        try:
            if APT[pkg].is_installed:
                print(nice_name(pkg))
        except KeyError:
            pass
            
def list_not_installed_packages():
    APT.flush()

    for pkg in sorted(set(all_packages())):
        try:
            if not APT[pkg].is_installed:
                print(nice_name(pkg))
        except KeyError:
            pass

def search():
    """
    Searches the APT cache. If the search string is
    a package name display information about the package
    like 'apt show' otherwise treat it like a keyword for
    'apt search'.
    """
    print()
    print("Enter a package name to get information about a package")
    print("or enter a keyword to search for packages...")
    print()
    key = input("Search: ")

    if APT.has_package(key):
        APT.show(key)
    else:
        APT.search(key)

def main():
    sel = Selection("Main Menu")
    sel.add_choice("View Categories", view_categories)
    sel.add_choice("Install All", install_all_packages)
    sel.add_choice("Uninstall All", delete_all_packages)
    sel.add_choice("Search repository", search)
    sel.add_choice("List installed packages", list_installed_packages)
    sel.add_choice("List not installed packages", list_not_installed_packages)
    sel.add_choice("Install Kali Menu", lambda: APT.install(["kali-menu"]))
    sel.add_choice("Uninstall old katoolin", lambda: handle_old_katoolin(force=True))
    sel.add_choice("Help", print_help)
    sel.add_choice("Exit", Selection.BACK)

    while True:
        choice = sel.get_choice()

        if choice == Selection.BACK:
            raise StepBack()

        try:
            choice()
        except StepBack as s:
            if s.has_message():
                print(s)
        except VisibleError as v:
            print(v)

def handle_old_katoolin(force=False):
    """
    Detect the old katoolin installation and ask the user
    to delete it or force the uninstallation.
    """
    try:
        with open("/etc/apt/sources.list", "r+") as file:
            file.seek(0)
            lines = []
            seen = False

            for line in file:
                if not "//http.kali.org/kali" in line and not "Added by Katoolin" in line:
                    lines.append(line)
                else:
                    seen = True

            if not seen:
                if force:
                    print("It doesn't look like the old katoolin is installed")
                return

            if not force:
                print("The old katoolin is still installed on your system.")
                print("To avoid any inconveniences it is recommended to")
                print("delete the configuration of the old katoolin.")
                sel = Selection("Delete old katoolin configuration?")
                sel.add_choice("Yes", True)
                sel.add_choice("No", False)

                if not sel.get_choice():
                    print("This might be dangerous. You have been warned...")
                    return

            file.seek(0)
            file.write("".join(lines))
            file.truncate()

    except OSError as e:
        raise VisibleError() from e

    else:
        print("Successfully uninstalled the old katoolin")
        print()
        
def print_disclaimer():
    print("""
{}DISCLAIMER:
Don't update your packages, upgrade your system or
modify your package cache in any other way while 
katoolin3 is still running!
{}""".format(Terminal.red, Terminal.reset))

if __name__ == "__main__":
    try:
        print_logo()
        handle_old_katoolin()
        with APTManager() as APT: # this will be used globally
            print()
            print_disclaimer()
            main()
    except (KeyboardInterrupt, StepBack):
        print()
    except VisibleError as v:
        print(v)
        exit(1)

    print("Goodbye")
    exit(0)
