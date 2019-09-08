#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
katoolin3 is a port of katoolin for python3.
"""

__author__ = "s-h-3-l-l"
__credits__ = ["LionSec"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "s-h-3-l-l"
__status__ = "Production"

import os
from collections import namedtuple
from math import ceil
import shlex
import textwrap

try:
    import apt
except ImportError:
    print("Please install the 'python3-apt' package")
    exit(1)

# The list of kali programs available in the repo:
PACKAGES = {
    "Information Gathering" : [
        "ace-voip",
        "amap",
        "apt2",
        "arp-scan",
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
        "eyewitness",
        "fierce",
        "firewalk",
        "fragroute",
        "fragrouter",
        "ghost-phisher",
        "golismero",
        "goofile",
        "ident-user-enum",
        "inspy",
        "lbd",
        "maltego-teeth",
        "masscan",
        "metagoofil",
        "miranda",
        "nbtscan-unixwiz",
        "nikto",
        "nmap",
        "osrframework",
        "p0f",
        "parsero",
        "recon-ng",
        "set",
        "smbmap",
        "smtp-user-enum",
        "snmpcheck",
        "sparta",
        "sslcaudit",
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
        "openvas",
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
        "ghost-phisher",
        "gqrx", 
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
        "wifitap", 
        "wifite",
        "wifiphisher"
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
        "gobuster",
        "grabber", 
        "hurl",
        "jboss-autopwn", 
        "joomscan", 
        "jsql", 
        "maltego-teeth", 
        "nikto",
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
        "webscarab", 
        "websploit", 
        "wfuzz", 
        "whatweb",
        "wpscan", 
        "xsser", 
        "zaproxy"
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
    "Maintaining Access" : [
        "cryptcat", 
        "cymothoa", 
        "dbd", 
        "dns2tcp", 
        "httptunnel", 
        "intersect", 
        "nishang", 
        "polenum", 
        "powersploit", 
        "pwnat", 
        "ridenum", 
        "sbd", 
        "shellter",
        "u3-pwn", 
        "webshells", 
        "weevely"
    ],
    "Reporting Tools" : [
        "casefile", 
        "cutycapt", 
        "cherrytree",
        "dos2unix",  # what is that doing here ??
        "dradis", 
        "keepnote", 
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
        "commix",
        "exploitdb",
        "jboss-autopwn", 
        "linux-exploit-suggester", 
        "maltego-teeth", 
        "metasploit-framework",
        "msfpc",
        "routersploit",
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
        "p0f", 
        "pdf-parser", 
        "pdfid", 
        "pdgmail", 
        "peepdf", 
        "regripper",
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
        "burpsuite", 
        "brutespray",
        "cewl", 
        "chntpw", 
        "cisco-auditing-tool", 
        "cmospwd", 
        "creddump", 
        "crunch", 
        "crowbar",
        "findmyhash", 
        "gpp-decrypt", 
        "hashcat",
        "hash-identifier", 
        "hexorbase", 
        "hydra",
        "john", 
        "johnny", 
        "keimpx", 
        "maltego-teeth", 
        "maskprocessor", 
        "multiforcer", 
        "ncrack", 
        "oclgausscrack", 
        "ophcrack",
        "pack", 
        "patator", 
        "polenum", 
        "rainbowcrack", 
        "rcracki-mt", 
        "rsmangler", 
        "seclists",
        "statsprocessor", 
        "sqldict",
        "thc-pptp-bruter", 
        "truecrack", 
        "webscarab", 
        "wordlists", 
        "zaproxy"
    ],
    "Reverse Engineering" : [
        "apktool", 
        "dex2jar", 
        "python-distorm3", 
        "edb-debugger", 
        "jad", 
        "javasnoop", 
        "jd-gui", 
        "ollydbg", 
        "smali", 
        "valgrind", 
        "yara"
    ],
    "Hardware Hacking" : [
        "android-sdk", 
        "apktool", 
        "arduino", 
        "dex2jar", 
        "sakis3g", 
        "smali"
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
Choice = namedtuple("Choice", ["text", "value"])

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
    a list of options to the user and let the user select
    one (or more!) of them.
    """
    def __init__(self, head=None):
        # The list of choices.
        # This is a dict because we wanna
        # forbid relative indexing:
        self._options = {}
        self._headline = head
        self._col_thresh = 11
        self._colpad = 2
        self._delchar = "~"
        self._prompt = "kat> "

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
            yield "{}{}{}".format(Terminal.underscore, self._headline, Terminal.reset)

        for index in self._options:
            y = "{}) {}".format(
                index,
                self._options[index].text
            )

            # If there are a lot items display them columnwise:
            if len(self._options) >= self._col_thresh:
                # Bring all entries in left column to fixed size:
                y += (" " * (max_l - len(y) + self._colpad))

                if max_i + index in self._options:
                    yield y + "{}) {}".format(
                        max_i + index,
                        self._options[max_i + index].text
                    )
                else:
                    # If number options is odd display the last item
                    # only on the left column
                    if len(self._options) % 2 == 1:
                        yield y
                    break

            else:
                yield y

        yield ""

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
                n = int(input(self._prompt))
                return self._options[n].value
            except (ValueError, KeyError):
                print("Invalid input")

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
                ret = InstallList()

                if n[0] == self._delchar:
                    ret = UninstallList()
                    n = n[1:]

                if len(n) == 0:
                    raise ValueError()

                for i in self._parse_selection(n):
                    ret.append(self._options[i].value)

                return ret
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
        return "{}{}{}".format(Terminal.green, self._msg, Terminal.reset)

class VisibleError(Exception):
    """
    An exception that will be displayed
    but will not change the program
    flow.
    """
    def __init__(self, ex):
        super().__init__()
        self._msg = str(ex)
        self.args = ex.args

    def __str__(self):
        return "{}{}{}".format(Terminal.red, self._msg, Terminal.reset)

class APTManager:
    """
    A wrapper class for operations with aptitude
    """
    def __init__(self):
        self._cache = None
        self._success_code = 0

    def __enter__(self):
        self.update()
        return self

    def __exit__(self, *nil):
        self._cache.close()

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
        del self._cache
        self._cache = apt.Cache()

    def update(self):
        if os.system("apt-get -m -y -q update") != self._success_code:
            raise VisibleError(Exception("Apt update failed"))

        self.flush()

    def install(self, pkgs):
        """
        Install packages from iterator 'pkgs'
        """
        print("Reading package lists...")

        for pkg in pkgs:
            try:
                self._cache[pkg].mark_install()
            except KeyError:
                print("Warning: Could not find package '{}'".format(pkg))

        print("Fetching packages...")

        if not self._cache.commit():
            raise VisibleError(Exception("Apt install failed"))

        self.flush()

    def remove(self, pkgs):
        """
        Uninstall packages in iterator 'pkgs'
        """
        print("Reading package lists...")

        for pkg in pkgs:
            try:
                self._cache[pkg].mark_delete()
            except KeyError:
                print("Warning: Could not find package '{}'".format(pkg))

        print("Initiating removal...")

        if not self._cache.commit():
            raise VisibleError(Exception("Apt remove failed"))

        self.flush()

    def has_package(self, pkg):
        return self._cache.has_key(pkg)

    def upgrade(self, pkgs):
        print("Reading package lists...")

        for pkg in pkgs:
            try:
                if self._cache[pkg].is_installed and self._cache[pkg].is_upgradable:
                    self._cache[pkg].mark_upgrade()
            except KeyError:
                print("Warning: Could not find package '{}'".format(pkg))

        print("Initiating upgrade...")

        if not self._cache.commit():
            raise VisibleError(Exception("Apt upgrade failed"))

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
            if len(org.origin) > 0:
                ret = ret.union([org.origin])

        return ret

    def show(self, pkg):
        """
        Display some information about a package.
        """
        print("Package: ", pkg)

        if pkg in get_all():
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

        if len(key) > 0:
            os.system(f"apt search -qq {key};")

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

    @classmethod
    def uninstall(cls):
        try:
            os.remove(cls.file)
        except OSError as e:
            raise VisibleError(e)

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

def help():
    print("""
The program flow of this program is realized by presenting
a list of options that you can choose from.

When selecting packages you can select
more than one by passing a comma-separated list like
'0,1,2,3' or specifying a range like '12-24' or combining
those two '0,1,3-5,12'.

If you want to remove packages simply prepend '~' before a
string like above.
""".format(Terminal.black, Terminal.reset), end="")

def get_all():
    """
    Return all tools subsequently
    """
    for cat in PACKAGES:
        for pkg in PACKAGES[cat]:
            yield pkg

def install_all_packages():
    global apt_mgr
    sel = Selection("Install everything?")
    sel.add_choice("Yes", True)
    sel.add_choice("No", False)

    if sel.get_choice():
        apt_mgr.install(get_all())
        raise StepBack("Installed all packages")

def delete_all_packages():
    global apt_mgr
    sel = Selection("Delete everything?")
    sel.add_choice("Yes", True)
    sel.add_choice("No", False)

    if sel.get_choice():
        apt_mgr.remove(get_all())
        raise StepBack("Removed all packages")

def view_packages(cat):
    """
    Display the submenu for installing packages
    from a specific category.
    """
    global apt_mgr

    while True:
        sel = Selection("Select a Package")

        for pkg in PACKAGES[cat]:
            sel.add_choice(pkg, pkg)

        if len(PACKAGES[cat]) > 1:
            sel.add_choice("ALL", 0)
        sel.add_choice("BACK", 1)
        sel.add_choice("HELP", 2)

        choices = sel.get_choices()
        method = apt_mgr.install if isinstance(choices, InstallList) else apt_mgr.remove

        try:
            if len(choices) == 1:
                if choices[0] == 1:
                    raise StepBack()

                elif choices[0] == 0:
                    method(PACKAGES[cat])
                    continue

                elif choices[0] == 2:
                    help()
                    continue

            elif 1 in choices or 0 in choices or 2 in choices:
                print("Invalid selection")
                continue

            method(choices)

        except VisibleError as v:
            print(v)

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

    sel.add_choice("BACK", None)

    while True:
        choice = sel.get_choice()

        if choice is None:
            raise StepBack()

        try:
            view_packages(choice)
        except VisibleError as v:
            print(v)
        except StepBack as s:
            if s.has_message():
                print(s)

def list_installed_packages():
    global apt_mgr
    apt_mgr.flush()

    for pkg in sorted(set(get_all())):
        try:
            if apt_mgr[pkg].is_installed:
                print(pkg)
        except KeyError:
            pass

def search():
    """
    Searches the APT cache. If the search string is
    a package name display information about the package
    like 'apt show' otherwise treat it like a keyword for
    'apt search'.
    """
    global apt_mgr

    print()
    print("Enter a package name to get information about a package")
    print("or enter a keyword to search for packages...")
    print()
    key = input("Search: ")

    if apt_mgr.has_package(key):
        apt_mgr.show(key)
    else:
        apt_mgr.search(key)

def main():
    global apt_mgr
    sel = Selection("Main Menu")
    sel.add_choice("View Categories", view_categories)
    sel.add_choice("Install All", install_all_packages)
    sel.add_choice("Uninstall All", delete_all_packages)
    sel.add_choice("Search repository", search)
    sel.add_choice("List installed packages", list_installed_packages)
    sel.add_choice("Update all Kali packages", lambda: apt_mgr.upgrade(get_all()))
    sel.add_choice("Install Kali Menu", lambda: apt_mgr.install(["kali-menu"]))
    sel.add_choice("Uninstall old katoolin", lambda: handle_old_katoolin(force=True))
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

    except Exception as e:
        raise VisibleError(e)

    else:
        print("Successfully uninstalled the old katoolin")
        print()

if __name__ == "__main__":
    try:
        print_logo()
        handle_old_katoolin()
        Sources.install()
        with APTManager() as apt_mgr: # this will be used globally
            print()
            main()
    except (KeyboardInterrupt, StepBack):
        print()
    except Exception as e:
        print("{}{!s}{}".format(Terminal.red, e, Terminal.reset))
        exit(1)
    finally:
        try:
            Sources.uninstall()
        except VisibleError:
            exit(1)

        # Launch an update in the background:
        os.system("apt-get -m -y -qq update &")

    print("Goodbye")
    exit(0)
