#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
katoolin3 is a port of katoolin for python3.

Following packages arent available because they are on github or not in the repo:
    - ntop
    - ip2hosts
    - commix
    - dbpwaudit
    - gsd
    - inguma
    - gr-scan
    - bluepot
    - webshag
    - webslayer
    - evilgraid
    - capstone
    - distone3
    - regripper
    - inundator
    - dbpwaudit
    - thc-hydra
    - phrasendrescher
    - sqldict
    - wifresti
"""

__author__ = "s-h-3-l-l"
__credits__ = ["LionSec"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "s-h-3-l-l"
__status__ = "Production"

import os
from collections import namedtuple
import subprocess
from math import ceil

try:
    import apt
except ImportError:
    print("Please install the 'python-apt' package")
    exit(1)

# The list of kali programs available in the repo:
PACKAGES = {
    "Information Gathering" : [
        "acccheck",
        "ace-voip",
        "amap",
        "automater",
        "braa",
        "casefile",
        "cdpsnarf",
        "cisco-torch",
        "cookie-cadger",
        "copy-router-config",
        "dmitry",
        "dnmap",
        "dnsenum",
        "dnsmap",
        "dnsrecon",
        "dnstracer",
        "dnswalk",
        "dotdotpwn",
        "enum4linux",
        "enumiax",
        "exploitdb",
        "fierce",
        "firewalk",
        "fragroute",
        "fragrouter",
        "ghost-phisher",
        "golismero",
        "goofile",
        "lbd",
        "maltego-teeth",
        "masscan",
        "metagoofil",
        "miranda",
        "nmap",
        "p0f",
        "parsero",
        "recon-ng",
        "set",
        "smtp-user-enum",
        "snmpcheck",
        "sslcaudit",
        "sslsplit",
        "sslstrip",
        "sslyze",
        "thc-ipv6",
        "theharvester",
        "tlssled",
        "twofi",
        "urlcrazy",
        "wireshark",
        "wol-e",
        "xplico",
        "ismtp",
        "intrace",
        "hping3"
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
        "greenbone-security-assistant",
        "hexorbase",
        "jsql",
        "lynis",
        "nmap",
        "ohrwurm",
        "openvas-cli",
        "openvas-manager",
        "openvas-scanner",
        "oscanner",
        "powerfuzzer",
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
    "Wireless Attacks" : [
        "aircrack-ng",
        "asleap", 
        "bluelog", 
        "blueranger", 
        "bluesnarfer", 
        "bully", 
        "cowpatty", 
        "crackle", 
        "eapmd5pass", 
        "fern-wifi-cracker", 
        "ghost-phisher",
        "giskismet", 
        "gqrx", 
        "kalibrate-rtl", 
        "killerbee", 
        "kismet", 
        "mdk3", 
        "mfcuk", 
        "mfoc", 
        "mfterm", 
        "multimon-ng", 
        "pixiewps", 
        "reaver", 
        "redfang", 
        "spooftooph", 
        "wifi-honey", 
        "wifitap", 
        "wifite"
    ],
    "Web Applications" : [
        "apache-users", 
        "arachni", 
        "bbqsql", 
        "blindelephant", 
        "burpsuite", 
        "cutycapt", 
        "davtest", 
        "deblaze", 
        "dirb", 
        "dirbuster", 
        "fimap", 
        "funkload", 
        "grabber", 
        "jboss-autopwn", 
        "joomscan", 
        "jsql", 
        "maltego-teeth", 
        "padbuster", 
        "paros", 
        "parsero", 
        "plecost", 
        "powerfuzzer", 
        "proxystrike", 
        "recon-ng", 
        "skipfish", 
        "sqlmap", 
        "sqlninja", 
        "sqlsus", 
        "ua-tester", 
        "uniscan", 
        "vega", 
        "w3af", 
        "webscarab", 
        "websploit", 
        "wfuzz", 
        "wpscan", 
        "xsser", 
        "zaproxy"
    ],
    "Sniffing & Spoofing" : [
        "burpsuite", 
        "dnschef", 
        "fiked", 
        "hamster-sidejack", 
        "hexinject", 
        "iaxflood", 
        "inviteflood", 
        "ismtp", 
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
    "Maintaining Access" : [
        "cryptcat", 
        "cymothoa", 
        "dbd", 
        "dns2tcp", 
        "http-tunnel", 
        "httptunnel", 
        "intersect", 
        "nishang", 
        "polenum", 
        "powersploit", 
        "pwnat", 
        "ridenum", 
        "sbd", 
        "u3-pwn", 
        "webshells", 
        "weevely"
    ],
    "Reporting Tools" : [
        "casefile", 
        "cutycapt", 
        "dos2unix",  # what is that doing here ??
        "dradis", 
        "keepnote", 
        "magictree", 
        "metagoofil", 
        "nipper-ng", 
        "pipal"
    ],
    "Exploitation Tools" : [
        "armitage", 
        "backdoor-factory", 
        "cisco-auditing-tool", 
        "cisco-global-exploiter", 
        "cisco-ocs", 
        "cisco-torch", 
        "crackle", 
        "jboss-autopwn", 
        "linux-exploit-suggester", 
        "maltego-teeth", 
        "set", 
        "shellnoob", 
        "sqlmap", 
        "thc-ipv6", 
        "yersinia", 
        "beef-xss"
    ],
    "Forensics Tools" : [
        "binwalk", 
        "bulk-extractor", 
        "chntpw", 
        "cuckoo", 
        "dc3dd", 
        "ddrescue", 
        "dumpzilla", 
        "extundelete", 
        "foremost", 
        "galleta", 
        "guymager", 
        "iphone-backup-analyzer", 
        "p0f", 
        "pdf-parser", 
        "pdfid", 
        "pdgmail", 
        "peepdf", 
        "volatility", 
        "xplico"
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
    "Password Attacks" : [
        "acccheck", 
        "burpsuite", 
        "cewl", 
        "chntpw", 
        "cisco-auditing-tool", 
        "cmospwd", 
        "creddump", 
        "crunch", 
        "findmyhash", 
        "gpp-decrypt", 
        "hash-identifier", 
        "hexorbase", 
        "john", 
        "johnny", 
        "keimpx", 
        "maltego-teeth", 
        "maskprocessor", 
        "multiforcer", 
        "ncrack", 
        "oclgausscrack", 
        "pack", 
        "patator", 
        "polenum", 
        "rainbowcrack", 
        "rcracki-mt", 
        "rsmangler", 
        "statsprocessor", 
        "thc-pptp-bruter", 
        "truecrack", 
        "webscarab", 
        "wordlists", 
        "zaproxy"
    ],
    "Reverse Engineering" : [
        "apktool", 
        "dex2jar", 
        "python-diStorm3", 
        "edb-debugger", 
        "jad", 
        "javasnoop", 
        "JD", 
        "OllyDbg", 
        "smali", 
        "Valgrind", 
        "YARA"
    ],
    "Hardware Hacking" : [
        "android-sdk", 
        "apktool", 
        "arduino", 
        "dex2jar", 
        "sakis3g", 
        "smali"
    ],
    "Extra" : [
        "squid3"
    ]
}

class Color:
    """
    A list of colors for stylish terminal output according to
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

# Just a type used in Selection:
Choice = namedtuple("Choice", ["text", "value"])

class Selection:
    """
    This class encapsulates the procedure that presents
    a list of options to the user and let the user select
    one (or more!) of them.
    """
    def __init__(self, head=None):
        # The list of choices.
        # This is a dict because we wanna
        # forbid relative indexing:
        self._options = {}
        self._headline = head
        self._col_thresh = 10
        self._colpad = 2

    def add_choice(self, text, value):
        """
        Add an option to display
        """
        self._options[len(self._options)] = Choice(text, value)

    def __iter__(self):
        # THIS IS UGLY DONT LOOK AT IT

        # The maximum index of an option in the left column:
        max_i = ceil(max(self._options.keys()) / 2)

        # The maximum length that an option in the left column can have:
        max_l = (
            len(str(max_i))
            + 2
            + len(max(self._options.values(), key=lambda x: len(x.text)).text)
        )

        if self._headline is not None:
            yield ""
            yield self._headline

        for index in self._options:
            y = "{}) {}".format(
                index,
                self._options[index].text
            )

            if len(self._options) >= self._col_thresh:
                # Bring all entries in left column to fixed size:
                y += (" " * (max_l - len(y) + self._colpad))

                if max_i + index in self._options:
                    yield y + "{}) {}".format(
                        max_i + index,
                        self._options[max_i + index].text
                    )
                else:
                    if max(self._options) % 2 == 0:
                        yield y
                    break

            else:
                yield y

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
                n = int(input("> "))
                return self._options[n].value
            except (ValueError, KeyError):
                print("Invalid input")

    def get_choices(self):
        """
        The selection procedure where all options are listed
        and the user selects 1 or more.
        """
        for option in self:
            print(option)

        while True:
            try:
                n = input("> ")

                if len(n) == 0:
                    raise ValueError()

                return [
                    self._options[i].value for i in self._parse_selection(n)
                ]
            except (ValueError, KeyError):
                print("Invalid input")

class StepBack(BaseException):
    """
    A custom exception used in the submenus
    to get to the previous (sub)menu.
    This is also used for transferring
    status messages (only success) between the menu-layers.
    It is the opposite of VisibleError.
    """
    def __init__(self, msg=""):
        self._msg = msg
        super().__init__()

    def has_message(self):
        return self._msg != ""

    def __str__(self):
        """
        This is only used in the innermost submenus
        """
        return "{}{}{}".format(Color.green, self._msg, Color.reset)

class VisibleError(Exception):
    """
    An exception that will be displayed
    but will not change the program
    flow. This is catched by the innermost
    submenus.
    """
    def __init__(self, ex):
        super().__init__()
        self._msg = str(ex)
        self.args = ex.args

    def __str__(self):
        return "{}{}{}".format(Color.red, self._msg, Color.reset)

class Apt:
    """
    A wrapper for operations with aptitude
    """
    success_code = 0

    @classmethod
    def update(cls):
        if os.system("apt-get -m -y -q update") != cls.success_code:
            raise VisibleError(Exception("Apt update failed"))

    @classmethod
    def install(cls, pkgs):
        if len(pkgs) > 0:
            cmd = "apt-get -m -y -q install {}".format(" ".join(pkgs))
            if os.system(cmd) != cls.success_code:
                raise VisibleError(Exception("Apt install failed"))

class Sources:
    """
    A wrapper for handling the sources.list.d(5) file
    """
    file = "/etc/apt/sources.list.d/katoolin3.list"

    @classmethod
    def install(cls):
        if not os.path.exists(cls.file):
            try:
                with open(cls.file, "w") as f:
                    f.write("# This file was automatically created by katoolin3. DO NOT MODIFY\n")
                    f.write("deb http://http.kali.org/kali kali-rolling main contrib non-free\n")
            except OSError as e:
                raise VisibleError(e)

            subprocess.run([
                "apt-key", "adv",
                "--keyserver", "pool.sks-keyservers.net",
                "--recv-keys", "ED444FF07D8D0BF6"
            ])

    @classmethod
    def uninstall(cls):
        try:
            os.remove(cls.file)
        except OSError as e:
            raise VisibleError(e)

        # Since all parts of the program need a valid kali repository
        # exit the program now
        raise Exception("Successfully uninstalled. Exiting now...")

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
""".format(f=Color.red, b=Color.black, s=Color.red), end=Color.reset)
    print("""{} ~~~~~{{ Author: s-h-3-l-l | Homepage: https://github.com/s-h-3-l-l }}~~~~~
{}""".format(Color.white, Color.reset))

def install_all_packages():
    def get_all():
        for cat in PACKAGES:
            for pkg in PACKAGES[cat]:
                yield pkg

    Apt.install([*get_all()])

    for cat in PACKAGES:
        PACKAGES[cat] = []

    raise StepBack("Installed all packages")

def view_packages(cat):
    """
    Display the submenu for installing packages
    from a specific category.
    """
    while True:
        sel = Selection("Select a Package")

        for i, pkg in enumerate(PACKAGES[cat]):
            sel.add_choice(pkg, i)

        if len(PACKAGES[cat]) > 1:
            sel.add_choice("ALL", "All")
        sel.add_choice("BACK", None)

        choices = sel.get_choices()

        try:
            if len(choices) == 1:
                choice = choices[0]

                if choice is None:
                    raise StepBack()

                elif choice == "All":
                    Apt.install(PACKAGES[cat])
                    PACKAGES[cat] = []

                else:
                    Apt.install((PACKAGES[cat][choice],))
                    del PACKAGES[cat][choice]

            else:
                # when deleting items in the
                # middle of lists the items get shifted:
                moved = 0

                if "All" in choices or None in choices:
                    print("Invalid selection")
                    continue

                Apt.install([
                    PACKAGES[cat][i] for i in choices
                ])

                choices.sort()

                for i in choices:
                    del PACKAGES[cat][i - moved]
                    moved += 1

        except VisibleError as v:
            print(v)

def help():
    print("""The program flow of this program is realized by presenting
a list of options that the user can choose from.

When selecting packages you can select
more than one by passing a comma-separated list like
'0,1,2,3' or specifying a range like '12-24' or combine
those two '0,1,3-5,12'.
""", end="")

def view_categories():
    """
    Displays the list of categories.
    If the user selects "All" all packages
    are directly installed without going
    into the submenus for the categories.
    """
    sel = Selection("Select a Category")

    for cat in PACKAGES:
        sel.add_choice(cat, cat)

    if len(PACKAGES) > 1:
        sel.add_choice("INSTALL ALL", "All")
    sel.add_choice("BACK", None)

    while True:
        choice = sel.get_choice()

        if choice is None:
            raise StepBack()

        try:
            if choice == "All":
                install_all_packages()
            else:
                view_packages(choice)
        except VisibleError as v:
            print(v)
        except StepBack as s:
            if s.has_message():
                print(s)

def main():
    sel = Selection("Main Menu")
    sel.add_choice("Remove Kali Repositories", Sources.uninstall)
    sel.add_choice("View Categories", view_categories)
    sel.add_choice("Install Kali Menu", lambda: Apt.install(("kali-menu",)))
    sel.add_choice("Help", help)
    sel.add_choice("Exit", None)

    while True:
        choice = sel.get_choice()

        if choice is None:
            raise StepBack()

        try:
            choice()
        except StepBack as s:
            if s.has_message():
                print(s)
        except VisibleError as v:
            print(v)

def remove_unknown_packages():
    """
    Some packages in PACKAGES may be not
    available in different debian versions
    so this function deletes all packages
    from PACKAGES which are not in the APT
    cache.
    """
    # Only informational:
    not_found = 0

    with apt.Cache() as cache:
        for cat in PACKAGES:
            to_delete = []

            for i, pkg in enumerate(PACKAGES[cat]):
                try:
                    cache[pkg]
                except KeyError:
                    to_delete.append(i - len(to_delete))
                    not_found += 1

            for i in to_delete:
                del PACKAGES[cat][i]

    print("{} packages not in current repositories".format(not_found))

if __name__ == "__main__":
    try:
        print_logo()
        # Since every part of the program needs a valid
        # kali repository always make sure there is one:
        Sources.install()
        Apt.update()
        remove_unknown_packages()
        print()
        main()
    except (KeyboardInterrupt, StepBack):
        print()
    except Exception as e:
        print("{}{!s}{}".format(Color.red, e, Color.reset))
        exit(1)

    print("Goodbye")
    exit(0)
