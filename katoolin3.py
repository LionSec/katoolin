#!/usr/bin/python3

import os
import sys
import traceback
import subprocess


def setup():
    if os.geteuid() != 0:
        print(
            "You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting.")
        return False
    os.system("clear")
    return True


def run_shell(cmd):
    return subprocess.run(cmd, shell=True).returncode == 0


def add_kali_key():
    cmd = (
        "wget -q -O - https://archive.kali.org/archive-key.asc | "
        "gpg --dearmor | tee /usr/share/keyrings/kali-archive-keyring.gpg >/dev/null"
    )
    if not run_shell(cmd):
        return False
    try:
        os.chmod("/usr/share/keyrings/kali-archive-keyring.gpg", 0o644)
    except OSError:
        return False
    return True


def write_kali_repo():
    repo_path = "/etc/apt/sources.list.d/katoolin.list"
    repo_line = (
        "deb [signed-by=/usr/share/keyrings/kali-archive-keyring.gpg] "
        "https://http.kali.org/kali kali-rolling main contrib non-free\n"
    )
    if os.path.exists(repo_path):
        return "exists"
    try:
        with open(repo_path, "w") as repo_file:
            repo_file.write("# Kali linux repositories | Added by Katoolin\n")
            repo_file.write(repo_line)
    except IOError:
        return "error"
    return "added"


def remove_kali_repo():
    repo_path = "/etc/apt/sources.list.d/katoolin.list"
    removed_repo = False
    if os.path.exists(repo_path):
        os.remove(repo_path)
        removed_repo = True
    sources_path = "/etc/apt/sources.list"
    delete_list = [
        "# Kali linux repositories | Added by Katoolin\n",
        "deb http://http.kali.org/kali kali-rolling main contrib non-free\n",
        "deb [signed-by=/usr/share/keyrings/kali-archive-keyring.gpg] "
        "https://http.kali.org/kali kali-rolling main contrib non-free\n",
    ]
    try:
        with open(sources_path, "r") as fin:
            lines = fin.readlines()
        with open(sources_path, "w") as fout:
            for line in lines:
                if line in delete_list:
                    removed_repo = True
                    continue
                fout.write(line)
    except IOError:
        return False
    return removed_repo


def help_menu():
    print("****************** +Commands+ ******************\n")
    print("\033[1;32mback\033[1;m 	\033[1;33mGo back\033[1;m")
    print("\033[1;32mgohome\033[1;m	\033[1;33mGo to the main menu\033[1;m")
    print("\033[1;32mhelp\033[1;m 	\033[1;33mShow this help menu\033[1;m")
    print("\033[1;32mExit\033[1;m	\033[1;33mExit the script\033[1;m")


def main_menu():
    print("")
    print(" $$\   $$\           $$\                         $$\ $$\            $$$$$$\  ")
    print(" $$ | $$  |          $$ |                        $$ |\__|          $$ ___$$\ ")
    print(" $$ |$$  / $$$$$$\ $$$$$$\    $$$$$$\   $$$$$$\  $$ |$$\ $$$$$$$\  \_/   $$ |")
    print(" $$$$$  /  \____$$\\_$$  _|  $$  __$$\ $$  __$$\ $$ |$$ |$$  __$$\   $$$$$ / ")
    print(" $$  $$<   $$$$$$$ | \033[1;34mKali-Linux tools installer\033[1;m |$$ |$$ |$$ |  $$ |  \___$$\ ")
    print(" \033[1;34m$$ |\$$\ $$  __$$ | $$ |$$\ $$ |  $$ |$$ |  $$ |$$ |$$ |$$ |  $$ |$$\   $$ |")
    print(" $$ | \$$\\$$$$$$$  | \$$$$  |\$$$$$$  |\$$$$$$  |$$ |$$ |$$ |  $$ |\$$$$$$  |")
    print(" \__|  \__|\_______|  \____/  \______/  \______/ \__|\__|\__|  \__| \______/ V3.0\033[1;m")
    print("")
    print("")
    print(" \033[1;32m+ -- -- +=[ Original Script by: LionSec | Homepage: www.neodrix.com \033[1;m")
    print(" \033[1;32m+ -- -- +=[ Rewrites and maintained by: 0xGuigui\033[1;m")
    print(" \033[1;32m+ -- -- +=[ Latest update: 1/12/2026\033[1;m")
    print("")
    print("")
    print("\033[1;91m[W] Before updating and upgrading your system, please remove all Kali-linux repositories to "
          "avoid any kind of problem.\033[1;m")
    print("\033[1;91m[W] In some cases, Kali-Linux repositories can destabilize your system or worse, completely "
          "destroy it.\033[1;m")
    print("")


def main():
    try:
        if not setup():
            return
        main_menu()

        def initio1():
            while True:
                print("1) Add Kali repositories & Update")
                print("2) View Categories")
                print("3) Install classicmenu indicator")
                print("4) Install Kali menu")
                print("5) Help")
                print("")

                option0 = input("\033[1;36mkat > \033[1;m")
                if option0 == "exit" or option0 == "quit":
                    print("Shutdown requested...Goodbye...")
                    sys.exit()
                while option0 == "1":
                    print("")
                    print("1) Add kali linux repositories")
                    print("2) Update")
                    print("3) Remove all kali linux repositories")
                    print("4) View the contents of sources.list file")
                    print("")
                    repo = input(
                        "\033[1;32mWhat do you want to do ?> \033[1;m")
                    if repo == "1":
                        if not add_kali_key():
                            print(
                                "\033[1;31m\nFailed to add Kali repository key.\n\033[1;m")
                            continue
                        repo_status = write_kali_repo()
                        if repo_status == "added":
                            print(
                                "\033[1;32m\nKali repositories have been added.\n\033[1;m")
                        elif repo_status == "exists":
                            print(
                                "\033[1;33m\nKali repositories are already present.\n\033[1;m")
                        else:
                            print(
                                "\033[1;31m\nFailed to add Kali repositories.\n\033[1;m")
                    elif repo == "2":
                        if run_shell("apt-get update"):
                            print("\033[1;32m\nUpdate completed.\n\033[1;m")
                        else:
                            print("\033[1;31m\nUpdate failed.\n\033[1;m")
                    elif repo == "3":
                        removed = remove_kali_repo()
                        if removed:
                            print(
                                "\033[1;31m\nAll kali linux repositories have been deleted !\n\033[1;m")
                        else:
                            print(
                                "\033[1;33m\nNo Kali repositories were found.\n\033[1;m")
                    elif repo == "back":
                        initio1()
                    elif repo == "gohome":
                        initio1()
                    elif repo == "exit" or repo == "quit":
                        print("Shutdown requested...Goodbye...")
                        sys.exit()
                    elif repo == "4":
                        file = open('/etc/apt/sources.list', 'r')

                        print(file.read())
                    else:
                        print(
                            "\033[1;31mSorry, that was an invalid command!\033[1;m")

                if option0 == "3":
                    print(''' 
ClassicMenu Indicator is a notification area applet (application indicator) for the top panel of Ubuntu's Unity desktop environment.

It provides a simple way to get a classic GNOME-style application menu for those who prefer this over the Unity dash menu.

Like the classic GNOME menu, it includes Wine games and applications if you have those installed.

For more information , please visit : http://www.florian-diesch.de/software/classicmenu-indicator/

''')
                    repo = input(
                        "\033[1;32mDo you want to install classicmenu indicator ? [y/n]> \033[1;m")
                    if repo == "y":
                        cmd1 = os.system(
                            "add-apt-repository ppa:diesch/testing && apt-get update")
                        cmd = os.system(
                            "sudo apt-get install classicmenu-indicator")
                elif option0 == "help":
                    print("")
                    help_menu()
                elif option0 == "4":
                    repo = input(
                        "\033[1;32mDo you want to install Kali menu ? [y/n]> \033[1;m")
                    if repo == "y":
                        cmd1 = os.system("apt-get install kali-menu")
                elif option0 == "5":
                    help_menu()

                def inicio():
                    while option0 == "2":
                        print('''
\033[1;36m**************************** All Categories *****************************\033[1;m

1) Information Gathering			8) Exploitation Tools
2) Vulnerability Analysis			9) Forensics Tools
3) Wireless Attacks				10) Stress Testing
4) Web Applications				11) Password Attacks
5) Sniffing & Spoofing				12) Reverse Engineering
6) Maintaining Access				13) Hardware Hacking
7) Reporting Tools 				14) Extra
									
0) All

			 ''')
                        print(
                            "\033[1;32mSelect a category or press (0) to install all Kali linux tools .\n\033[1;m")

                        opcion1 = input("\033[1;36mkat > \033[1;m")
                        if opcion1 == "back":
                            initio1()
                        elif opcion1 == "gohome":
                            initio1()
                        elif opcion1 == "exit" or opcion1 == "quit":
                            print("Shutdown requested...Goodbye...")
                            sys.exit()
                        elif opcion1 == "help":
                            print("Available commands:\n"
                                  "back\t\tGo back to main menu\n"
                                  "gohome\t\tGo to the main menu\n"
                                  "exit\t\tExit the program\n"
                                  "help\t\tShow this help menu\n")
                        elif opcion1 == "0":
                            cmd = os.system(
                                "apt-get -f install acccheck ace-voip amap automater braa casefile cdpsnarf cisco-torch cookie-cadger copy-router-config dmitry dnmap dnsenum dnsmap dnsrecon dnstracer dnswalk dotdotpwn enum4linux enumiax exploitdb fierce firewalk fragroute fragrouter ghost-phisher golismero goofile lbd maltego-teeth masscan metagoofil miranda nmap p0f parsero recon-ng set smtp-user-enum snmpcheck sslcaudit sslsplit sslstrip sslyze thc-ipv6 theharvester tlssled twofi urlcrazy wireshark wol-e xplico ismtp intrace hping3 bbqsql bed cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch copy-router-config doona dotdotpwn greenbone-security-assistant hexorbase jsql lynis nmap ohrwurm openvas-cli openvas-manager openvas-scanner oscanner powerfuzzer sfuzz sidguesser siparmyknife sqlmap sqlninja sqlsus thc-ipv6 tnscmd10g unix-privesc-check yersinia aircrack-ng asleap bluelog blueranger bluesnarfer bully cowpatty crackle eapmd5pass fern-wifi-cracker ghost-phisher giskismet gqrx kalibrate-rtl killerbee kismet mdk3 mfcuk mfoc mfterm multimon-ng pixiewps reaver redfang spooftooph wifi-honey wifitap wifite apache-users arachni bbqsql blindelephant burpsuite cutycapt davtest deblaze dirb dirbuster fimap funkload grabber jboss-autopwn joomscan jsql maltego-teeth padbuster paros parsero plecost powerfuzzer proxystrike recon-ng skipfish sqlmap sqlninja sqlsus ua-tester uniscan vega w3af webscarab websploit wfuzz wpscan xsser zaproxy burpsuite dnschef fiked hamster-sidejack hexinject iaxflood inviteflood ismtp mitmproxy ohrwurm protos-sip rebind responder rtpbreak rtpinsertsound rtpmixsound sctpscan siparmyknife sipp sipvicious sniffjoke sslsplit sslstrip thc-ipv6 voiphopper webscarab wifi-honey wireshark xspy yersinia zaproxy cryptcat cymothoa dbd dns2tcp http-tunnel httptunnel intersect nishang polenum powersploit pwnat ridenum sbd u3-pwn webshells weevely casefile cutycapt dos2unix dradis keepnote magictree metagoofil nipper-ng pipal armitage backdoor-factory cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch crackle jboss-autopwn linux-exploit-suggester maltego-teeth set shellnoob sqlmap thc-ipv6 yersinia beef-xss binwalk bulk-extractor chntpw cuckoo dc3dd ddrescue dumpzilla extundelete foremost galleta guymager iphone-backup-analyzer p0f pdf-parser pdfid pdgmail peepdf volatility xplico dhcpig funkload iaxflood inviteflood ipv6-toolkit mdk3 reaver rtpflood slowhttptest t50 termineter thc-ipv6 thc-ssl-dos acccheck burpsuite cewl chntpw cisco-auditing-tool cmospwd creddump crunch findmyhash gpp-decrypt hash-identifier hexorbase john johnny keimpx maltego-teeth maskprocessor multiforcer ncrack oclgausscrack pack patator polenum rainbowcrack rcracki-mt rsmangler statsprocessor thc-pptp-bruter truecrack webscarab wordlists zaproxy apktool dex2jar python-distorm3 edb-debugger jad javasnoop jd ollydbg smali valgrind yara android-sdk apktool arduino dex2jar sakis3g smali && wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")
                        while opcion1 == "1":
                            print('''
\033[1;36m=+[ Information Gathering\033[1;m

 1) acccheck					30) lbd
 2) ace-voip					31) Maltego Teeth
 3) Amap					32) masscan
 4) Automater					33) Metagoofil
 5) bing-ip2hosts				34) Miranda
 6) braa					35) Nmap
 7) CaseFile					36) ntop
 8) CDPSnarf					37) p0f
 9) cisco-torch					38) Parsero
10) Cookie Cadger				39) Recon-ng
11) copy-router-config				40) SET
12) DMitry					41) smtp-user-enum
13) dnmap					42) snmpcheck
14) dnsenum					43) sslcaudit
15) dnsmap					44) SSLsplit
16) DNSRecon					45) sslstrip
17) dnstracer					46) SSLyze
18) dnswalk					47) THC-IPV6
19) DotDotPwn					48) theHarvester
20) enum4linux					49) TLSSLed
21) enumIAX					50) twofi
22) exploitdb					51) URLCrazy
23) Fierce					52) Wireshark
24) Firewalk					53) WOL-E
25) fragroute					54) Xplico
26) fragrouter					55) iSMTP
27) Ghost Phisher				56) InTrace
28) GoLismero					57) hping3
29) goofile

0) Install all Information Gathering tools

						''')
                            print(
                                "\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
                            option2 = input("\033[1;36mkat > \033[1;m")
                            if option2 == "1":
                                cmd = os.system("apt-get install acccheck")

                            elif option2 == "2":
                                cmd = os.system("apt-get install ace-voip")

                            elif option2 == "3":
                                cmd = os.system("apt-get install amap")
                            elif option2 == "4":
                                cmd = os.system("apt-get install automater")
                            elif option2 == "5":
                                cmd = os.system(
                                    "wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")
                            elif option2 == "6":
                                cmd = os.system("apt-get install braa")
                            elif option2 == "7":
                                cmd = os.system("apt-get install casefile")
                            elif option2 == "8":
                                cmd = os.system("apt-get install cdpsnarf")
                            elif option2 == "9":
                                cmd = os.system("apt-get install cisco-torch")
                            elif option2 == "10":
                                cmd = os.system(
                                    "apt-get install cookie-cadger")
                            elif option2 == "11":
                                cmd = os.system(
                                    "apt-get install copy-router-config")
                            elif option2 == "12":
                                cmd = os.system("apt-get install dmitry")
                            elif option2 == "13":
                                cmd = os.system("apt-get install dnmap")
                            elif option2 == "14":
                                cmd = os.system("apt-get install dnsenum")
                            elif option2 == "15":
                                cmd = os.system("apt-get install dnsmap")
                            elif option2 == "16":
                                cmd = os.system("apt-get install dnsrecon")
                            elif option2 == "17":
                                cmd = os.system("apt-get install dnstracer")
                            elif option2 == "18":
                                cmd = os.system("apt-get install dnswalk")
                            elif option2 == "19":
                                cmd = os.system("apt-get install dotdotpwn")
                            elif option2 == "20":
                                cmd = os.system("apt-get install enum4linux")
                            elif option2 == "21":
                                cmd = os.system("apt-get install enumiax")
                            elif option2 == "22":
                                cmd = os.system("apt-get install exploitdb")
                            elif option2 == "23":
                                cmd = os.system("apt-get install fierce")
                            elif option2 == "24":
                                cmd = os.system("apt-get install firewalk")
                            elif option2 == "25":
                                cmd = os.system("apt-get install fragroute")
                            elif option2 == "26":
                                cmd = os.system("apt-get install fragrouter")
                            elif option2 == "27":
                                cmd = os.system(
                                    "apt-get install ghost-phisher")
                            elif option2 == "28":
                                cmd = os.system("apt-get install golismero")
                            elif option2 == "29":
                                cmd = os.system("apt-get install goofile")
                            elif option2 == "30":
                                cmd = os.system("apt-get install lbd")
                            elif option2 == "31":
                                cmd = os.system(
                                    "apt-get install maltego-teeth")
                            elif option2 == "32":
                                cmd = os.system("apt-get install masscan")
                            elif option2 == "33":
                                cmd = os.system("apt-get install metagoofil")
                            elif option2 == "34":
                                cmd = os.system("apt-get install miranda")
                            elif option2 == "35":
                                cmd = os.system("apt-get install nmap")
                            elif option2 == "36":
                                print('ntop is unavailable')
                            elif option2 == "37":
                                cmd = os.system("apt-get install p0f")
                            elif option2 == "38":
                                cmd = os.system("apt-get install parsero")
                            elif option2 == "39":
                                cmd = os.system("apt-get install recon-ng")
                            elif option2 == "40":
                                cmd = os.system("apt-get install set")
                            elif option2 == "41":
                                cmd = os.system(
                                    "apt-get install smtp-user-enum")
                            elif option2 == "42":
                                cmd = os.system("apt-get install snmpcheck")
                            elif option2 == "43":
                                cmd = os.system("apt-get install sslcaudit")
                            elif option2 == "44":
                                cmd = os.system("apt-get install sslsplit")
                            elif option2 == "45":
                                cmd = os.system("apt-get install sslstrip")
                            elif option2 == "46":
                                cmd = os.system("apt-get install sslyze")
                            elif option2 == "47":
                                cmd = os.system("apt-get install thc-ipv6")
                            elif option2 == "48":
                                cmd = os.system("apt-get install theharvester")
                            elif option2 == "49":
                                cmd = os.system("apt-get install tlssled")
                            elif option2 == "50":
                                cmd = os.system("apt-get install twofi")
                            elif option2 == "51":
                                cmd = os.system("apt-get install urlcrazy")
                            elif option2 == "52":
                                cmd = os.system("apt-get install wireshark")
                            elif option2 == "53":
                                cmd = os.system("apt-get install wol-e")
                            elif option2 == "54":
                                cmd = os.system("apt-get install xplico")
                            elif option2 == "55":
                                cmd = os.system("apt-get install ismtp")
                            elif option2 == "56":
                                cmd = os.system("apt-get install intrace")
                            elif option2 == "57":
                                cmd = os.system("apt-get install hping3")
                            elif option2 == "back":
                                inicio()
                            elif option2 == "gohome":
                                initio1()
                            elif option2 == "exit" or option2 == "quit":
                                sys.exit()
                            elif option2 == "help":
                                print("Available commands:\n"
                                      "back\t\tGo back to main menu\n"
                                      "gohome\t\tGo to the main menu\n"
                                      "exit\t\tExit the program\n"
                                      "help\t\tShow this help menu\n")
                            elif option2 == "0":
                                cmd = os.system(
                                    "apt-get install -y acccheck ace-voip amap automater braa casefile cdpsnarf cisco-torch cookie-cadger copy-router-config dmitry dnmap dnsenum dnsmap dnsrecon dnstracer dnswalk dotdotpwn enum4linux enumiax exploitdb fierce firewalk fragroute fragrouter ghost-phisher golismero goofile lbd maltego-teeth masscan metagoofil miranda nmap p0f parsero recon-ng set smtp-user-enum snmpcheck sslcaudit sslsplit sslstrip sslyze thc-ipv6 theharvester tlssled twofi urlcrazy wireshark wol-e xplico ismtp intrace hping3 && wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")
                            else:
                                print(
                                    "\033[1;31mSorry, that was an invalid command!\033[1;m")

                        while opcion1 == "2":
                            print('''
\033[1;36m=+[ Vulnerability Analysis\033[1;m

 1) BBQSQL				18) Nmap
 2) BED					19)ohrwurm
 3) cisco-auditing-tool			20) openvas-administrator
 4) cisco-global-exploiter		21) openvas-cli
 5) cisco-ocs				22) openvas-manager
 6) cisco-torch				23) openvas-scanner
 7) copy-router-config			24) Oscanner
 8) commix				25) Powerfuzzer
 9) DBPwAudit				26) sfuzz
10) DoonaDot				27) SidGuesser
11) DotPwn				28) SIPArmyKnife
12) Greenbone Security Assistant 	29) sqlmap
13) GSD					30) Sqlninja
14) HexorBase				31) sqlsus
15) Inguma				32) THC-IPV6
16) jSQL				33) tnscmd10g
17) Lynis				34) unix-privesc-check
					35) Yersinia

0) Install all Vulnerability Analysis tools

						''')
                            print(
                                "\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
                            option2 = input("\033[1;36mkat > \033[1;m")
                            if option2 == "1":
                                cmd = os.system("apt-get install bbqsql")

                            elif option2 == "2":
                                cmd = os.system("apt-get install bed")

                            elif option2 == "3":
                                cmd = os.system(
                                    "apt-get install cisco-auditing-tool")
                            elif option2 == "4":
                                cmd = os.system(
                                    "apt-get install cisco-global-exploiter")
                            elif option2 == "5":
                                cmd = os.system("apt-get install cisco-ocs")
                            elif option2 == "6":
                                cmd = os.system("apt-get install cisco-torch")
                            elif option2 == "7":
                                cmd = os.system(
                                    "apt-get install copy-router-config")
                            elif option2 == "8":
                                cmd = os.system(
                                    "apt-get install git && git clone https://github.com/stasinopoulos/commix.git commix && cd commix && python ./commix.py --install")
                            elif option2 == "9":
                                cmd = os.system(
                                    "echo 'download page : http://www.cqure.net/wp/tools/database/dbpwaudit/'")
                            elif option2 == "10":
                                cmd = os.system("apt-get install doona")
                            elif option2 == "11":
                                cmd = os.system("apt-get install dotdotpwn")
                            elif option2 == "12":
                                cmd = os.system(
                                    "apt-get install greenbone-security-assistant")
                            elif option2 == "13":
                                cmd = os.system(
                                    "apt-get install git && git clone git://git.kali.org/packages/gsd.git")
                            elif option2 == "14":
                                cmd = os.system("apt-get install hexorbase")
                            elif option2 == "15":
                                print(
                                    "Please download inguma from : http://inguma.sourceforge.net")
                            elif option2 == "16":
                                cmd = os.system("apt-get install jsql")
                            elif option2 == "17":
                                cmd = os.system("apt-get install lynis")
                            elif option2 == "18":
                                cmd = os.system("apt-get install nmap")
                            elif option2 == "19":
                                cmd = os.system("apt-get install ohrwurm")
                            elif option2 == "20":
                                cmd = os.system(
                                    "apt-get install openvas-administrator")
                            elif option2 == "21":
                                cmd = os.system("apt-get install openvas-cli")
                            elif option2 == "22":
                                cmd = os.system(
                                    "apt-get install openvas-manager")
                            elif option2 == "23":
                                cmd = os.system(
                                    "apt-get install openvas-scanner")
                            elif option2 == "24":
                                cmd = os.system("apt-get install oscanner")
                            elif option2 == "25":
                                cmd = os.system("apt-get install powerfuzzer")
                            elif option2 == "26":
                                cmd = os.system("apt-get install sfuzz")
                            elif option2 == "27":
                                cmd = os.system("apt-get install sidguesser")
                            elif option2 == "28":
                                cmd = os.system("apt-get install siparmyknife")
                            elif option2 == "29":
                                cmd = os.system("apt-get install sqlmap")
                            elif option2 == "30":
                                cmd = os.system("apt-get install sqlninja")
                            elif option2 == "31":
                                cmd = os.system("apt-get install sqlsus")
                            elif option2 == "32":
                                cmd = os.system("apt-get install thc-ipv6")
                            elif option2 == "33":
                                cmd = os.system("apt-get install tnscmd10g")
                            elif option2 == "34":
                                cmd = os.system(
                                    "apt-get install unix-privesc-check")
                            elif option2 == "35":
                                cmd = os.system("apt-get install yersinia")
                            elif option2 == "back":
                                inicio()
                            elif option2 == "gohome":
                                initio1()
                            elif option2 == "0":
                                cmd = os.system(
                                    "apt-get install -y bbqsql bed cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch copy-router-config doona dotdotpwn greenbone-security-assistant hexorbase jsql lynis nmap ohrwurm openvas-cli openvas-manager openvas-scanner oscanner powerfuzzer sfuzz sidguesser siparmyknife sqlmap sqlninja sqlsus thc-ipv6 tnscmd10g unix-privesc-check yersinia")
                            else:
                                print(
                                    "\033[1;31mSorry, that was an invalid command!\033[1;m")

                        while opcion1 == "3":
                            print('''
		\033[1;36m=+[ Wireless Attacks\033[1;m

 1) Aircrack-ng				17) kalibrate-rtl
 2) Asleap				18) KillerBee
 3) Bluelog				19) Kismet
 4) BlueMaho				20) mdk3
 5) Bluepot				21) mfcuk
 6) BlueRanger				22) mfoc
 7) Bluesnarfer				23) mfterm
 8) Bully				24) Multimon-NG
 9) coWPAtty				25) PixieWPS
10) crackle				26) Reaver
11) eapmd5pass				27) redfang
12) Fern Wifi Cracker			28) RTLSDR Scanner
13) Ghost Phisher			29) Spooftooph
14) GISKismet				30) Wifi Honey				31) Wifitap
16) gr-scan				32) Wifite

0) Install all Wireless Attacks tools

						''')
                            print(
                                "\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
                            option2 = input("\033[1;36mkat > \033[1;m")
                            if option2 == "1":
                                cmd = os.system("apt-get install aircrack-ng")

                            elif option2 == "2":
                                cmd = os.system("apt-get install asleap")

                            elif option2 == "3":
                                cmd = os.system("apt-get install bluelog")
                            elif option2 == "4":
                                cmd = os.system(
                                    "apt-get install git && git clone git://git.kali.org/packages/bluemaho.git")
                            elif option2 == "5":
                                cmd = os.system(
                                    "apt-get install git && git clone git://git.kali.org/packages/bluepot.git")
                            elif option2 == "6":
                                cmd = os.system("apt-get install blueranger")
                            elif option2 == "7":
                                cmd = os.system("apt-get install bluesnarfer")
                            elif option2 == "8":
                                cmd = os.system("apt-get install bully")
                            elif option2 == "9":
                                cmd = os.system("apt-get install cowpatty")
                            elif option2 == "10":
                                cmd = os.system("apt-get install crackle")
                            elif option2 == "11":
                                cmd = os.system("apt-get install eapmd5pass")
                            elif option2 == "12":
                                cmd = os.system(
                                    "apt-get install fern-wifi-cracker")
                            elif option2 == "13":
                                cmd = os.system(
                                    "apt-get install ghost-phisher")
                            elif option2 == "14":
                                cmd = os.system("apt-get install giskismet")
                            elif option2 == "16":
                                cmd = os.system(
                                    "apt-get install git && git clone git://git.kali.org/packages/gr-scan.git")
                            elif option2 == "17":
                                cmd = os.system(
                                    "apt-get install kalibrate-rtl")
                            elif option2 == "18":
                                cmd = os.system("apt-get install killerbee")
                            elif option2 == "19":
                                cmd = os.system("apt-get install kismet")
                            elif option2 == "20":
                                cmd = os.system("apt-get install mdk3")
                            elif option2 == "21":
                                cmd = os.system("apt-get install mfcuk")
                            elif option2 == "22":
                                cmd = os.system("apt-get install mfoc")
                            elif option2 == "23":
                                cmd = os.system("apt-get install mfterm")
                            elif option2 == "24":
                                cmd = os.system("apt-get install multimon-ng")
                            elif option2 == "25":
                                cmd = os.system("apt-get install pixiewps")
                            elif option2 == "26":
                                cmd = os.system("apt-get install reaver")
                            elif option2 == "27":
                                cmd = os.system("apt-get install redfang")
                            elif option2 == "28":
                                cmd = os.system(
                                    "apt-get install rtlsdr-scanner")
                            elif option2 == "29":
                                cmd = os.system("apt-get install spooftooph")
                            elif option2 == "30":
                                cmd = os.system("apt-get install wifi-honey")
                            elif option2 == "31":
                                cmd = os.system("apt-get install wifitap")
                            elif option2 == "32":
                                cmd = os.system("apt-get install wifite")
                            elif option2 == "0":
                                cmd = os.system(
                                    "apt-get install -y aircrack-ng asleap bluelog blueranger bluesnarfer bully cowpatty crackle eapmd5pass fern-wifi-cracker ghost-phisher giskismet gqrx kalibrate-rtl killerbee kismet mdk3 mfcuk mfoc mfterm multimon-ng pixiewps reaver redfang spooftooph wifi-honey wifitap wifite")
                            elif option2 == "back":
                                inicio()
                            elif option2 == "gohome":
                                initio1()
                            else:
                                print(
                                    "\033[1;31mSorry, that was an invalid command!\033[1;m")
                        while opcion1 == "4":
                            print('''
\033[1;36m=+[ Web Applications\033[1;m

 1) apache-users			21) Parsero
 2) Arachni				22) plecost
 3) BBQSQL				23) Powerfuzzer
 4) BlindElephant			24) ProxyStrike
 5) Burp Suite				25) Recon-ng
 6) commix				26) Skipfish
 7) CutyCapt				27) sqlmap
 8) DAVTest				28) Sqlninja
 9) deblaze				29) sqlsus
10) DIRB				30) ua-tester
11) DirBuster				31) Uniscan
12) fimap				32) Vega
13) FunkLoad				33) w3af
14) Grabber				34) WebScarab
15) jboss-autopwn			35) Webshag
16) joomscan				36) WebSlayer
17) jSQL				37) WebSploit
18) Maltego Teeth			38) Wfuzz
19) PadBuster				39) WPScan
20) Paros				40) XSSer
					41) zaproxy

0) Install all Web Applications tools

						''')
                            print(
                                "\033[1;32mInsert the number of the tool to install it .\n\033[1;m")

                            option2 = input("\033[1;36mkat > \033[1;m")
                            if option2 == "1":
                                cmd = os.system("apt-get install apache-users")

                            elif option2 == "2":
                                cmd = os.system("apt-get install arachni")

                            elif option2 == "3":
                                cmd = os.system("apt-get install bbqsql")
                            elif option2 == "4":
                                cmd = os.system(
                                    "apt-get install blindelephant")
                            elif option2 == "5":
                                cmd = os.system("apt-get install burpsuite")
                            elif option2 == "6":
                                cmd = os.system("apt-get install cutycapt")
                            elif option2 == "7":
                                cmd = os.system(
                                    "apt-get install git && git clone https://github.com/stasinopoulos/commix.git commix && cd commix && python ./commix.py --install")
                            elif option2 == "8":
                                cmd = os.system("apt-get install davtest")
                            elif option2 == "9":
                                cmd = os.system("apt-get install deblaze")
                            elif option2 == "10":
                                cmd = os.system("apt-get install dirb")
                            elif option2 == "11":
                                cmd = os.system("apt-get install dirbuster")
                            elif option2 == "12":
                                cmd = os.system("apt-get install fimap")
                            elif option2 == "13":
                                cmd = os.system("apt-get install funkload")
                            elif option2 == "14":
                                cmd = os.system("apt-get install grabber")
                            elif option2 == "15":
                                cmd = os.system(
                                    "apt-get install jboss-autopwn")
                            elif option2 == "16":
                                cmd = os.system("apt-get install joomscan")
                            elif option2 == "17":
                                cmd = os.system("apt-get install jsql")
                            elif option2 == "18":
                                cmd = os.system(
                                    "apt-get install maltego-teeth")
                            elif option2 == "19":
                                cmd = os.system("apt-get install padbuster")
                            elif option2 == "20":
                                cmd = os.system("apt-get install paros")
                            elif option2 == "21":
                                cmd = os.system("apt-get install parsero")
                            elif option2 == "22":
                                cmd = os.system("apt-get install plecost")
                            elif option2 == "23":
                                cmd = os.system("apt-get install powerfuzzer")
                            elif option2 == "24":
                                cmd = os.system("apt-get install proxystrike")
                            elif option2 == "25":
                                cmd = os.system("apt-get install recon-ng")
                            elif option2 == "26":
                                cmd = os.system("apt-get install skipfish")
                            elif option2 == "27":
                                cmd = os.system("apt-get install sqlmap")
                            elif option2 == "28":
                                cmd = os.system("apt-get install sqlninja")
                            elif option2 == "29":
                                cmd = os.system("apt-get install sqlsus")
                            elif option2 == "30":
                                cmd = os.system("apt-get install ua-tester")
                            elif option2 == "31":
                                cmd = os.system("apt-get install uniscan")
                            elif option2 == "32":
                                cmd = os.system("apt-get install vega")
                            elif option2 == "33":
                                cmd = os.system("apt-get install w3af")
                            elif option2 == "34":
                                cmd = os.system("apt-get install webscarab")
                            elif option2 == "35":
                                print("Webshag is unavailable")
                            elif option2 == "36":
                                cmd = os.system(
                                    "apt-get install git && git clone git://git.kali.org/packages/webslayer.git")
                            elif option2 == "37":
                                cmd = os.system("apt-get install websploit")
                            elif option2 == "38":
                                cmd = os.system("apt-get install wfuzz")
                            elif option2 == "39":
                                cmd = os.system("apt-get install wpscan")
                            elif option2 == "40":
                                cmd = os.system("apt-get install xsser")
                            elif option2 == "41":
                                cmd = os.system("apt-get install zaproxy")
                            elif option2 == "back":
                                inicio()
                            elif option2 == "gohome":
                                initio1()
                            elif option2 == "0":
                                cmd = os.system(
                                    "apt-get install -y apache-users arachni bbqsql blindelephant burpsuite cutycapt davtest deblaze dirb dirbuster fimap funkload grabber jboss-autopwn joomscan jsql maltego-teeth padbuster paros parsero plecost powerfuzzer proxystrike recon-ng skipfish sqlmap sqlninja sqlsus ua-tester uniscan vega w3af webscarab websploit wfuzz wpscan xsser zaproxy")
                            else:
                                print(
                                    "\033[1;31mSorry, that was an invalid command!\033[1;m")
                        while opcion1 == "5":
                            print('''
\033[1;36m=+[ Sniffing & Spoofing\033[1;m

 1) Burp Suite				17) rtpmixsound
 2) DNSChef				18) sctpscan
 3) fiked				19) SIPArmyKnife
 4) hamster-sidejack			20) SIPp
 5) HexInject				21) SIPVicious
 6) iaxflood				22) SniffJoke
 7) inviteflood				23) SSLsplit
 8) iSMTP				24) sslstrip
 9) isr-evilgrade			25) THC-IPV6
10) mitmproxy				26) VoIPHopper
11) ohrwurm				27) WebScarab
12) protos-sip				28) Wifi Honey
13) rebind				29) Wireshark
14) responder				30) xspy
15) rtpbreak				31) Yersinia
16) rtpinsertsound			32) zaproxy

0) Install all Sniffing & Spoofing tools

						''')
                            print(
                                "\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
                            option2 = input("\033[1;36mkat > \033[1;m")
                            if option2 == "1":
                                cmd = os.system("apt-get install burpsuite")

                            elif option2 == "2":
                                cmd = os.system("apt-get install dnschef")

                            elif option2 == "3":
                                cmd = os.system("apt-get install fiked")
                            elif option2 == "4":
                                cmd = os.system(
                                    "apt-get install hamster-sidejack")
                            elif option2 == "5":
                                cmd = os.system("apt-get install hexinject")
                            elif option2 == "6":
                                cmd = os.system("apt-get install iaxflood")
                            elif option2 == "7":
                                cmd = os.system("apt-get install inviteflood")
                            elif option2 == "8":
                                cmd = os.system("apt-get install ismtp")
                            elif option2 == "9":
                                cmd = os.system(
                                    "apt-get install git && git clone git://git.kali.org/packages/isr-evilgrade.git")
                            elif option2 == "10":
                                cmd = os.system("apt-get install mitmproxy")
                            elif option2 == "11":
                                cmd = os.system("apt-get install ohrwurm")
                            elif option2 == "12":
                                cmd = os.system("apt-get install protos-sip")
                            elif option2 == "13":
                                cmd = os.system("apt-get install rebind")
                            elif option2 == "14":
                                cmd = os.system("apt-get install responder")
                            elif option2 == "15":
                                cmd = os.system("apt-get install rtpbreak")
                            elif option2 == "16":
                                cmd = os.system(
                                    "apt-get install rtpinsertsound")
                            elif option2 == "17":
                                cmd = os.system("apt-get install rtpmixsound")
                            elif option2 == "18":
                                cmd = os.system("apt-get install sctpscan")
                            elif option2 == "19":
                                cmd = os.system("apt-get install siparmyknife")
                            elif option2 == "20":
                                cmd = os.system("apt-get install sipp")
                            elif option2 == "21":
                                cmd = os.system("apt-get install sipvicious")
                            elif option2 == "22":
                                cmd = os.system("apt-get install sniffjoke")
                            elif option2 == "23":
                                cmd = os.system("apt-get install sslsplit")
                            elif option2 == "24":
                                cmd = os.system("apt-get install sslstrip")
                            elif option2 == "25":
                                cmd = os.system("apt-get install thc-ipv6")
                            elif option2 == "26":
                                cmd = os.system("apt-get install voiphopper")
                            elif option2 == "27":
                                cmd = os.system("apt-get install webscarab")
                            elif option2 == "28":
                                cmd = os.system("apt-get install wifi-honey")
                            elif option2 == "29":
                                cmd = os.system("apt-get install wireshark")
                            elif option2 == "30":
                                cmd = os.system("apt-get install xspy")
                            elif option2 == "31":
                                cmd = os.system("apt-get install yersinia")
                            elif option2 == "32":
                                cmd = os.system("apt-get install zaproxy")
                            elif option2 == "back":
                                inicio()
                            elif option2 == "gohome":
                                initio1()

                            elif option2 == "0":
                                cmd = os.system(
                                    "apt-get install -y burpsuite dnschef fiked hamster-sidejack hexinject iaxflood inviteflood ismtp mitmproxy ohrwurm protos-sip rebind responder rtpbreak rtpinsertsound rtpmixsound sctpscan siparmyknife sipp sipvicious sniffjoke sslsplit sslstrip thc-ipv6 voiphopper webscarab wifi-honey wireshark xspy yersinia zaproxy")
                            else:
                                print(
                                    "\033[1;31mSorry, that was an invalid command!\033[1;m")

                        while opcion1 == "6":
                            print('''
\033[1;36m=+[ Maintaining Access\033[1;m

 1) CryptCat
 2) Cymothoa
 3) dbd
 4) dns2tcp
 5) http-tunnel
 6) HTTPTunnel
 7) Intersect
 8) Nishang
 9) polenum
10) PowerSploit
11) pwnat
12) RidEnum
13) sbd
14) U3-Pwn
15) Webshells
16) Weevely

0) Install all Maintaining Access tools

						''')
                            print(
                                "\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
                            option2 = input("\033[1;36mkat > \033[1;m")
                            if option2 == "1":
                                cmd = os.system("apt-get install cryptcat")

                            elif option2 == "2":
                                cmd = os.system("apt-get install cymothoa")

                            elif option2 == "3":
                                cmd = os.system("apt-get install dbd")
                            elif option2 == "4":
                                cmd = os.system("apt-get install dns2tcp")
                            elif option2 == "5":
                                cmd = os.system("apt-get install http-tunnel")
                            elif option2 == "6":
                                cmd = os.system("apt-get install httptunnel")
                            elif option2 == "7":
                                cmd = os.system("apt-get install intersect")
                            elif option2 == "8":
                                cmd = os.system("apt-get install nishang")
                            elif option2 == "9":
                                cmd = os.system("apt-get install polenum")
                            elif option2 == "10":
                                cmd = os.system("apt-get install powersploit")
                            elif option2 == "11":
                                cmd = os.system("apt-get install pwnat")
                            elif option2 == "12":
                                cmd = os.system("apt-get install ridenum")
                            elif option2 == "13":
                                cmd = os.system("apt-get install sbd")
                            elif option2 == "14":
                                cmd = os.system("apt-get install u3-pwn")
                            elif option2 == "15":
                                cmd = os.system("apt-get install webshells")
                            elif option2 == "16":
                                cmd = os.system("apt-get install weevely")
                            elif option2 == "back":
                                inicio()
                            elif option2 == "gohome":
                                initio1()
                            elif option2 == "0":
                                cmd = os.system(
                                    "apt-get install -y cryptcat cymothoa dbd dns2tcp http-tunnel httptunnel intersect nishang polenum powersploit pwnat ridenum sbd u3-pwn webshells weevely")
                            else:
                                print(
                                    "\033[1;31mSorry, that was an invalid command!\033[1;m")
                        while opcion1 == "7":
                            print('''
\033[1;36m=+[ Reporting Tools\033[1;m

1) CaseFile
2) CutyCapt
3) dos2unix
4) Dradis
5) KeepNote
6) MagicTree
7) Metagoofil
8) Nipper-ng
9) pipal

0) Install all Reporting Tools

						''')
                            print(
                                "\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
                            option2 = input("\033[1;36mkat > \033[1;m")
                            if option2 == "1":
                                cmd = os.system("apt-get install casefile")

                            elif option2 == "2":
                                cmd = os.system("apt-get install cutycapt")

                            elif option2 == "3":
                                cmd = os.system("apt-get install dos2unix")
                            elif option2 == "4":
                                cmd = os.system("apt-get install dradis")
                            elif option2 == "5":
                                cmd = os.system("apt-get install keepnote")
                            elif option2 == "6":
                                cmd = os.system("apt-get install magictree")
                            elif option2 == "7":
                                cmd = os.system("apt-get install metagoofil")
                            elif option2 == "8":
                                cmd = os.system("apt-get install nipper-ng")
                            elif option2 == "9":
                                cmd = os.system("apt-get install pipal")
                            elif option2 == "back":
                                inicio()
                            elif option2 == "gohome":
                                initio1()
                            elif option2 == "0":
                                cmd = os.system(
                                    "apt-get install -y casefile cutycapt dos2unix dradis keepnote magictree metagoofil nipper-ng pipal")
                            else:
                                print(
                                    "\033[1;31mSorry, that was an invalid command!\033[1;m")

                        while opcion1 == "8":
                            print('''
\033[1;36m=+[ Exploitation Tools\033[1;m

 1) Armitage
 2) Backdoor Factory
 3) BeEF
 4) cisco-auditing-tool
 5) cisco-global-exploiter
 6) cisco-ocs
 7) cisco-torch
 8) commix
 9) crackle
10) jboss-autopwn
11) Linux Exploit Suggester
12) Maltego Teeth
13) SET
14) ShellNoob
15) sqlmap
16) THC-IPV6
17) Yersinia

0) Install all Exploitation Tools

						''')
                            print(
                                "\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
                            option2 = input("\033[1;36mkat > \033[1;m")
                            if option2 == "1":
                                cmd = os.system("apt-get install armitage")

                            elif option2 == "2":
                                cmd = os.system(
                                    "apt-get install backdoor-factory")

                            elif option2 == "3":
                                cmd = os.system("apt-get install beef-xss")
                            elif option2 == "4":
                                cmd = os.system(
                                    "apt-get install cisco-auditing-tool")
                            elif option2 == "5":
                                cmd = os.system(
                                    "apt-get install cisco-global-exploiter")
                            elif option2 == "6":
                                cmd = os.system("apt-get install cisco-ocs")
                            elif option2 == "7":
                                cmd = os.system("apt-get install cisco-torch")
                            elif option2 == "8":
                                cmd = os.system(
                                    "apt-get install git && git clone https://github.com/stasinopoulos/commix.git commix && cd commix && python ./commix.py --install")
                            elif option2 == "9":
                                cmd = os.system("apt-get install crackle")
                            elif option2 == "10":
                                cmd = os.system(
                                    "apt-get install jboss-autopwn")
                            elif option2 == "11":
                                cmd = os.system(
                                    "apt-get install linux-exploit-suggester")
                            elif option2 == "12":
                                cmd = os.system(
                                    "apt-get install maltego-teeth")
                            elif option2 == "13":
                                cmd = os.system("apt-get install set")
                            elif option2 == "14":
                                cmd = os.system("apt-get install shellnoob")
                            elif option2 == "15":
                                cmd = os.system("apt-get install sqlmap")
                            elif option2 == "16":
                                cmd = os.system("apt-get install thc-ipv6")
                            elif option2 == "17":
                                cmd = os.system("apt-get install yersinia")
                            elif option2 == "back":
                                inicio()
                            elif option2 == "gohome":
                                initio1()
                            elif option2 == "0":
                                cmd = os.system(
                                    "apt-get install -y armitage backdoor-factory cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch crackle jboss-autopwn linux-exploit-suggester maltego-teeth set shellnoob sqlmap thc-ipv6 yersinia beef-xss")
                            else:
                                print(
                                    "\033[1;31mSorry, that was an invalid command!\033[1;m")

                        while opcion1 == "9":
                            print('''
\033[1;36m=+[ Forensics Tools\033[1;m

 1) Binwalk				11) extundelete
 2) bulk-extractor			12) Foremost
 3) Capstone				13) Galleta
 4) chntpw				14) Guymager
 5) Cuckoo				15) iPhone Backup Analyzer
 6) dc3dd				16) p0f
 7) ddrescue				17) pdf-parser
 8) DFF					18) pdfid
 9) diStorm3				19) pdgmail
10) Dumpzilla				20) peepdf
					21) RegRipper
					22) Volatility
					23) Xplico

0) Install all Forensics Tools

						''')
                            print(
                                "\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
                            option2 = input("\033[1;36mkat > \033[1;m")
                            if option2 == "1":
                                cmd = os.system("apt-get install binwalk")

                            elif option2 == "2":
                                cmd = os.system(
                                    "apt-get install bulk-extractor")

                            elif option2 == "3":
                                cmd = os.system(
                                    "apt-get install git && git clone git://git.kali.org/packages/capstone.git")
                            elif option2 == "4":
                                cmd = os.system("apt-get install chntpw")
                            elif option2 == "5":
                                cmd = os.system("apt-get install cuckoo")
                            elif option2 == "6":
                                cmd = os.system("apt-get install dc3dd")
                            elif option2 == "7":
                                cmd = os.system("apt-get install ddrescue")
                            elif option2 == "8":
                                print('dff is unavailable')
                            elif option2 == "9":
                                cmd = os.system(
                                    "apt-get install git && git clone git://git.kali.org/packages/distorm3.git")
                            elif option2 == "10":
                                cmd = os.system("apt-get install dumpzilla")
                            elif option2 == "11":
                                cmd = os.system("apt-get install extundelete")
                            elif option2 == "12":
                                cmd = os.system("apt-get install foremost")
                            elif option2 == "13":
                                cmd = os.system("apt-get install galleta")
                            elif option2 == "14":
                                cmd = os.system("apt-get install guymager")
                            elif option2 == "15":
                                cmd = os.system(
                                    "apt-get install iphone-backup-analyzer")
                            elif option2 == "16":
                                cmd = os.system("apt-get install p0f")
                            elif option2 == "17":
                                cmd = os.system("apt-get install pdf-parser")
                            elif option2 == "18":
                                cmd = os.system("apt-get install pdfid")
                            elif option2 == "19":
                                cmd = os.system("apt-get install pdgmail")
                            elif option2 == "20":
                                cmd = os.system("apt-get install peepdf")
                            elif option2 == "21":
                                print("Regripper is unavailable")
                            elif option2 == "22":
                                cmd = os.system("apt-get install volatility")
                            elif option2 == "23":
                                cmd = os.system("apt-get install xplico")
                            elif option2 == "back":
                                inicio()
                            elif option2 == "gohome":
                                initio1()
                            elif option2 == "0":
                                cmd = os.system(
                                    "apt-get install -y binwalk bulk-extractor chntpw cuckoo dc3dd ddrescue dumpzilla extundelete foremost galleta guymager iphone-backup-analyzer p0f pdf-parser pdfid pdgmail peepdf volatility xplico")
                            else:
                                print(
                                    "\033[1;31mSorry, that was an invalid command!\033[1;m")
                        while opcion1 == "10":
                            print('''
\033[1;36m=+[ Stress Testing\033[1;m

 1) DHCPig
 2) FunkLoad
 3) iaxflood
 4) Inundator
 5) inviteflood
 6) ipv6-toolkit
 7) mdk3
 8) Reaver
 9) rtpflood
10) SlowHTTPTest
11) t50
12) Termineter
13) THC-IPV6
14) THC-SSL-DOS

0) Install all Stress Testing tools

						''')
                            print(
                                "\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
                            option2 = input("\033[1;36mkat > \033[1;m")
                            if option2 == "1":
                                cmd = os.system("apt-get install dhcpig")

                            elif option2 == "2":
                                cmd = os.system("apt-get install funkload")

                            elif option2 == "3":
                                cmd = os.system("apt-get install iaxflood")
                            elif option2 == "4":
                                cmd = os.system(
                                    "apt-get install git && git clone git://git.kali.org/packages/inundator.git")
                            elif option2 == "5":
                                cmd = os.system("apt-get install inviteflood")
                            elif option2 == "6":
                                cmd = os.system("apt-get install ipv6-toolkit")
                            elif option2 == "7":
                                cmd = os.system("apt-get install mdk3")
                            elif option2 == "8":
                                cmd = os.system("apt-get install reaver")
                            elif option2 == "9":
                                cmd = os.system("apt-get install rtpflood")
                            elif option2 == "10":
                                cmd = os.system("apt-get install slowhttptest")
                            elif option2 == "11":
                                cmd = os.system("apt-get install t50")
                            elif option2 == "12":
                                cmd = os.system("apt-get install termineter")
                            elif option2 == "13":
                                cmd = os.system("apt-get install thc-ipv6")
                            elif option2 == "14":
                                cmd = os.system("apt-get install thc-ssl-dos ")
                            elif option2 == "back":
                                inicio()
                            elif option2 == "gohome":
                                initio1()
                            elif option2 == "0":
                                cmd = os.system(
                                    "apt-get install -y dhcpig funkload iaxflood inviteflood ipv6-toolkit mdk3 reaver rtpflood slowhttptest t50 termineter thc-ipv6 thc-ssl-dos")
                            else:
                                print(
                                    "\033[1;31mSorry, that was an invalid command!\033[1;m")
                        while opcion1 == "11":
                            print('''
\033[1;36m=+[ Password Attacks\033[1;m

 1) acccheck				19) Maskprocessor
 2) Burp Suite				20) multiforcer
 3) CeWL				21) Ncrack
 4) chntpw				22) oclgausscrack
 5) cisco-auditing-tool			23) PACK
 6) CmosPwd				24) patator
 7) creddump				25) phrasendrescher
 8) crunch				26) polenum
 9) DBPwAudit				27) RainbowCrack
10) findmyhash				28) rcracki-mt
11) gpp-decrypt				29) RSMangler
12) hash-identifier			30) SQLdict
13) HexorBase				31) Statsprocessor
14) THC-Hydra				32) THC-pptp-bruter
15) John the Ripper			33) TrueCrack
16) Johnny				34) WebScarab
17) keimpx				35) wordlists
18) Maltego Teeth			36) zaproxy

0) Install all Password Attacks tools

						''')
                            print(
                                "\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
                            option2 = input("\033[1;36mkat > \033[1;m")
                            if option2 == "1":
                                cmd = os.system("apt-get install acccheck")

                            elif option2 == "2":
                                cmd = os.system("apt-get install burpsuite")

                            elif option2 == "3":
                                cmd = os.system("apt-get install cewl")
                            elif option2 == "4":
                                cmd = os.system("apt-get install chntpw")
                            elif option2 == "5":
                                cmd = os.system(
                                    "apt-get install cisco-auditing-tool")
                            elif option2 == "6":
                                cmd = os.system("apt-get install cmospwd")
                            elif option2 == "7":
                                cmd = os.system("apt-get install creddump")
                            elif option2 == "8":
                                cmd = os.system("apt-get install crunch")
                            elif option2 == "9":
                                cmd = os.system(
                                    "apt-get install git && git clone git://git.kali.org/packages/dbpwaudit.git")
                            elif option2 == "10":
                                cmd = os.system("apt-get install findmyhash")
                            elif option2 == "11":
                                cmd = os.system("apt-get install gpp-decrypt")
                            elif option2 == "12":
                                cmd = os.system(
                                    "apt-get install hash-identifier")
                            elif option2 == "13":
                                cmd = os.system("apt-get install hexorbase")
                            elif option2 == "14":
                                cmd = os.system(
                                    "echo 'please visit : https://www.thc.org/thc-hydra/' ")
                            elif option2 == "15":
                                cmd = os.system("apt-get install john")
                            elif option2 == "16":
                                cmd = os.system("apt-get install johnny")
                            elif option2 == "17":
                                cmd = os.system("apt-get install keimpx")
                            elif option2 == "18":
                                cmd = os.system(
                                    "apt-get install maltego-teeth")
                            elif option2 == "19":
                                cmd = os.system(
                                    "apt-get install maskprocessor")
                            elif option2 == "20":
                                cmd = os.system("apt-get install multiforcer")
                            elif option2 == "21":
                                cmd = os.system("apt-get install ncrack")
                            elif option2 == "22":
                                cmd = os.system(
                                    "apt-get install oclgausscrack")
                            elif option2 == "23":
                                cmd = os.system("apt-get install pack")
                            elif option2 == "24":
                                cmd = os.system("apt-get install patator")
                            elif option2 == "25":
                                cmd = os.system(
                                    "echo 'please visit : http://www.leidecker.info/projects/phrasendrescher/index.shtml' ")
                            elif option2 == "26":
                                cmd = os.system("apt-get install polenum")
                            elif option2 == "27":
                                cmd = os.system("apt-get install rainbowcrack")
                            elif option2 == "28":
                                cmd = os.system("apt-get install rcracki-mt")
                            elif option2 == "29":
                                cmd = os.system("apt-get install rsmangler")
                            elif option2 == "30":
                                print("Sqldict is unavailable")
                            elif option2 == "31":
                                cmd = os.system(
                                    "apt-get install statsprocessor")
                            elif option2 == "32":
                                cmd = os.system(
                                    "apt-get install thc-pptp-bruter")
                            elif option2 == "33":
                                cmd = os.system("apt-get install truecrack")
                            elif option2 == "34":
                                cmd = os.system("apt-get install webscarab")
                            elif option2 == "35":
                                cmd = os.system("apt-get install wordlists")
                            elif option2 == "36":
                                cmd = os.system("apt-get install zaproxy")
                            elif option2 == "back":
                                inicio()
                            elif option2 == "gohome":
                                initio1()
                            elif option2 == "0":
                                cmd = os.system(
                                    "apt-get install -y acccheck burpsuite cewl chntpw cisco-auditing-tool cmospwd creddump crunch findmyhash gpp-decrypt hash-identifier hexorbase john johnny keimpx maltego-teeth maskprocessor multiforcer ncrack oclgausscrack pack patator polenum rainbowcrack rcracki-mt rsmangler statsprocessor thc-pptp-bruter truecrack webscarab wordlists zaproxy")
                            else:
                                print(
                                    "\033[1;31mSorry, that was an invalid command!\033[1;m")
                        while opcion1 == "12":
                            print('''
\033[1;36m=+[ Reverse Engineering\033[1;m

 1) apktool
 2) dex2jar
 3) diStorm3
 4) edb-debugger
 5) jad
 6) javasnoop
 7) JD-GUI
 8) OllyDbg
 9) smali
10) Valgrind
11) YARA

0) Install all Reverse Engineering tools

						''')
                            print(
                                "\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
                            option2 = input("\033[1;36mkat > \033[1;m")
                            if option2 == "1":
                                cmd = os.system("apt-get install apktool")

                            elif option2 == "2":
                                cmd = os.system("apt-get install dex2jar")

                            elif option2 == "3":
                                cmd = os.system(
                                    "apt-get install python-diStorm3")
                            elif option2 == "4":
                                cmd = os.system("apt-get install edb-debugger")
                            elif option2 == "5":
                                cmd = os.system("apt-get install jad")
                            elif option2 == "6":
                                cmd = os.system("apt-get install javasnoop")
                            elif option2 == "7":
                                cmd = os.system("apt-get install JD")
                            elif option2 == "8":
                                cmd = os.system("apt-get install OllyDbg")
                            elif option2 == "9":
                                cmd = os.system("apt-get install smali")
                            elif option2 == "10":
                                cmd = os.system("apt-get install Valgrind")
                            elif option2 == "11":
                                cmd = os.system("apt-get install YARA")
                            elif option2 == "back":
                                inicio()
                            elif option2 == "gohome":
                                initio1()
                            elif option2 == "0":
                                cmd = os.system(
                                    "apt-get install -y apktool dex2jar python-diStorm3 edb-debugger jad javasnoop JD OllyDbg smali Valgrind YARA")
                            else:
                                print(
                                    "\033[1;31mSorry, that was an invalid command!\033[1;m")
                        while opcion1 == "13":
                            print('''
\033[1;36m=+[ Hardware Hacking\033[1;m

 1) android-sdk
 2) apktool
 3) Arduino
 4) dex2jar
 5) Sakis3G
 6) smali

0) Install all Hardware Hacking tools

						''')
                            print(
                                "\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
                            option2 = input("\033[1;36mkat > \033[1;m")
                            if option2 == "1":
                                cmd = os.system("apt-get install android-sdk")

                            elif option2 == "2":
                                cmd = os.system("apt-get install apktool")

                            elif option2 == "3":
                                cmd = os.system("apt-get install arduino")
                            elif option2 == "4":
                                cmd = os.system("apt-get install dex2jar")
                            elif option2 == "5":
                                cmd = os.system("apt-get install sakis3g")
                            elif option2 == "6":
                                cmd = os.system("apt-get install smali")

                            elif option2 == "back":
                                inicio()
                            elif option2 == "gohome":
                                initio1()
                            elif option2 == "0":
                                cmd = os.system(
                                    "apt-get install -y android-sdk apktool arduino dex2jar sakis3g smali")
                            else:
                                print(
                                    "\033[1;31mSorry, that was an invalid command!\033[1;m")
                        while opcion1 == "14":
                            print('\n'
                                  '\033[1;36m=+[ Extra\033[1;m\n'
                                  '\n'
                                  '1) Wifresti\n'
                                  '2) Squid3\n'
                                  '				')
                            print(
                                "\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
                            option2 = input("\033[1;36mkat > \033[1;m")
                            if option2 == "1":
                                cmd = os.system(
                                    "git clone https://github.com/LionSec/wifresti.git && cp wifresti/wifresti.py /usr/bin/wifresti && chmod +x /usr/bin/wifresti && wifresti")
                                print(" ")
                            elif option2 == "2":
                                cmd = os.system("apt-get install squid3")
                                print(" ")
                            elif option2 == "back":
                                inicio()
                            elif option2 == "gohome":
                                initio1()

                inicio()

        initio1()
    except KeyboardInterrupt:
        print("Shutdown requested...Goodbye...")
    except Exception:
        traceback.print_exc(file=sys.stdout)
    sys.exit(0)


if __name__ == "__main__":
    main()
