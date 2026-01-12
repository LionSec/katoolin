import os
import sys

from commands import open_shell
from style import print_menu, wait_for_input


# Menu actions mostly call apt-get install to fetch packages.


ALL_TOOLS_COMMAND = (
    "apt-get -f install acccheck ace-voip amap automater braa casefile cdpsnarf cisco-torch "
    "cookie-cadger copy-router-config dmitry dnmap dnsenum dnsmap dnsrecon dnstracer dnswalk "
    "dotdotpwn enum4linux enumiax exploitdb fierce firewalk fragroute fragrouter ghost-phisher "
    "golismero goofile lbd maltego-teeth masscan metagoofil miranda nmap p0f parsero recon-ng "
    "set smtp-user-enum snmpcheck sslcaudit sslsplit sslstrip sslyze thc-ipv6 theharvester tlssled "
    "twofi urlcrazy wireshark wol-e xplico ismtp intrace hping3 bbqsql bed cisco-auditing-tool "
    "cisco-global-exploiter cisco-ocs cisco-torch copy-router-config doona dotdotpwn "
    "greenbone-security-assistant hexorbase jsql lynis nmap ohrwurm openvas-cli openvas-manager "
    "openvas-scanner oscanner powerfuzzer sfuzz sidguesser siparmyknife sqlmap sqlninja sqlsus "
    "thc-ipv6 tnscmd10g unix-privesc-check yersinia aircrack-ng asleap bluelog blueranger bluesnarfer "
    "bully cowpatty crackle eapmd5pass fern-wifi-cracker ghost-phisher giskismet gqrx kalibrate-rtl "
    "killerbee kismet mdk3 mfcuk mfoc mfterm multimon-ng pixiewps reaver redfang spooftooph "
    "wifi-honey wifitap wifite apache-users arachni bbqsql blindelephant burpsuite cutycapt davtest "
    "deblaze dirb dirbuster fimap funkload grabber jboss-autopwn joomscan jsql maltego-teeth padbuster "
    "paros parsero plecost powerfuzzer proxystrike recon-ng skipfish sqlmap sqlninja sqlsus ua-tester "
    "uniscan vega w3af webscarab websploit wfuzz wpscan xsser zaproxy burpsuite dnschef fiked "
    "hamster-sidejack hexinject iaxflood inviteflood ismtp mitmproxy ohrwurm protos-sip rebind responder "
    "rtpbreak rtpinsertsound rtpmixsound sctpscan siparmyknife sipp sipvicious sniffjoke sslsplit sslstrip "
    "thc-ipv6 voiphopper webscarab wifi-honey wireshark xspy yersinia zaproxy cryptcat cymothoa dbd dns2tcp "
    "http-tunnel httptunnel intersect nishang polenum powersploit pwnat ridenum sbd u3-pwn webshells weevely "
    "casefile cutycapt dos2unix dradis keepnote magictree metagoofil nipper-ng pipal armitage backdoor-factory "
    "cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch crackle jboss-autopwn linux-exploit-suggester "
    "maltego-teeth set shellnoob sqlmap thc-ipv6 yersinia beef-xss binwalk bulk-extractor chntpw cuckoo dc3dd "
    "ddrescue dumpzilla extundelete foremost galleta guymager iphone-backup-analyzer p0f pdf-parser pdfid pdgmail "
    "peepdf volatility xplico dhcpig funkload iaxflood inviteflood ipv6-toolkit mdk3 reaver rtpflood slowhttptest "
    "t50 termineter thc-ipv6 thc-ssl-dos acccheck burpsuite cewl chntpw cisco-auditing-tool cmospwd creddump crunch "
    "findmyhash gpp-decrypt hash-identifier hexorbase john johnny keimpx maltego-teeth maskprocessor multiforcer ncrack "
    "oclgausscrack pack patator polenum rainbowcrack rcracki-mt rsmangler statsprocessor thc-pptp-bruter truecrack "
    "webscarab wordlists zaproxy apktool dex2jar python-distorm3 edb-debugger jad javasnoop jd ollydbg smali valgrind yara "
    "android-sdk apktool arduino dex2jar sakis3g smali && wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz "
    "&& tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/"
)

def category_information_gathering():
    while True:
        options = [
             ("1", "acccheck"), ("30", "lbd"),
             ("2", "ace-voip"), ("31", "Maltego Teeth"),
             ("3", "Amap"), ("32", "masscan"),
             ("4", "Automater"), ("33", "Metagoofil"),
             ("5", "bing-ip2hosts"), ("34", "Miranda"),
             ("6", "braa"), ("35", "Nmap"),
             ("7", "CaseFile"), ("36", "ntop"),
             ("8", "CDPSnarf"), ("37", "p0f"),
             ("9", "cisco-torch"), ("38", "Parsero"),
             ("10", "Cookie Cadger"), ("39", "Recon-ng"),
             ("11", "copy-router-config"), ("40", "SET"),
             ("12", "DMitry"), ("41", "smtp-user-enum"),
             ("13", "dnmap"), ("42", "snmpcheck"),
             ("14", "dnsenum"), ("43", "sslcaudit"),
             ("15", "dnsmap"), ("44", "SSLsplit"),
             ("16", "DNSRecon"), ("45", "sslstrip"),
             ("17", "dnstracer"), ("46", "SSLyze"),
             ("18", "dnswalk"), ("47", "THC-IPV6"),
             ("19", "DotDotPwn"), ("48", "theHarvester"),
             ("20", "enum4linux"), ("49", "TLSSLed"),
             ("21", "enumIAX"), ("50", "twofi"),
             ("22", "exploitdb"), ("51", "URLCrazy"),
             ("23", "Fierce"), ("52", "Wireshark"),
             ("24", "Firewalk"), ("53", "WOL-E"),
             ("25", "fragroute"), ("54", "Xplico"),
             ("26", "fragrouter"), ("55", "iSMTP"),
             ("27", "Ghost Phisher"), ("56", "InTrace"),
             ("28", "GoLismero"), ("57", "hping3"),
             ("29", "goofile")
        ]
        print_menu("Information Gathering", options, tools_mode=True)
        print("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
        option2 = input("\033[1;36mkat > \033[1;m")
        if option2 == "1":
            cmd = os.system("apt-get install acccheck")
            wait_for_input()
        elif option2 == "2":
            cmd = os.system("apt-get install ace-voip")
            wait_for_input()
        elif option2 == "3":
            cmd = os.system("apt-get install amap")
            wait_for_input()
        elif option2 == "4":
            cmd = os.system("apt-get install automater")
            wait_for_input()
        elif option2 == "5":
            cmd = os.system(
                "wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")
            wait_for_input()
        elif option2 == "6":
            cmd = os.system("apt-get install braa")
            wait_for_input()
        elif option2 == "7":
            cmd = os.system("apt-get install casefile")
            wait_for_input()
        elif option2 == "8":
            cmd = os.system("apt-get install cdpsnarf")
            wait_for_input()
        elif option2 == "9":
            cmd = os.system("apt-get install cisco-torch")
            wait_for_input()
        elif option2 == "10":
            cmd = os.system(
                "apt-get install cookie-cadger")
            wait_for_input()
        elif option2 == "11":
            cmd = os.system(
                "apt-get install copy-router-config")
            wait_for_input()
        elif option2 == "12":
            cmd = os.system("apt-get install dmitry")
            wait_for_input()
        elif option2 == "13":
            cmd = os.system("apt-get install dnmap")
            wait_for_input()
        elif option2 == "14":
            cmd = os.system("apt-get install dnsenum")
            wait_for_input()
        elif option2 == "15":
            cmd = os.system("apt-get install dnsmap")
            wait_for_input()
        elif option2 == "16":
            cmd = os.system("apt-get install dnsrecon")
            wait_for_input()
        elif option2 == "17":
            cmd = os.system("apt-get install dnstracer")
            wait_for_input()
        elif option2 == "18":
            cmd = os.system("apt-get install dnswalk")
            wait_for_input()
        elif option2 == "19":
            cmd = os.system("apt-get install dotdotpwn")
            wait_for_input()
        elif option2 == "20":
            cmd = os.system("apt-get install enum4linux")
            wait_for_input()
        elif option2 == "21":
            cmd = os.system("apt-get install enumiax")
            wait_for_input()
        elif option2 == "22":
            cmd = os.system("apt-get install exploitdb")
            wait_for_input()
        elif option2 == "23":
            cmd = os.system("apt-get install fierce")
            wait_for_input()
        elif option2 == "24":
            cmd = os.system("apt-get install firewalk")
            wait_for_input()
        elif option2 == "25":
            cmd = os.system("apt-get install fragroute")
            wait_for_input()
        elif option2 == "26":
            cmd = os.system("apt-get install fragrouter")
            wait_for_input()
        elif option2 == "27":
            cmd = os.system(
                "apt-get install ghost-phisher")
            wait_for_input()
        elif option2 == "28":
            cmd = os.system("apt-get install golismero")
            wait_for_input()
        elif option2 == "29":
            cmd = os.system("apt-get install goofile")
            wait_for_input()
        elif option2 == "30":
            cmd = os.system("apt-get install lbd")
            wait_for_input()
        elif option2 == "31":
            cmd = os.system(
                "apt-get install maltego-teeth")
            wait_for_input()
        elif option2 == "32":
            cmd = os.system("apt-get install masscan")
            wait_for_input()
        elif option2 == "33":
            cmd = os.system("apt-get install metagoofil")
            wait_for_input()
        elif option2 == "34":
            cmd = os.system("apt-get install miranda")
            wait_for_input()
        elif option2 == "35":
            cmd = os.system("apt-get install nmap")
            wait_for_input()
        elif option2 == "36":
            print('ntop is unavailable')
            wait_for_input()
        elif option2 == "37":
            cmd = os.system("apt-get install p0f")
            wait_for_input()
        elif option2 == "38":
            cmd = os.system("apt-get install parsero")
            wait_for_input()
        elif option2 == "39":
            cmd = os.system("apt-get install recon-ng")
            wait_for_input()
        elif option2 == "40":
            cmd = os.system("apt-get install set")
            wait_for_input()
        elif option2 == "41":
            cmd = os.system(
                "apt-get install smtp-user-enum")
            wait_for_input()
        elif option2 == "42":
            cmd = os.system("apt-get install snmpcheck")
            wait_for_input()
        elif option2 == "43":
            cmd = os.system("apt-get install sslcaudit")
            wait_for_input()
        elif option2 == "44":
            cmd = os.system("apt-get install sslsplit")
            wait_for_input()
        elif option2 == "45":
            cmd = os.system("apt-get install sslstrip")
            wait_for_input()
        elif option2 == "46":
            cmd = os.system("apt-get install sslyze")
            wait_for_input()
        elif option2 == "47":
            cmd = os.system("apt-get install thc-ipv6")
            wait_for_input()
        elif option2 == "48":
            cmd = os.system("apt-get install theharvester")
            wait_for_input()
        elif option2 == "49":
            cmd = os.system("apt-get install tlssled")
            wait_for_input()
        elif option2 == "50":
            cmd = os.system("apt-get install twofi")
            wait_for_input()
        elif option2 == "51":
            cmd = os.system("apt-get install urlcrazy")
            wait_for_input()
        elif option2 == "52":
            cmd = os.system("apt-get install wireshark")
            wait_for_input()
        elif option2 == "53":
            cmd = os.system("apt-get install wol-e")
            wait_for_input()
        elif option2 == "54":
            cmd = os.system("apt-get install xplico")
            wait_for_input()
        elif option2 == "55":
            cmd = os.system("apt-get install ismtp")
            wait_for_input()
        elif option2 == "56":
            cmd = os.system("apt-get install intrace")
            wait_for_input()
        elif option2 == "57":
            cmd = os.system("apt-get install hping3")
            wait_for_input()
        elif option2 == "back":
            return "back"
        elif option2 == "gohome":
            return "gohome"
        elif option2 == "shell":
            open_shell()
        elif option2 == "exit" or option2 == "quit":
            sys.exit()
        elif option2 == "help":
            print("Available commands:\n"
                  "back\t\tGo back to main menu\n"
                  "gohome\t\tGo to the main menu\n"
                  "exit\t\tExit the program\n"
                  "help\t\tShow this help menu\n")
            wait_for_input()
        elif option2 == "0":
            cmd = os.system(
                "apt-get install -y acccheck ace-voip amap automater braa casefile cdpsnarf cisco-torch cookie-cadger copy-router-config dmitry dnmap dnsenum dnsmap dnsrecon dnstracer dnswalk dotdotpwn enum4linux enumiax exploitdb fierce firewalk fragroute fragrouter ghost-phisher golismero goofile lbd maltego-teeth masscan metagoofil miranda nmap p0f parsero recon-ng set smtp-user-enum snmpcheck sslcaudit sslsplit sslstrip sslyze thc-ipv6 theharvester tlssled twofi urlcrazy wireshark wol-e xplico ismtp intrace hping3 && wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")
            wait_for_input()
        elif option2 == "exit" or option2 == "quit":
            sys.exit()
        elif option2 == "help":
            print("Available commands:\n"
                  "back\t\tGo back to main menu\n"
                  "gohome\t\tGo to the main menu\n"
                  "exit\t\tExit the program\n"
                  "help\t\tShow this help menu\n")
            wait_for_input()
        elif option2 == "0":
            cmd = os.system(
                "apt-get install -y bbqsql bed cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch copy-router-config doona dotdotpwn greenbone-security-assistant hexorbase jsql lynis nmap ohrwurm openvas-cli openvas-manager openvas-scanner oscanner powerfuzzer sfuzz sidguesser siparmyknife sqlmap sqlninja sqlsus thc-ipv6 tnscmd10g unix-privesc-check yersinia")
            wait_for_input()
        else:
            print(
                "\033[1;31mSorry, that was an invalid command!\033[1;m")
            wait_for_input()
            wait_for_input()

def category_vulnerability_analysis():
    while True:
        options = [
            ("1", "BBQSQL"), ("18", "Nmap"),
            ("2", "BED"), ("19", "ohrwurm"),
            ("3", "cisco-auditing-tool"), ("20", "openvas-administrator"),
            ("4", "cisco-global-exploiter"), ("21", "openvas-cli"),
            ("5", "cisco-ocs"), ("22", "openvas-manager"),
            ("6", "cisco-torch"), ("23", "openvas-scanner"),
            ("7", "copy-router-config"), ("24", "Oscanner"),
            ("8", "commix"), ("25", "Powerfuzzer"),
            ("9", "DBPwAudit"), ("26", "sfuzz"),
            ("10", "DoonaDot"), ("27", "SidGuesser"),
            ("11", "DotPwn"), ("28", "SIPArmyKnife"),
            ("12", "Greenbone Security Assistant"), ("29", "sqlmap"),
            ("13", "GSD"), ("30", "Sqlninja"),
            ("14", "HexorBase"), ("31", "sqlsus"),
            ("15", "Inguma"), ("32", "THC-IPV6"),
            ("16", "jSQL"), ("33", "tnscmd10g"),
            ("17", "Lynis"), ("34", "unix-privesc-check"),
            ("35", "Yersinia")
        ]
        print_menu("Vulnerability Analysis", options, tools_mode=True)
        print("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
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
            return "back"
        elif option2 == "gohome":
            return "gohome"
        elif option2 == "shell":
            open_shell()
        elif option2 == "0":
            cmd = os.system(
                "apt-get install -y bbqsql bed cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch copy-router-config doona dotdotpwn greenbone-security-assistant hexorbase jsql lynis nmap ohrwurm openvas-cli openvas-manager openvas-scanner oscanner powerfuzzer sfuzz sidguesser siparmyknife sqlmap sqlninja sqlsus thc-ipv6 tnscmd10g unix-privesc-check yersinia")
        elif option2 == "exit" or option2 == "quit":
            sys.exit()
        elif option2 == "help":
            print("Available commands:\n"
                  "back\t\tGo back to main menu\n"
                  "gohome\t\tGo to the main menu\n"
                  "exit\t\tExit the program\n"
                  "help\t\tShow this help menu\n")
            wait_for_input()
        elif option2 == "0":
            cmd = os.system(
                "apt-get install -y bbqsql bed cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch copy-router-config doona dotdotpwn greenbone-security-assistant hexorbase jsql lynis nmap ohrwurm openvas-cli openvas-manager openvas-scanner oscanner powerfuzzer sfuzz sidguesser siparmyknife sqlmap sqlninja sqlsus thc-ipv6 tnscmd10g unix-privesc-check yersinia")
            wait_for_input()
        else:
            print(
                "\033[1;31mSorry, that was an invalid command!\033[1;m")
            wait_for_input()

def category_wireless_attacks():
    while True:
        options = [
            ("1", "Aircrack-ng"), ("17", "kalibrate-rtl"),
            ("2", "Asleap"), ("18", "KillerBee"),
            ("3", "Bluelog"), ("19", "Kismet"),
            ("4", "BlueMaho"), ("20", "mdk3"),
            ("5", "Bluepot"), ("21", "mfcuk"),
            ("6", "BlueRanger"), ("22", "mfoc"),
            ("7", "Bluesnarfer"), ("23", "mfterm"),
            ("8", "Bully"), ("24", "Multimon-NG"),
            ("9", "coWPAtty"), ("25", "PixieWPS"),
            ("10", "crackle"), ("26", "Reaver"),
            ("11", "eapmd5pass"), ("27", "redfang"),
            ("12", "Fern Wifi Cracker"), ("28", "RTLSDR Scanner"),
            ("13", "Ghost Phisher"), ("29", "Spooftooph"),
            ("14", "GISKismet"), ("30", "Wifi Honey"),
            ("16", "gr-scan"), ("31", "Wifitap"),
            ("32", "Wifite")
        ]
        print_menu("Wireless Attacks", options, tools_mode=True)
        print("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
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
            return "back"
        elif option2 == "gohome":
            return "gohome"
        elif option2 == "shell":
            open_shell()
        elif option2 == "exit" or option2 == "quit":
            sys.exit()
        elif option2 == "help":
            print("Available commands:\n"
                  "back\t\tGo back to main menu\n"
                  "gohome\t\tGo to the main menu\n"
                  "exit\t\tExit the program\n"
                  "help\t\tShow this help menu\n")
            wait_for_input()
        elif option2 == "0":
            cmd = os.system(
                "apt-get install -y bbqsql bed cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch copy-router-config doona dotdotpwn greenbone-security-assistant hexorbase jsql lynis nmap ohrwurm openvas-cli openvas-manager openvas-scanner oscanner powerfuzzer sfuzz sidguesser siparmyknife sqlmap sqlninja sqlsus thc-ipv6 tnscmd10g unix-privesc-check yersinia")
            wait_for_input()
        else:
            print(
                "\033[1;31mSorry, that was an invalid command!\033[1;m")
            wait_for_input()

def category_web_applications():
    while True:
        options = [
            ("1", "apache-users"), ("21", "Parsero"),
            ("2", "Arachni"), ("22", "plecost"),
            ("3", "BBQSQL"), ("23", "Powerfuzzer"),
            ("4", "BlindElephant"), ("24", "ProxyStrike"),
            ("5", "Burp Suite"), ("25", "Recon-ng"),
            ("6", "commix"), ("26", "Skipfish"),
            ("7", "CutyCapt"), ("27", "sqlmap"),
            ("8", "DAVTest"), ("28", "Sqlninja"),
            ("9", "deblaze"), ("29", "sqlsus"),
            ("10", "DIRB"), ("30", "ua-tester"),
            ("11", "DirBuster"), ("31", "Uniscan"),
            ("12", "fimap"), ("32", "Vega"),
            ("13", "FunkLoad"), ("33", "w3af"),
            ("14", "Grabber"), ("34", "WebScarab"),
            ("15", "jboss-autopwn"), ("35", "Webshag"),
            ("16", "joomscan"), ("36", "WebSlayer"),
            ("17", "jSQL"), ("37", "WebSploit"),
            ("18", "Maltego Teeth"), ("38", "Wfuzz"),
            ("19", "PadBuster"), ("39", "WPScan"),
            ("20", "Paros"), ("40", "XSSer"),
            ("41", "zaproxy")
        ]
        print_menu("Web Applications", options, tools_mode=True)
        print("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")

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
            return "back"
        elif option2 == "gohome":
            return "gohome"
        elif option2 == "shell":
            open_shell()
        elif option2 == "0":
            cmd = os.system(
                "apt-get install -y apache-users arachni bbqsql blindelephant burpsuite cutycapt davtest deblaze dirb dirbuster fimap funkload grabber jboss-autopwn joomscan jsql maltego-teeth padbuster paros parsero plecost powerfuzzer proxystrike recon-ng skipfish sqlmap sqlninja sqlsus ua-tester uniscan vega w3af webscarab websploit wfuzz wpscan xsser zaproxy")
        elif option2 == "exit" or option2 == "quit":
            sys.exit()
        elif option2 == "help":
            print("Available commands:\n"
                  "back\t\tGo back to main menu\n"
                  "gohome\t\tGo to the main menu\n"
                  "exit\t\tExit the program\n"
                  "help\t\tShow this help menu\n")
            wait_for_input()
        elif option2 == "0":
            cmd = os.system(
                "apt-get install -y bbqsql bed cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch copy-router-config doona dotdotpwn greenbone-security-assistant hexorbase jsql lynis nmap ohrwurm openvas-cli openvas-manager openvas-scanner oscanner powerfuzzer sfuzz sidguesser siparmyknife sqlmap sqlninja sqlsus thc-ipv6 tnscmd10g unix-privesc-check yersinia")
            wait_for_input()
        else:
            print(
                "\033[1;31mSorry, that was an invalid command!\033[1;m")
            wait_for_input()

def category_sniffing_spoofing():
    while True:
        options = [
            ("1", "Burp Suite"), ("17", "rtpmixsound"),
            ("2", "dnschef"), ("18", "sctpscan"),
            ("3", "fiked"), ("19", "siparmyknife"),
            ("4", "hamster-sidejack"), ("20", "sipp"),
            ("5", "hexinject"), ("21", "sipvicious"),
            ("6", "iaxflood"), ("22", "sniffjoke"),
            ("7", "inviteflood"), ("23", "sslsplit"),
            ("8", "ismtp"), ("24", "sslstrip"),
            ("9", "isr-evilgrade"), ("25", "THC-IPV6"),
            ("10", "mitmproxy"), ("26", "voiphopper"),
            ("11", "ohrwurm"), ("27", "WebScarab"),
            ("12", "protos-sip"), ("28", "Wifi Honey"),
            ("13", "rebind"), ("29", "Wireshark"),
            ("14", "Responder"), ("30", "xspy"),
            ("15", "rtpbreak"), ("31", "Yersinia"),
            ("16", "rtpinsertsound"), ("32", "zaproxy")
        ]
        print_menu("Sniffing & Spoofing", options, tools_mode=True)
        print("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
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
            return "back"
        elif option2 == "gohome":
            return "gohome"
        elif option2 == "shell":
            open_shell()

        elif option2 == "0":
            cmd = os.system(
                "apt-get install -y burpsuite dnschef fiked hamster-sidejack hexinject iaxflood inviteflood ismtp mitmproxy ohrwurm protos-sip rebind responder rtpbreak rtpinsertsound rtpmixsound sctpscan siparmyknife sipp sipvicious sniffjoke sslsplit sslstrip thc-ipv6 voiphopper webscarab wifi-honey wireshark xspy yersinia zaproxy")
        elif option2 == "exit" or option2 == "quit":
            sys.exit()
        elif option2 == "help":
            print("Available commands:\n"
                  "back\t\tGo back to main menu\n"
                  "gohome\t\tGo to the main menu\n"
                  "exit\t\tExit the program\n"
                  "help\t\tShow this help menu\n")
            wait_for_input()
        elif option2 == "0":
            cmd = os.system(
                "apt-get install -y bbqsql bed cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch copy-router-config doona dotdotpwn greenbone-security-assistant hexorbase jsql lynis nmap ohrwurm openvas-cli openvas-manager openvas-scanner oscanner powerfuzzer sfuzz sidguesser siparmyknife sqlmap sqlninja sqlsus thc-ipv6 tnscmd10g unix-privesc-check yersinia")
            wait_for_input()
        else:
            print(
                "\033[1;31mSorry, that was an invalid command!\033[1;m")
            wait_for_input()

def category_maintaining_access():
    while True:
        options = [
            ("1", "CryptCat"),
            ("2", "Cymothoa"),
            ("3", "dbd"),
            ("4", "dns2tcp"),
            ("5", "http-tunnel"),
            ("6", "HTTPTunnel"),
            ("7", "Intersect"),
            ("8", "Nishang"),
            ("9", "polenum"),
            ("10", "PowerSploit"),
            ("11", "pwnat"),
            ("12", "RidEnum"),
            ("13", "sbd"),
            ("14", "U3-Pwn"),
            ("15", "Webshells"),
            ("16", "Weevely")
        ]
        print_menu("Maintaining Access", options, tools_mode=True)
        print("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
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
            return "back"
        elif option2 == "gohome":
            return "gohome"
        elif option2 == "shell":
            open_shell()
        elif option2 == "0":
            cmd = os.system(
                "apt-get install -y cryptcat cymothoa dbd dns2tcp http-tunnel httptunnel intersect nishang polenum powersploit pwnat ridenum sbd u3-pwn webshells weevely")
        elif option2 == "exit" or option2 == "quit":
            sys.exit()
        elif option2 == "help":
            print("Available commands:\n"
                  "back\t\tGo back to main menu\n"
                  "gohome\t\tGo to the main menu\n"
                  "exit\t\tExit the program\n"
                  "help\t\tShow this help menu\n")
            wait_for_input()
        elif option2 == "0":
            cmd = os.system(
                "apt-get install -y bbqsql bed cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch copy-router-config doona dotdotpwn greenbone-security-assistant hexorbase jsql lynis nmap ohrwurm openvas-cli openvas-manager openvas-scanner oscanner powerfuzzer sfuzz sidguesser siparmyknife sqlmap sqlninja sqlsus thc-ipv6 tnscmd10g unix-privesc-check yersinia")
            wait_for_input()
        else:
            print(
                "\033[1;31mSorry, that was an invalid command!\033[1;m")
            wait_for_input()

def category_reporting_tools():
    while True:
        options = [
            ("1", "CaseFile"),
            ("2", "CutyCapt"),
            ("3", "dos2unix"),
            ("4", "Dradis"),
            ("5", "KeepNote"),
            ("6", "MagicTree"),
            ("7", "Metagoofil"),
            ("8", "Nipper-ng"),
            ("9", "pipal")
        ]
        print_menu("Reporting Tools", options, tools_mode=True)
        print("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
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
            return "back"
        elif option2 == "gohome":
            return "gohome"
        elif option2 == "shell":
            open_shell()
        elif option2 == "0":
            cmd = os.system(
                "apt-get install -y casefile cutycapt dos2unix dradis keepnote magictree metagoofil nipper-ng pipal")
        elif option2 == "exit" or option2 == "quit":
            sys.exit()
        elif option2 == "help":
            print("Available commands:\n"
                  "back\t\tGo back to main menu\n"
                  "gohome\t\tGo to the main menu\n"
                  "exit\t\tExit the program\n"
                  "help\t\tShow this help menu\n")
            wait_for_input()
        elif option2 == "0":
            cmd = os.system(
                "apt-get install -y bbqsql bed cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch copy-router-config doona dotdotpwn greenbone-security-assistant hexorbase jsql lynis nmap ohrwurm openvas-cli openvas-manager openvas-scanner oscanner powerfuzzer sfuzz sidguesser siparmyknife sqlmap sqlninja sqlsus thc-ipv6 tnscmd10g unix-privesc-check yersinia")
            wait_for_input()
        else:
            print(
                "\033[1;31mSorry, that was an invalid command!\033[1;m")
            wait_for_input()

def category_exploitation_tools():
    while True:
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
back) Go back
gohome) Go to main menu
shell) Open system shell

\t\t\t\t\t\t''')
        print("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
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
            return "back"
        elif option2 == "gohome":
            return "gohome"
        elif option2 == "shell":
            open_shell()
        elif option2 == "0":
            cmd = os.system(
                "apt-get install -y armitage backdoor-factory cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch crackle jboss-autopwn linux-exploit-suggester maltego-teeth set shellnoob sqlmap thc-ipv6 yersinia beef-xss")
        elif option2 == "exit" or option2 == "quit":
            sys.exit()
        elif option2 == "help":
            print("Available commands:\n"
                  "back\t\tGo back to main menu\n"
                  "gohome\t\tGo to the main menu\n"
                  "exit\t\tExit the program\n"
                  "help\t\tShow this help menu\n")
            wait_for_input()
        elif option2 == "0":
            cmd = os.system(
                "apt-get install -y bbqsql bed cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch copy-router-config doona dotdotpwn greenbone-security-assistant hexorbase jsql lynis nmap ohrwurm openvas-cli openvas-manager openvas-scanner oscanner powerfuzzer sfuzz sidguesser siparmyknife sqlmap sqlninja sqlsus thc-ipv6 tnscmd10g unix-privesc-check yersinia")
            wait_for_input()
        else:
            print(
                "\033[1;31mSorry, that was an invalid command!\033[1;m")
            wait_for_input()

def category_forensics_tools():
    while True:
        options = [
            ("1", "Binwalk"), ("11", "extundelete"),
            ("2", "bulk-extractor"), ("12", "Foremost"),
            ("3", "Capstone"), ("13", "Galleta"),
            ("4", "chntpw"), ("14", "Guymager"),
            ("5", "Cuckoo"), ("15", "iPhone Backup Analyzer"),
            ("6", "dc3dd"), ("16", "p0f"),
            ("7", "ddrescue"), ("17", "pdf-parser"),
            ("8", "DFF"), ("18", "pdfid"),
            ("9", "diStorm3"), ("19", "pdgmail"),
            ("10", "Dumpzilla"), ("20", "peepdf"),
            ("21", "RegRipper"), ("22", "Volatility"),
            ("23", "Xplico")
        ]
        print_menu("Forensics Tools", options, tools_mode=True)
        print("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
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
            return "back"
        elif option2 == "gohome":
            return "gohome"
        elif option2 == "shell":
            open_shell()
        elif option2 == "0":
            cmd = os.system(
                "apt-get install -y binwalk bulk-extractor chntpw cuckoo dc3dd ddrescue dumpzilla extundelete foremost galleta guymager iphone-backup-analyzer p0f pdf-parser pdfid pdgmail peepdf volatility xplico")
        elif option2 == "exit" or option2 == "quit":
            sys.exit()
        elif option2 == "help":
            print("Available commands:\n"
                  "back\t\tGo back to main menu\n"
                  "gohome\t\tGo to the main menu\n"
                  "exit\t\tExit the program\n"
                  "help\t\tShow this help menu\n")
            wait_for_input()
        elif option2 == "0":
            cmd = os.system(
                "apt-get install -y bbqsql bed cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch copy-router-config doona dotdotpwn greenbone-security-assistant hexorbase jsql lynis nmap ohrwurm openvas-cli openvas-manager openvas-scanner oscanner powerfuzzer sfuzz sidguesser siparmyknife sqlmap sqlninja sqlsus thc-ipv6 tnscmd10g unix-privesc-check yersinia")
            wait_for_input()
        else:
            print(
                "\033[1;31mSorry, that was an invalid command!\033[1;m")
            wait_for_input()

def category_stress_testing():
    while True:
        options = [
             ("1", "DHCPig"),
             ("2", "FunkLoad"),
             ("3", "iaxflood"),
             ("4", "Inundator"),
             ("5", "inviteflood"),
             ("6", "ipv6-toolkit"),
             ("7", "mdk3"),
             ("8", "Reaver"),
             ("9", "rtpflood"),
             ("10", "SlowHTTPTest"),
             ("11", "t50"),
             ("12", "Termineter"),
             ("13", "THC-IPV6"),
             ("14", "THC-SSL-DOS")
        ]
        print_menu("Stress Testing", options, tools_mode=True)
        print("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
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
            return "back"
        elif option2 == "gohome":
            return "gohome"
        elif option2 == "shell":
            open_shell()
        elif option2 == "0":
            cmd = os.system(
                "apt-get install -y dhcpig funkload iaxflood inviteflood ipv6-toolkit mdk3 reaver rtpflood slowhttptest t50 termineter thc-ipv6 thc-ssl-dos")
        elif option2 == "exit" or option2 == "quit":
            sys.exit()
        elif option2 == "help":
            print("Available commands:\n"
                  "back\t\tGo back to main menu\n"
                  "gohome\t\tGo to the main menu\n"
                  "exit\t\tExit the program\n"
                  "help\t\tShow this help menu\n")
            wait_for_input()
        elif option2 == "0":
            cmd = os.system(
                "apt-get install -y bbqsql bed cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch copy-router-config doona dotdotpwn greenbone-security-assistant hexorbase jsql lynis nmap ohrwurm openvas-cli openvas-manager openvas-scanner oscanner powerfuzzer sfuzz sidguesser siparmyknife sqlmap sqlninja sqlsus thc-ipv6 tnscmd10g unix-privesc-check yersinia")
            wait_for_input()
        else:
            print(
                "\033[1;31mSorry, that was an invalid command!\033[1;m")
            wait_for_input()

def category_password_attacks():
    while True:
        options = [
            ("1", "acccheck"), ("19", "Maskprocessor"),
            ("2", "Burp Suite"), ("20", "multiforcer"),
            ("3", "CeWL"), ("21", "Ncrack"),
            ("4", "chntpw"), ("22", "oclgausscrack"),
            ("5", "cisco-auditing-tool"), ("23", "PACK"),
            ("6", "CmosPwd"), ("24", "patator"),
            ("7", "creddump"), ("25", "phrasendrescher"),
            ("8", "crunch"), ("26", "polenum"),
            ("9", "DBPwAudit"), ("27", "RainbowCrack"),
            ("10", "findmyhash"), ("28", "rcracki-mt"),
            ("11", "gpp-decrypt"), ("29", "RSMangler"),
            ("12", "hash-identifier"), ("30", "SQLdict"),
            ("13", "HexorBase"), ("31", "Statsprocessor"),
            ("14", "THC-Hydra"), ("32", "THC-pptp-bruter"),
            ("15", "John the Ripper"), ("33", "TrueCrack"),
            ("16", "Johnny"), ("34", "WebScarab"),
            ("17", "keimpx"), ("35", "wordlists"),
            ("18", "Maltego Teeth"), ("36", "zaproxy")
        ]
        print_menu("Password Attacks", options, tools_mode=True)
        print("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
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
            return "back"
        elif option2 == "gohome":
            return "gohome"
        elif option2 == "shell":
            open_shell()
        elif option2 == "0":
            cmd = os.system(
                "apt-get install -y acccheck burpsuite cewl chntpw cisco-auditing-tool cmospwd creddump crunch findmyhash gpp-decrypt hash-identifier hexorbase john johnny keimpx maltego-teeth maskprocessor multiforcer ncrack oclgausscrack pack patator polenum rainbowcrack rcracki-mt rsmangler statsprocessor thc-pptp-bruter truecrack webscarab wordlists zaproxy")
        elif option2 == "exit" or option2 == "quit":
            sys.exit()
        elif option2 == "help":
            print("Available commands:\n"
                  "back\t\tGo back to main menu\n"
                  "gohome\t\tGo to the main menu\n"
                  "exit\t\tExit the program\n"
                  "help\t\tShow this help menu\n")
            wait_for_input()
        elif option2 == "0":
            cmd = os.system(
                "apt-get install -y bbqsql bed cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch copy-router-config doona dotdotpwn greenbone-security-assistant hexorbase jsql lynis nmap ohrwurm openvas-cli openvas-manager openvas-scanner oscanner powerfuzzer sfuzz sidguesser siparmyknife sqlmap sqlninja sqlsus thc-ipv6 tnscmd10g unix-privesc-check yersinia")
            wait_for_input()
        else:
            print(
                "\033[1;31mSorry, that was an invalid command!\033[1;m")
            wait_for_input()

def category_reverse_engineering():
    while True:
        options = [
            ("1", "apktool"),
            ("2", "dex2jar"),
            ("3", "diStorm3"),
            ("4", "edb-debugger"),
            ("5", "jad"),
            ("6", "javasnoop"),
            ("7", "JD-GUI"),
            ("8", "OllyDbg"),
            ("9", "smali"),
            ("10", "Valgrind"),
            ("11", "YARA")
        ]
        print_menu("Reverse Engineering", options, tools_mode=True)
        print("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
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
            return "back"
        elif option2 == "gohome":
            return "gohome"
        elif option2 == "shell":
            open_shell()
        elif option2 == "0":
            cmd = os.system(
                "apt-get install -y apktool dex2jar python-diStorm3 edb-debugger jad javasnoop JD OllyDbg smali Valgrind YARA")
        elif option2 == "exit" or option2 == "quit":
            sys.exit()
        elif option2 == "help":
            print("Available commands:\n"
                  "back\t\tGo back to main menu\n"
                  "gohome\t\tGo to the main menu\n"
                  "exit\t\tExit the program\n"
                  "help\t\tShow this help menu\n")
            wait_for_input()
        elif option2 == "0":
            cmd = os.system(
                "apt-get install -y bbqsql bed cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch copy-router-config doona dotdotpwn greenbone-security-assistant hexorbase jsql lynis nmap ohrwurm openvas-cli openvas-manager openvas-scanner oscanner powerfuzzer sfuzz sidguesser siparmyknife sqlmap sqlninja sqlsus thc-ipv6 tnscmd10g unix-privesc-check yersinia")
            wait_for_input()
        else:
            print(
                "\033[1;31mSorry, that was an invalid command!\033[1;m")
            wait_for_input()

def category_hardware_hacking():
    while True:
        options = [
            ("1", "android-sdk"),
            ("2", "apktool"),
            ("3", "Arduino"),
            ("4", "dex2jar"),
            ("5", "Sakis3G"),
            ("6", "smali")
        ]
        print_menu("Hardware Hacking", options, tools_mode=True)
        print("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
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
            return "back"
        elif option2 == "gohome":
            return "gohome"
        elif option2 == "shell":
            open_shell()
        elif option2 == "0":
            cmd = os.system(
                "apt-get install -y android-sdk apktool arduino dex2jar sakis3g smali")
        elif option2 == "exit" or option2 == "quit":
            sys.exit()
        elif option2 == "help":
            print("Available commands:\n"
                  "back\t\tGo back to main menu\n"
                  "gohome\t\tGo to the main menu\n"
                  "exit\t\tExit the program\n"
                  "help\t\tShow this help menu\n")
            wait_for_input()
        elif option2 == "0":
            cmd = os.system(
                "apt-get install -y bbqsql bed cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch copy-router-config doona dotdotpwn greenbone-security-assistant hexorbase jsql lynis nmap ohrwurm openvas-cli openvas-manager openvas-scanner oscanner powerfuzzer sfuzz sidguesser siparmyknife sqlmap sqlninja sqlsus thc-ipv6 tnscmd10g unix-privesc-check yersinia")
            wait_for_input()
        else:
            print(
                "\033[1;31mSorry, that was an invalid command!\033[1;m")
            wait_for_input()

def category_extra():
    while True:
        options = [
            ("1", "Wifresti"),
            ("2", "Squid3"),
        ]
        print_menu("Extra", options, tools_mode=True)
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
            return "back"
        elif option2 == "gohome":
            return "gohome"
        elif option2 == "shell":
            open_shell()

def run_categories_menu():
    # Dispatcher for the category submenus.
    while True:
        options = [
            ("1", "Information Gathering"),
            ("2", "Vulnerability Analysis"),
            ("3", "Wireless Attacks"),
            ("4", "Web Applications"),
            ("5", "Sniffing & Spoofing"),
            ("6", "Maintaining Access"),
            ("7", "Reporting Tools"),
            ("8", "Exploitation Tools"),
            ("9", "Forensics Tools"),
            ("10", "Stress Testing"),
            ("11", "Password Attacks"),
            ("12", "Reverse Engineering"),
            ("13", "Hardware Hacking"),
            ("14", "Extra"),
        ]
        print_menu("All Categories", options, tools_mode=True)
        print("\033[1;32mSelect a category or press (0) to install all Kali linux tools .\n\033[1;m")

        option = input("\033[1;36mkat > \033[1;m")
        if option == "back":
            return
        elif option == "gohome":
            return
        elif option == "shell":
            open_shell()
        elif option == "exit" or option == "quit":
            print("Shutdown requested...Goodbye...")
            sys.exit()
        elif option == "help":
            print("Available commands:\n"
                  "back\t\tGo back to main menu\n"
                  "gohome\t\tGo to the main menu\n"
                  "exit\t\tExit the program\n"
                  "help\t\tShow this help menu\n")
        elif option == "0":
            cmd = os.system(ALL_TOOLS_COMMAND)
        elif option == "1":
            result = category_information_gathering()
            if result == "gohome":
                return
        elif option == "2":
            result = category_vulnerability_analysis()
            if result == "gohome":
                return
        elif option == "3":
            result = category_wireless_attacks()
            if result == "gohome":
                return
        elif option == "4":
            result = category_web_applications()
            if result == "gohome":
                return
        elif option == "5":
            result = category_sniffing_spoofing()
            if result == "gohome":
                return
        elif option == "6":
            result = category_maintaining_access()
            if result == "gohome":
                return
        elif option == "7":
            result = category_reporting_tools()
            if result == "gohome":
                return
        elif option == "8":
            result = category_exploitation_tools()
            if result == "gohome":
                return
        elif option == "9":
            result = category_forensics_tools()
            if result == "gohome":
                return
        elif option == "10":
            result = category_stress_testing()
            if result == "gohome":
                return
        elif option == "11":
            result = category_password_attacks()
            if result == "gohome":
                return
        elif option == "12":
            result = category_reverse_engineering()
            if result == "gohome":
                return
        elif option == "13":
            result = category_hardware_hacking()
            if result == "gohome":
                return
        elif option == "14":
            result = category_extra()
            if result == "gohome":
                return
        else:
            print("\033[1;31mSorry, that was an invalid command!\033[1;m")
