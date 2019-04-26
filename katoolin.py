#!/usr/bin/python

import os
import sys, traceback


if os.getuid() != 0:
	print "Sorry. This script requires sudo privledges"
	sys.exit()
def main():
	try:
		print ('''

 $$\   $$\             $$\                         $$\ $$\           
 $$ | $$  |            $$ |                        $$ |\__|          
 $$ |$$  /  $$$$$$\  $$$$$$\    $$$$$$\   $$$$$$\  $$ |$$\ $$$$$$$\  
 $$$$$  /   \____$$\ \_$$  _|  $$  __$$\ $$  __$$\ $$ |$$ |$$  __$$\ 
 $$  $$<    $$$$$$$ |  \033[1;36mKali linux tools installer\033[1;m |$$ |$$ |$$ |  $$ |
 \033[1;36m$$ |\$$\  $$  __$$ |  $$ |$$\ $$ |  $$ |$$ |  $$ |$$ |$$ |$$ |  $$ |
 $$ | \$$\ \$$$$$$$ |  \$$$$  |\$$$$$$  |\$$$$$$  |$$ |$$ |$$ |  $$ |
 \__|  \__| \_______|   \____/  \______/  \______/ \__|\__|\__|  \__| V2.0 \033[1;m


 \033[1;32m+ -- -- +=[ Author: LionSec | Homepage: www.neodrix.com\033[1;m
 \033[1;32m+ -- -- +=[ 331 Tools \033[1;m


\033[1;91m[W] Before updating your system , please remove all Kali-linux repositories to avoid any kind of problem .\033[1;m
		''')
		def inicio1():
			while True:
				print ('''
1) Add Kali repositories & Update 
2) View Categories
3) Install classicmenu indicator
4) Install Kali menu
5) Help

			''')

				opcion0 = raw_input("\033[1;36mkat > \033[1;m")
			
				while opcion0 == "1":
					print ('''
1) Add kali linux repositories
2) Update
3) Remove all kali linux repositories
4) View the contents of sources.list file

					''')
					repo = raw_input("\033[1;32mWhat do you want to do ?> \033[1;m")
					if repo == "1":
						cmd1 = os.system("apt-key adv --keyserver pool.sks-keyservers.net --recv-keys ED444FF07D8D0BF6")
						cmd2 = os.system("echo '# Kali linux repositories | Added by Katoolin\ndeb http://http.kali.org/kali kali-rolling main contrib non-free' >> /etc/apt/sources.list")
					elif repo == "2":
						cmd3 = os.system("apt-get update -m")
					elif repo == "3":
						infile = "/etc/apt/sources.list"
						outfile = "/etc/apt/sources.list"

						delete_list = ["# Kali linux repositories | Added by Katoolin\n", "deb http://http.kali.org/kali kali-rolling main contrib non-free\n"]
						fin = open(infile)
						os.remove("/etc/apt/sources.list")
						fout = open(outfile, "w+")
						for line in fin:
						    for word in delete_list:
						        line = line.replace(word, "")
						    fout.write(line)
						fin.close()
						fout.close()
						print ("\033[1;31m\nAll kali linux repositories have been deleted !\n\033[1;m")
					elif repo == "back":
						inicio1()
					elif repo == "gohome":
						inicio1()
					elif repo == "4":
						file = open('/etc/apt/sources.list', 'r')

						print (file.read())

					else:
						print ("\033[1;31mSorry, that was an invalid command!\033[1;m") 					
						

				if opcion0 == "3":
					print (''' 
ClassicMenu Indicator is a notification area applet (application indicator) for the top panel of Ubuntu's Unity desktop environment.

It provides a simple way to get a classic GNOME-style application menu for those who prefer this over the Unity dash menu.

Like the classic GNOME menu, it includes Wine games and applications if you have those installed.

For more information , please visit : http://www.florian-diesch.de/software/classicmenu-indicator/

''')
					repo = raw_input("\033[1;32mDo you want to install classicmenu indicator ? [y/n]> \033[1;m")
					if repo == "y":
						cmd1 = os.system("add-apt-repository ppa:diesch/testing && apt-get update")
						cmd = os.system("sudo apt-get install classicmenu-indicator")

				elif opcion0 == "4"	:
					repo = raw_input("\033[1;32mDo you want to install Kali menu ? [y/n]> \033[1;m")
					if repo == "y":
						cmd1 = os.system("apt-get install kali-menu")
				elif opcion0 == "5":
					print (''' 
****************** +Commands+ ******************


\033[1;32mback\033[1;m 	\033[1;33mGo back\033[1;m

\033[1;32mgohome\033[1;m	\033[1;33mGo to the main menu\033[1;m

		''')


				def inicio():
					while opcion0 == "2":
						print ('''
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
						print ("\033[1;32mSelect a category or press (0) to install all Kali linux tools .\n\033[1;m")

						opcion1 = raw_input("\033[1;36mkat > \033[1;m")
						if opcion1 == "back":
							inicio1()
						elif opcion1 == "gohome":
							inicio1()
						elif opcion1 == "0":
							cmd = os.system("apt-get -f install acccheck ace-voip amap automater braa casefile cdpsnarf cisco-torch cookie-cadger copy-router-config dmitry dnmap dnsenum dnsmap dnsrecon dnstracer dnswalk dotdotpwn enum4linux enumiax exploitdb fierce firewalk fragroute fragrouter ghost-phisher golismero goofile lbd maltego-teeth masscan metagoofil miranda nmap p0f parsero recon-ng set smtp-user-enum snmpcheck sslcaudit sslsplit sslstrip sslyze thc-ipv6 theharvester tlssled twofi urlcrazy wireshark wol-e xplico ismtp intrace hping3 bbqsql bed cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch copy-router-config doona dotdotpwn greenbone-security-assistant hexorbase jsql lynis nmap ohrwurm openvas-cli openvas-manager openvas-scanner oscanner powerfuzzer sfuzz sidguesser siparmyknife sqlmap sqlninja sqlsus thc-ipv6 tnscmd10g unix-privesc-check yersinia aircrack-ng asleap bluelog blueranger bluesnarfer bully cowpatty crackle eapmd5pass fern-wifi-cracker ghost-phisher giskismet gqrx kalibrate-rtl killerbee kismet mdk3 mfcuk mfoc mfterm multimon-ng pixiewps reaver redfang spooftooph wifi-honey wifitap wifite apache-users arachni bbqsql blindelephant burpsuite cutycapt davtest deblaze dirb dirbuster fimap funkload grabber jboss-autopwn joomscan jsql maltego-teeth padbuster paros parsero plecost powerfuzzer proxystrike recon-ng skipfish sqlmap sqlninja sqlsus ua-tester uniscan vega w3af webscarab websploit wfuzz wpscan xsser zaproxy burpsuite dnschef fiked hamster-sidejack hexinject iaxflood inviteflood ismtp mitmproxy ohrwurm protos-sip rebind responder rtpbreak rtpinsertsound rtpmixsound sctpscan siparmyknife sipp sipvicious sniffjoke sslsplit sslstrip thc-ipv6 voiphopper webscarab wifi-honey wireshark xspy yersinia zaproxy cryptcat cymothoa dbd dns2tcp http-tunnel httptunnel intersect nishang polenum powersploit pwnat ridenum sbd u3-pwn webshells weevely casefile cutycapt dos2unix dradis keepnote magictree metagoofil nipper-ng pipal armitage backdoor-factory cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch crackle jboss-autopwn linux-exploit-suggester maltego-teeth set shellnoob sqlmap thc-ipv6 yersinia beef-xss binwalk bulk-extractor chntpw cuckoo dc3dd ddrescue dumpzilla extundelete foremost galleta guymager iphone-backup-analyzer p0f pdf-parser pdfid pdgmail peepdf volatility xplico dhcpig funkload iaxflood inviteflood ipv6-toolkit mdk3 reaver rtpflood slowhttptest t50 termineter thc-ipv6 thc-ssl-dos acccheck burpsuite cewl chntpw cisco-auditing-tool cmospwd creddump crunch findmyhash gpp-decrypt hash-identifier hexorbase john johnny keimpx maltego-teeth maskprocessor multiforcer ncrack oclgausscrack pack patator polenum rainbowcrack rcracki-mt rsmangler statsprocessor thc-pptp-bruter truecrack webscarab wordlists zaproxy apktool dex2jar python-distorm3 edb-debugger jad javasnoop jd ollydbg smali valgrind yara android-sdk apktool arduino dex2jar sakis3g smali && wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")	
						while opcion1 == "1":
							print ('''
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
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install acccheck")

							elif opcion2 == "2":
								cmd = os.system("apt-get install ace-voip")

							elif opcion2 == "3":
								cmd = os.system("apt-get install amap")
							elif opcion2 == "4":
								cmd = os.system("apt-get install automater")
							elif opcion2 == "5":
								cmd = os.system("wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")
							elif opcion2 == "6":
								cmd = os.system("apt-get install braa")
							elif opcion2 == "7":
								cmd = os.system("apt-get install casefile")
							elif opcion2 == "8":
								cmd = os.system("apt-get install cdpsnarf")
							elif opcion2 == "9":
								cmd = os.system("apt-get install cisco-torch")
							elif opcion2 == "10":
								cmd = os.system("apt-get install cookie-cadger")
							elif opcion2 == "11":
								cmd = os.system("apt-get install copy-router-config")
							elif opcion2 == "12":
								cmd = os.system("apt-get install dmitry")
							elif opcion2 == "13":
								cmd = os.system("apt-get install dnmap")
							elif opcion2 == "14":
								cmd = os.system("apt-get install dnsenum")
							elif opcion2 == "15":
								cmd = os.system("apt-get install dnsmap")
							elif opcion2 == "16":
								cmd = os.system("apt-get install dnsrecon")
							elif opcion2 == "17":
								cmd = os.system("apt-get install dnstracer")
							elif opcion2 == "18":
								cmd = os.system("apt-get install dnswalk")
							elif opcion2 == "19":
								cmd = os.system("apt-get install dotdotpwn")
							elif opcion2 == "20":
								cmd = os.system("apt-get install enum4linux")
							elif opcion2 == "21":
								cmd = os.system("apt-get install enumiax")
							elif opcion2 == "22":
								cmd = os.system("apt-get install exploitdb")
							elif opcion2 == "23":
								cmd = os.system("apt-get install fierce")
							elif opcion2 == "24":
								cmd = os.system("apt-get install firewalk")
							elif opcion2 == "25":
								cmd = os.system("apt-get install fragroute")
							elif opcion2 == "26":
								cmd = os.system("apt-get install fragrouter")
							elif opcion2 == "27":
								cmd = os.system("apt-get install ghost-phisher")
							elif opcion2 == "28":
								cmd = os.system("apt-get install golismero")
							elif opcion2 == "29":
								cmd = os.system("apt-get install goofile")
							elif opcion2 == "30":
								cmd = os.system("apt-get install lbd")
							elif opcion2 == "31":
								cmd = os.system("apt-get install maltego-teeth")
							elif opcion2 == "32":
								cmd = os.system("apt-get install masscan")
							elif opcion2 == "33":
								cmd = os.system("apt-get install metagoofil")
							elif opcion2 == "34":
								cmd = os.system("apt-get install miranda")
							elif opcion2 == "35":
								cmd = os.system("apt-get install nmap")
							elif opcion2 == "36":
								print ('ntop is unavailable')
							elif opcion2 == "37":
								cmd = os.system("apt-get install p0f")
							elif opcion2 == "38":
								cmd = os.system("apt-get install parsero")
							elif opcion2 == "39":
								cmd = os.system("apt-get install recon-ng")
							elif opcion2 == "40":
								cmd = os.system("apt-get install set")
							elif opcion2 == "41":
								cmd = os.system("apt-get install smtp-user-enum")
							elif opcion2 == "42":
								cmd = os.system("apt-get install snmpcheck")
							elif opcion2 == "43":
								cmd = os.system("apt-get install sslcaudit")
							elif opcion2 == "44":
								cmd = os.system("apt-get install sslsplit")
							elif opcion2 == "45":
								cmd = os.system("apt-get install sslstrip")
							elif opcion2 == "46":
								cmd = os.system("apt-get install sslyze")
							elif opcion2 == "47":
								cmd = os.system("apt-get install thc-ipv6")
							elif opcion2 == "48":
								cmd = os.system("apt-get install theharvester")
							elif opcion2 == "49":
								cmd = os.system("apt-get install tlssled")
							elif opcion2 == "50":
								cmd = os.system("apt-get install twofi")
							elif opcion2 == "51":
								cmd = os.system("apt-get install urlcrazy")
							elif opcion2 == "52":
								cmd = os.system("apt-get install wireshark")
							elif opcion2 == "53":
								cmd = os.system("apt-get install wol-e")
							elif opcion2 == "54":
								cmd = os.system("apt-get install xplico")
							elif opcion2 == "55":
								cmd = os.system("apt-get install ismtp")
							elif opcion2 == "56":
								cmd = os.system("apt-get install intrace")
							elif opcion2 == "57":
								cmd = os.system("apt-get install hping3")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()		
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y acccheck ace-voip amap automater braa casefile cdpsnarf cisco-torch cookie-cadger copy-router-config dmitry dnmap dnsenum dnsmap dnsrecon dnstracer dnswalk dotdotpwn enum4linux enumiax exploitdb fierce firewalk fragroute fragrouter ghost-phisher golismero goofile lbd maltego-teeth masscan metagoofil miranda nmap p0f parsero recon-ng set smtp-user-enum snmpcheck sslcaudit sslsplit sslstrip sslyze thc-ipv6 theharvester tlssled twofi urlcrazy wireshark wol-e xplico ismtp intrace hping3 && wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")				
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")



						while opcion1 == "2":
							print ('''
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
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install bbqsql")

							elif opcion2 == "2":
								cmd = os.system("apt-get install bed")

							elif opcion2 == "3":
								cmd = os.system("apt-get install cisco-auditing-tool")
							elif opcion2 == "4":
								cmd = os.system("apt-get install cisco-global-exploiter")
							elif opcion2 == "5":
								cmd = os.system("apt-get install cisco-ocs")
							elif opcion2 == "6":
								cmd = os.system("apt-get install cisco-torch")
							elif opcion2 == "7":
								cmd = os.system("apt-get install copy-router-config")
							elif opcion2 == "8":
								cmd = os.system("apt-get install git && git clone https://github.com/stasinopoulos/commix.git commix && cd commix && python ./commix.py --install")
							elif opcion2 == "9":
								cmd = os.system("echo 'download page : http://www.cqure.net/wp/tools/database/dbpwaudit/'")
							elif opcion2 == "10":
								cmd = os.system("apt-get install doona")
							elif opcion2 == "11":
								cmd = os.system("apt-get install dotdotpwn")
							elif opcion2 == "12":
								cmd = os.system("apt-get install greenbone-security-assistant")
							elif opcion2 == "13":
								cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/gsd.git")
							elif opcion2 == "14":
								cmd = os.system("apt-get install hexorbase")
							elif opcion2 == "15":
								print ("Please download inguma from : http://inguma.sourceforge.net")
							elif opcion2 == "16":
								cmd = os.system("apt-get install jsql")
							elif opcion2 == "17":
								cmd = os.system("apt-get install lynis")
							elif opcion2 == "18":
								cmd = os.system("apt-get install nmap")
							elif opcion2 == "19":
								cmd = os.system("apt-get install ohrwurm")
							elif opcion2 == "20":
								cmd = os.system("apt-get install openvas-administrator")
							elif opcion2 == "21":
								cmd = os.system("apt-get install openvas-cli")
							elif opcion2 == "22":
								cmd = os.system("apt-get install openvas-manager")
							elif opcion2 == "23":
								cmd = os.system("apt-get install openvas-scanner")
							elif opcion2 == "24":
								cmd = os.system("apt-get install oscanner")
							elif opcion2 == "25":
								cmd = os.system("apt-get install powerfuzzer")
							elif opcion2 == "26":
								cmd = os.system("apt-get install sfuzz")
							elif opcion2 == "27":
								cmd = os.system("apt-get install sidguesser")
							elif opcion2 == "28":
								cmd = os.system("apt-get install siparmyknife")
							elif opcion2 == "29":
								cmd = os.system("apt-get install sqlmap")
							elif opcion2 == "30":
								cmd = os.system("apt-get install sqlninja")
							elif opcion2 == "31":
								cmd = os.system("apt-get install sqlsus")
							elif opcion2 == "32":
								cmd = os.system("apt-get install thc-ipv6")
							elif opcion2 == "33":
								cmd = os.system("apt-get install tnscmd10g")
							elif opcion2 == "34":
								cmd = os.system("apt-get install unix-privesc-check")
							elif opcion2 == "35":
								cmd = os.system("apt-get install yersinia")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()						
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y bbqsql bed cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch copy-router-config doona dotdotpwn greenbone-security-assistant hexorbase jsql lynis nmap ohrwurm openvas-cli openvas-manager openvas-scanner oscanner powerfuzzer sfuzz sidguesser siparmyknife sqlmap sqlninja sqlsus thc-ipv6 tnscmd10g unix-privesc-check yersinia")						
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")

						while opcion1 == "3":
							print ('''
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
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install aircrack-ng")

							elif opcion2 == "2":
								cmd = os.system("apt-get install asleap")

							elif opcion2 == "3":
								cmd = os.system("apt-get install bluelog")
							elif opcion2 == "4":
								cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/bluemaho.git")
							elif opcion2 == "5":
								cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/bluepot.git")
							elif opcion2 == "6":
								cmd = os.system("apt-get install blueranger")
							elif opcion2 == "7":
								cmd = os.system("apt-get install bluesnarfer")
							elif opcion2 == "8":
								cmd = os.system("apt-get install bully")
							elif opcion2 == "9":
								cmd = os.system("apt-get install cowpatty")
							elif opcion2 == "10":
								cmd = os.system("apt-get install crackle")
							elif opcion2 == "11":
								cmd = os.system("apt-get install eapmd5pass")
							elif opcion2 == "12":
								cmd = os.system("apt-get install fern-wifi-cracker")
							elif opcion2 == "13":
								cmd = os.system("apt-get install ghost-phisher")
							elif opcion2 == "14":
								cmd = os.system("apt-get install giskismet")
							elif opcion2 == "16":
								cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/gr-scan.git")
							elif opcion2 == "17":
								cmd = os.system("apt-get install kalibrate-rtl")
							elif opcion2 == "18":
								cmd = os.system("apt-get install killerbee")
							elif opcion2 == "19":
								cmd = os.system("apt-get install kismet")
							elif opcion2 == "20":
								cmd = os.system("apt-get install mdk3")
							elif opcion2 == "21":
								cmd = os.system("apt-get install mfcuk")
							elif opcion2 == "22":
								cmd = os.system("apt-get install mfoc")
							elif opcion2 == "23":
								cmd = os.system("apt-get install mfterm")
							elif opcion2 == "24":
								cmd = os.system("apt-get install multimon-ng")
							elif opcion2 == "25":
								cmd = os.system("apt-get install pixiewps")
							elif opcion2 == "26":
								cmd = os.system("apt-get install reaver")
							elif opcion2 == "27":
								cmd = os.system("apt-get install redfang")
							elif opcion2 == "28":
								cmd = os.system("apt-get install rtlsdr-scanner")
							elif opcion2 == "29":
								cmd = os.system("apt-get install spooftooph")
							elif opcion2 == "30":
								cmd = os.system("apt-get install wifi-honey")
							elif opcion2 == "31":
								cmd = os.system("apt-get install wifitap")
							elif opcion2 == "32":
								cmd = os.system("apt-get install wifite")
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y aircrack-ng asleap bluelog blueranger bluesnarfer bully cowpatty crackle eapmd5pass fern-wifi-cracker ghost-phisher giskismet gqrx kalibrate-rtl killerbee kismet mdk3 mfcuk mfoc mfterm multimon-ng pixiewps reaver redfang spooftooph wifi-honey wifitap wifite")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()						
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")
						while opcion1 == "4":
							print ('''
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
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")

							
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install apache-users")

							elif opcion2 == "2":
								cmd = os.system("apt-get install arachni")

							elif opcion2 == "3":
								cmd = os.system("apt-get install bbqsql")
							elif opcion2 == "4":
								cmd = os.system("apt-get install blindelephant")
							elif opcion2 == "5":
								cmd = os.system("apt-get install burpsuite")
							elif opcion2 == "6":
								cmd = os.system("apt-get install cutycapt")
							elif opcion2 == "7":
								cmd = os.system("apt-get install git && git clone https://github.com/stasinopoulos/commix.git commix && cd commix && python ./commix.py --install")
							elif opcion2 == "8":
								cmd = os.system("apt-get install davtest")
							elif opcion2 == "9":
								cmd = os.system("apt-get install deblaze")
							elif opcion2 == "10":
								cmd = os.system("apt-get install dirb")
							elif opcion2 == "11":
								cmd = os.system("apt-get install dirbuster")
							elif opcion2 == "12":
								cmd = os.system("apt-get install fimap")
							elif opcion2 == "13":
								cmd = os.system("apt-get install funkload")
							elif opcion2 == "14":
								cmd = os.system("apt-get install grabber")
							elif opcion2 == "15":
								cmd = os.system("apt-get install jboss-autopwn")
							elif opcion2 == "16":
								cmd = os.system("apt-get install joomscan")
							elif opcion2 == "17":
								cmd = os.system("apt-get install jsql")
							elif opcion2 == "18":
								cmd = os.system("apt-get install maltego-teeth")
							elif opcion2 == "19":
								cmd = os.system("apt-get install padbuster")
							elif opcion2 == "20":
								cmd = os.system("apt-get install paros")
							elif opcion2 == "21":
								cmd = os.system("apt-get install parsero")
							elif opcion2 == "22":
								cmd = os.system("apt-get install plecost")
							elif opcion2 == "23":
								cmd = os.system("apt-get install powerfuzzer")
							elif opcion2 == "24":
								cmd = os.system("apt-get install proxystrike")
							elif opcion2 == "25":
								cmd = os.system("apt-get install recon-ng")
							elif opcion2 == "26":
								cmd = os.system("apt-get install skipfish")
							elif opcion2 == "27":
								cmd = os.system("apt-get install sqlmap")
							elif opcion2 == "28":
								cmd = os.system("apt-get install sqlninja")
							elif opcion2 == "29":
								cmd = os.system("apt-get install sqlsus")
							elif opcion2 == "30":
								cmd = os.system("apt-get install ua-tester")
							elif opcion2 == "31":
								cmd = os.system("apt-get install uniscan")
							elif opcion2 == "32":
								cmd = os.system("apt-get install vega")
							elif opcion2 == "33":
								cmd = os.system("apt-get install w3af")
							elif opcion2 == "34":
								cmd = os.system("apt-get install webscarab")
							elif opcion2 == "35":
								print ("Webshag is unavailable")
							elif opcion2 == "36":
								cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/webslayer.git")
							elif opcion2 == "37":
								cmd = os.system("apt-get install websploit")
							elif opcion2 == "38":
								cmd = os.system("apt-get install wfuzz")
							elif opcion2 == "39":
								cmd = os.system("apt-get install wpscan")
							elif opcion2 == "40":
								cmd = os.system("apt-get install xsser")
							elif opcion2 == "41":
								cmd = os.system("apt-get install zaproxy")										
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()	
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y apache-users arachni bbqsql blindelephant burpsuite cutycapt davtest deblaze dirb dirbuster fimap funkload grabber jboss-autopwn joomscan jsql maltego-teeth padbuster paros parsero plecost powerfuzzer proxystrike recon-ng skipfish sqlmap sqlninja sqlsus ua-tester uniscan vega w3af webscarab websploit wfuzz wpscan xsser zaproxy")												
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")
						while opcion1 == "5":
							print ('''
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
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install burpsuite")

							elif opcion2 == "2":
								cmd = os.system("apt-get install dnschef")

							elif opcion2 == "3":
								cmd = os.system("apt-get install fiked")
							elif opcion2 == "4":
								cmd = os.system("apt-get install hamster-sidejack")
							elif opcion2 == "5":
								cmd = os.system("apt-get install hexinject")
							elif opcion2 == "6":
								cmd = os.system("apt-get install iaxflood")
							elif opcion2 == "7":
								cmd = os.system("apt-get install inviteflood")
							elif opcion2 == "8":
								cmd = os.system("apt-get install ismtp")
							elif opcion2 == "9":
								cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/isr-evilgrade.git")
							elif opcion2 == "10":
								cmd = os.system("apt-get install mitmproxy")
							elif opcion2 == "11":
								cmd = os.system("apt-get install ohrwurm")
							elif opcion2 == "12":
								cmd = os.system("apt-get install protos-sip")
							elif opcion2 == "13":
								cmd = os.system("apt-get install rebind")
							elif opcion2 == "14":
								cmd = os.system("apt-get install responder")
							elif opcion2 == "15":
								cmd = os.system("apt-get install rtpbreak")
							elif opcion2 == "16":
								cmd = os.system("apt-get install rtpinsertsound")
							elif opcion2 == "17":
								cmd = os.system("apt-get install rtpmixsound")
							elif opcion2 == "18":
								cmd = os.system("apt-get install sctpscan")
							elif opcion2 == "19":
								cmd = os.system("apt-get install siparmyknife")
							elif opcion2 == "20":
								cmd = os.system("apt-get install sipp")
							elif opcion2 == "21":
								cmd = os.system("apt-get install sipvicious")
							elif opcion2 == "22":
								cmd = os.system("apt-get install sniffjoke")
							elif opcion2 == "23":
								cmd = os.system("apt-get install sslsplit")
							elif opcion2 == "24":
								cmd = os.system("apt-get install sslstrip")
							elif opcion2 == "25":
								cmd = os.system("apt-get install thc-ipv6")
							elif opcion2 == "26":
								cmd = os.system("apt-get install voiphopper")
							elif opcion2 == "27":
								cmd = os.system("apt-get install webscarab")
							elif opcion2 == "28":
								cmd = os.system("apt-get install wifi-honey")
							elif opcion2 == "29":
								cmd = os.system("apt-get install wireshark")
							elif opcion2 == "30":
								cmd = os.system("apt-get install xspy")
							elif opcion2 == "31":
								cmd = os.system("apt-get install yersinia")
							elif opcion2 == "32":
								cmd = os.system("apt-get install zaproxy")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()


							elif opcion2 == "0":
								cmd = os.system("apt-get install -y burpsuite dnschef fiked hamster-sidejack hexinject iaxflood inviteflood ismtp mitmproxy ohrwurm protos-sip rebind responder rtpbreak rtpinsertsound rtpmixsound sctpscan siparmyknife sipp sipvicious sniffjoke sslsplit sslstrip thc-ipv6 voiphopper webscarab wifi-honey wireshark xspy yersinia zaproxy")  
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")

						while opcion1 == "6":
							print ('''
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
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install cryptcat")

							elif opcion2 == "2":
								cmd = os.system("apt-get install cymothoa")

							elif opcion2 == "3":
								cmd = os.system("apt-get install dbd")
							elif opcion2 == "4":
								cmd = os.system("apt-get install dns2tcp")
							elif opcion2 == "5":
								cmd = os.system("apt-get install http-tunnel")
							elif opcion2 == "6":
								cmd = os.system("apt-get install httptunnel")
							elif opcion2 == "7":
								cmd = os.system("apt-get install intersect")
							elif opcion2 == "8":
								cmd = os.system("apt-get install nishang")
							elif opcion2 == "9":
								cmd = os.system("apt-get install polenum")
							elif opcion2 == "10":
								cmd = os.system("apt-get install powersploit")
							elif opcion2 == "11":
								cmd = os.system("apt-get install pwnat")
							elif opcion2 == "12":
								cmd = os.system("apt-get install ridenum")
							elif opcion2 == "13":
								cmd = os.system("apt-get install sbd")
							elif opcion2 == "14":
								cmd = os.system("apt-get install u3-pwn")
							elif opcion2 == "15":
								cmd = os.system("apt-get install webshells")
							elif opcion2 == "16":
								cmd = os.system("apt-get install weevely")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y cryptcat cymothoa dbd dns2tcp http-tunnel httptunnel intersect nishang polenum powersploit pwnat ridenum sbd u3-pwn webshells weevely")
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")
						while opcion1 == "7":
							print ('''
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
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install casefile")

							elif opcion2 == "2":
								cmd = os.system("apt-get install cutycapt")

							elif opcion2 == "3":
								cmd = os.system("apt-get install dos2unix")
							elif opcion2 == "4":
								cmd = os.system("apt-get install dradis")
							elif opcion2 == "5":
								cmd = os.system("apt-get install keepnote")
							elif opcion2 == "6":
								cmd = os.system("apt-get install magictree")
							elif opcion2 == "7":
								cmd = os.system("apt-get install metagoofil")
							elif opcion2 == "8":
								cmd = os.system("apt-get install nipper-ng")
							elif opcion2 == "9":
								cmd = os.system("apt-get install pipal")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y casefile cutycapt dos2unix dradis keepnote magictree metagoofil nipper-ng pipal")  
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")

						while opcion1 == "8":
							print ('''
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
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install armitage")

							elif opcion2 == "2":
								cmd = os.system("apt-get install backdoor-factory")

							elif opcion2 == "3":
								cmd = os.system("apt-get install beef-xss")
							elif opcion2 == "4":
								cmd = os.system("apt-get install cisco-auditing-tool")
							elif opcion2 == "5":
								cmd = os.system("apt-get install cisco-global-exploiter")
							elif opcion2 == "6":
								cmd = os.system("apt-get install cisco-ocs")
							elif opcion2 == "7":
								cmd = os.system("apt-get install cisco-torch")
							elif opcion2 == "8":
								cmd = os.system("apt-get install git && git clone https://github.com/stasinopoulos/commix.git commix && cd commix && python ./commix.py --install")
							elif opcion2 == "9":
								cmd = os.system("apt-get install crackle")
							elif opcion2 == "10":
								cmd = os.system("apt-get install jboss-autopwn")
							elif opcion2 == "11":
								cmd = os.system("apt-get install linux-exploit-suggester")
							elif opcion2 == "12":
								cmd = os.system("apt-get install maltego-teeth")
							elif opcion2 == "13":
								cmd = os.system("apt-get install set")
							elif opcion2 == "14":
								cmd = os.system("apt-get install shellnoob")
							elif opcion2 == "15":
								cmd = os.system("apt-get install sqlmap")
							elif opcion2 == "16":
								cmd = os.system("apt-get install thc-ipv6")
							elif opcion2 == "17":
								cmd = os.system("apt-get install yersinia")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y armitage backdoor-factory cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch crackle jboss-autopwn linux-exploit-suggester maltego-teeth set shellnoob sqlmap thc-ipv6 yersinia beef-xss")  						
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")

						while opcion1 == "9":
							print ('''
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
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install binwalk")

							elif opcion2 == "2":
								cmd = os.system("apt-get install bulk-extractor")

							elif opcion2 == "3":
								cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/capstone.git")
							elif opcion2 == "4":
								cmd = os.system("apt-get install chntpw")
							elif opcion2 == "5":
								cmd = os.system("apt-get install cuckoo")
							elif opcion2 == "6":
								cmd = os.system("apt-get install dc3dd")
							elif opcion2 == "7":
								cmd = os.system("apt-get install ddrescue")
							elif opcion2 == "8":
								print ('dff is unavailable')
							elif opcion2 == "9":
								cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/distorm3.git")
							elif opcion2 == "10":
								cmd = os.system("apt-get install dumpzilla")
							elif opcion2 == "11":
								cmd = os.system("apt-get install extundelete")
							elif opcion2 == "12":
								cmd = os.system("apt-get install foremost")
							elif opcion2 == "13":
								cmd = os.system("apt-get install galleta")
							elif opcion2 == "14":
								cmd = os.system("apt-get install guymager")
							elif opcion2 == "15":
								cmd = os.system("apt-get install iphone-backup-analyzer")
							elif opcion2 == "16":
								cmd = os.system("apt-get install p0f")
							elif opcion2 == "17":
								cmd = os.system("apt-get install pdf-parser")
							elif opcion2 == "18":
								cmd = os.system("apt-get install pdfid")
							elif opcion2 == "19":
								cmd = os.system("apt-get install pdgmail")
							elif opcion2 == "20":
								cmd = os.system("apt-get install peepdf")
							elif opcion2 == "21":
								print ("Regripper is unavailable")
							elif opcion2 == "22":
								cmd = os.system("apt-get install volatility")
							elif opcion2 == "23":
								cmd = os.system("apt-get install xplico")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y binwalk bulk-extractor chntpw cuckoo dc3dd ddrescue dumpzilla extundelete foremost galleta guymager iphone-backup-analyzer p0f pdf-parser pdfid pdgmail peepdf volatility xplico")						
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")
						while opcion1 == "10":
							print ('''
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
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install dhcpig")

							elif opcion2 == "2":
								cmd = os.system("apt-get install funkload")

							elif opcion2 == "3":
								cmd = os.system("apt-get install iaxflood")
							elif opcion2 == "4":
								cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/inundator.git")
							elif opcion2 == "5":
								cmd = os.system("apt-get install inviteflood")
							elif opcion2 == "6":
								cmd = os.system("apt-get install ipv6-toolkit")
							elif opcion2 == "7":
								cmd = os.system("apt-get install mdk3")
							elif opcion2 == "8":
								cmd = os.system("apt-get install reaver")
							elif opcion2 == "9":
								cmd = os.system("apt-get install rtpflood")
							elif opcion2 == "10":
								cmd = os.system("apt-get install slowhttptest")
							elif opcion2 == "11":
								cmd = os.system("apt-get install t50")
							elif opcion2 == "12":
								cmd = os.system("apt-get install termineter")
							elif opcion2 == "13":
								cmd = os.system("apt-get install thc-ipv6")
							elif opcion2 == "14":
								cmd = os.system("apt-get install thc-ssl-dos ")    				             										
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y dhcpig funkload iaxflood inviteflood ipv6-toolkit mdk3 reaver rtpflood slowhttptest t50 termineter thc-ipv6 thc-ssl-dos")
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")
						while opcion1 == "11":
							print ('''
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
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install acccheck")

							elif opcion2 == "2":
								cmd = os.system("apt-get install burpsuite")

							elif opcion2 == "3":
								cmd = os.system("apt-get install cewl")
							elif opcion2 == "4":
								cmd = os.system("apt-get install chntpw")
							elif opcion2 == "5":
								cmd = os.system("apt-get install cisco-auditing-tool")
							elif opcion2 == "6":
								cmd = os.system("apt-get install cmospwd")
							elif opcion2 == "7":
								cmd = os.system("apt-get install creddump")
							elif opcion2 == "8":
								cmd = os.system("apt-get install crunch")
							elif opcion2 == "9":
								cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/dbpwaudit.git")
							elif opcion2 == "10":
								cmd = os.system("apt-get install findmyhash")
							elif opcion2 == "11":
								cmd = os.system("apt-get install gpp-decrypt")
							elif opcion2 == "12":
								cmd = os.system("apt-get install hash-identifier")
							elif opcion2 == "13":
								cmd = os.system("apt-get install hexorbase")
							elif opcion2 == "14":
								cmd = os.system("echo 'please visit : https://www.thc.org/thc-hydra/' ")
							elif opcion2 == "15":
								cmd = os.system("apt-get install john")
							elif opcion2 == "16":
								cmd = os.system("apt-get install johnny")
							elif opcion2 == "17":
								cmd = os.system("apt-get install keimpx")
							elif opcion2 == "18":
								cmd = os.system("apt-get install maltego-teeth")
							elif opcion2 == "19":
								cmd = os.system("apt-get install maskprocessor")
							elif opcion2 == "20":
								cmd = os.system("apt-get install multiforcer")
							elif opcion2 == "21":
								cmd = os.system("apt-get install ncrack")
							elif opcion2 == "22":
								cmd = os.system("apt-get install oclgausscrack")
							elif opcion2 == "23":
								cmd = os.system("apt-get install pack")
							elif opcion2 == "24":
								cmd = os.system("apt-get install patator")
							elif opcion2 == "25":
								cmd = os.system("echo 'please visit : http://www.leidecker.info/projects/phrasendrescher/index.shtml' ")
							elif opcion2 == "26":
								cmd = os.system("apt-get install polenum")
							elif opcion2 == "27":
								cmd = os.system("apt-get install rainbowcrack")
							elif opcion2 == "28":
								cmd = os.system("apt-get install rcracki-mt")
							elif opcion2 == "29":
								cmd = os.system("apt-get install rsmangler")
							elif opcion2 == "30":
								print ("Sqldict is unavailable")
							elif opcion2 == "31":
								cmd = os.system("apt-get install statsprocessor")
							elif opcion2 == "32":
								cmd = os.system("apt-get install thc-pptp-bruter")
							elif opcion2 == "33":
								cmd = os.system("apt-get install truecrack")
							elif opcion2 == "34":
								cmd = os.system("apt-get install webscarab")
							elif opcion2 == "35":
								cmd = os.system("apt-get install wordlists")
							elif opcion2 == "36":
								cmd = os.system("apt-get install zaproxy")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y acccheck burpsuite cewl chntpw cisco-auditing-tool cmospwd creddump crunch findmyhash gpp-decrypt hash-identifier hexorbase john johnny keimpx maltego-teeth maskprocessor multiforcer ncrack oclgausscrack pack patator polenum rainbowcrack rcracki-mt rsmangler statsprocessor thc-pptp-bruter truecrack webscarab wordlists zaproxy")
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")
						while opcion1 == "12" :
							print ('''
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
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install apktool")

							elif opcion2 == "2":
								cmd = os.system("apt-get install dex2jar")

							elif opcion2 == "3":
								cmd = os.system("apt-get install python-diStorm3")
							elif opcion2 == "4":
								cmd = os.system("apt-get install edb-debugger")
							elif opcion2 == "5":
								cmd = os.system("apt-get install jad")
							elif opcion2 == "6":
								cmd = os.system("apt-get install javasnoop")
							elif opcion2 == "7":
								cmd = os.system("apt-get install JD")
							elif opcion2 == "8":
								cmd = os.system("apt-get install OllyDbg")
							elif opcion2 == "9":
								cmd = os.system("apt-get install smali")
							elif opcion2 == "10":
								cmd = os.system("apt-get install Valgrind")
							elif opcion2 == "11":
								cmd = os.system("apt-get install YARA")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y apktool dex2jar python-diStorm3 edb-debugger jad javasnoop JD OllyDbg smali Valgrind YARA")
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")
						while opcion1 == "13" :
							print ('''
\033[1;36m=+[ Hardware Hacking\033[1;m

 1) android-sdk
 2) apktool
 3) Arduino
 4) dex2jar
 5) Sakis3G	
 6) smali

0) Install all Hardware Hacking tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install android-sdk")

							elif opcion2 == "2":
								cmd = os.system("apt-get install apktool")

							elif opcion2 == "3":
								cmd = os.system("apt-get install arduino")
							elif opcion2 == "4":
								cmd = os.system("apt-get install dex2jar")
							elif opcion2 == "5":
								cmd = os.system("apt-get install sakis3g")
							elif opcion2 == "6":
								cmd = os.system("apt-get install smali")

							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y android-sdk apktool arduino dex2jar sakis3g smali")
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")
						while opcion1 == "14" :
							print ('''
\033[1;36m=+[ Extra\033[1;m

1) Wifresti
2) Squid3
				''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("git clone https://github.com/LionSec/wifresti.git && cp wifresti/wifresti.py /usr/bin/wifresti && chmod +x /usr/bin/wifresti && wifresti")
								print (" ")
							elif opcion2 == "2":
								cmd = os.system("apt-get install squid3")
								print (" ")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()

				inicio()
		inicio1()
	except KeyboardInterrupt:
		print ("Shutdown requested...Goodbye...")
	except Exception:
		traceback.print_exc(file=sys.stdout)
	sys.exit(0)

if __name__ == "__main__":
    main()
