#!/usr/bin/python
import os
import sys, traceback

def main():
	try:
		print '''

 $$\   $$\             $$\                         $$\ $$\           
 $$ | $$  |            $$ |                        $$ |\__|          
 $$ |$$  /  $$$$$$\  $$$$$$\    $$$$$$\   $$$$$$\  $$ |$$\ $$$$$$$\  
 $$$$$  /   \____$$\ \_$$  _|  $$  __$$\ $$  __$$\ $$ |$$ |$$  __$$\ 
 $$  $$<    $$$$$$$ |  \033[1;36mKali linux tools installer\033[1;m |$$ |$$ |$$ |  $$ |
 \033[1;36m$$ |\$$\  $$  __$$ |  $$ |$$\ $$ |  $$ |$$ |  $$ |$$ |$$ |$$ |  $$ |
 $$ | \$$\ \$$$$$$$ |  \$$$$  |\$$$$$$  |\$$$$$$  |$$ |$$ |$$ |  $$ |
 \__|  \__| \_______|   \____/  \______/  \______/ \__|\__|\__|  \__| V1.0 \033[1;m


 \033[1;32m+ -- -- +=[ Author: LionSec | Homepage: www.lionsec.net\033[1;m
 \033[1;32m+ -- -- +=[ 330 Tools \033[1;m

		'''
		def inicio1():
			while True:
				print '''
1) Add Kali repositories & Update 
2) View Categories
3) Install classicmenu indicator
4) Install Kali menu
5) Help

			'''

				opcion0 = raw_input("\033[1;36mkat > \033[1;m")
			
				while opcion0 == "1":
					print '''
1) Add kali linux repositories
2) Update
3) Remove all kali linux repositories
4) View the contents of sources.list file

					'''
					repo = raw_input("\033[1;32mWhat do you want to do ?> \033[1;m")
					if repo == "1":
						cmd1 = os.system("apt-key adv --keyserver pgp.mit.edu --recv-keys ED444FF07D8D0BF6")
						cmd2 = os.system("echo '# Kali linux repositories | Added by Katoolin\ndeb http://http.kali.org/kali sana main non-free contrib\ndeb http://security.kali.org/kali-security sana/updates main contrib non-free\ndeb http://repo.kali.org/kali kali-bleeding-edge main' >> /etc/apt/sources.list")
					elif repo == "2":
						cmd3 = os.system("apt-get update -m")
					elif repo == "3":
						infile = "/etc/apt/sources.list"
						outfile = "/etc/apt/sources.list"

						delete_list = ["# Kali linux repositories | Added by Katoolin\n", "deb http://http.kali.org/kali sana main non-free contrib\n", "deb http://security.kali.org/kali-security sana/updates main contrib non-free\n","deb http://repo.kali.org/kali kali-bleeding-edge main\n"]
						fin = open(infile)
						os.remove("/etc/apt/sources.list")
						fout = open(outfile, "w+")
						for line in fin:
						    for word in delete_list:
						        line = line.replace(word, "")
						    fout.write(line)
						fin.close()
						fout.close()
						print " "
						print "\033[1;31mAll kali linux repositories have been deleted !\033[1;m"
						print " "
					elif repo == "back":
						inicio1()
					elif repo == "gohome":
						inicio1()
					elif repo == "4":
						file = open('/etc/apt/sources.list', 'r')

						print file.read()

					else:
						print ("\033[1;31mSorry, that was an invalid command!\033[1;m") 					
						

				if opcion0 == "3":
					print ''' 
ClassicMenu Indicator is a notification area applet (application indicator) for the top panel of Ubuntu's Unity desktop environment.

It provides a simple way to get a classic GNOME-style application menu for those who prefer this over the Unity dash menu.

Like the classic GNOME menu, it includes Wine games and applications if you have those installed.

For more information , please visit : http://www.florian-diesch.de/software/classicmenu-indicator/

'''
					repo = raw_input("\033[1;32mDo you want to install classicmenu indicator ? [y/n]> \033[1;m")
					if repo == "y":
						cmd1 = os.system("add-apt-repository ppa:diesch/testing && apt-get update")
						cmd = os.system("sudo apt-get install classicmenu-indicator")

				elif opcion0 == "4"	:
					repo = raw_input("\033[1;32mDo you want to install Kali menu ? [y/n]> \033[1;m")
					if repo == "y":
						cmd1 = os.system("apt-get install kali-menu")
				elif opcion0 == "5":
					print ''' 
****************** +Commands+ ****************** 


\033[1;32mback\033[1;m 	\033[1;33mGo back\033[1;m

\033[1;32mgohome\033[1;m	\033[1;33mGo to the main menu\033[1;m

		'''


				def inicio():
					while opcion0 == "2":
						print '''
\033[1;36m**************************** All Categories *****************************\033[1;m

1) Information Gathering			8) Exploitation Tools
2) Vulnerability Analysis			9) Forensics Tools
3) Wireless Attacks				10) Stress Testing
4) Web Applications				11) Password Attacks
5) Sniffing & Spoofing				12) Reverse Engineering
6) Maintaining Access				13) Hardware Hacking
7) Reporting Tools 				14) Extra
									
0) All

			 '''
						print "\033[1;32mSelect a category or press (0) to install all Kali linux tools .\033[1;m"

						print " "
						opcion1 = raw_input("\033[1;36mkat > \033[1;m")
						if opcion1 == "back":
							inicio1()
						elif opcion1 == "gohome":
							inicio1()
						elif opcion1 == "0":
							cmd = os.system("apt-get install acccheck ace-voip Amap Automater braa CaseFile CDPSnarf Cisco-torch Cookie-Cadger copy-router-config DMitry dnmap dnsenum dnsmap DNSRecon dnstracer dnswalk DotDotPwn enum4linux enumIAX exploitdb Fierce Firewalk fragroute fragrouter Ghost-Phisher GoLismero goofile lbd Maltego-Teeth masscan Metagoofil Miranda Nmap ntop p0f Parsero Recon-ng SET smtp-user-enum snmpcheck sslcaudit SSLsplit sslstrip SSLyze THC-IPV6 theHarvester TLSSLed twofi URLCrazy Wireshark WOL-E Xplico iSMTP InTrace hping3 BBQSQL BED cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch copy-router-config Doona DotDotPwn Greenbone-Security-Assistant HexorBase Inguma jSQL Lynis Nmap ohrwurm openvas-cli openvas-manager openvas-scanner Oscanner Powerfuzzer sfuzz SidGuesser SIPArmyKnife sqlmap Sqlninja sqlsus THC-IPV6 tnscmd10g unix-privesc-check Yersinia Aircrack-ng Asleap Bluelog BlueRanger Bluesnarfer Bully coWPAtty crackle eapmd5pass Fern-Wifi-Cracker Ghost-Phisher GISKismet Gqrx kalibrate-rtl KillerBee Kismet mdk3 mfcuk mfoc mfterm Multimon-NG PixieWPS Reaver redfang Spooftooph Wifi-Honey Wifitap Wifite apache-users Arachni BBQSQL BlindElephant BurpSuite CutyCapt DAVTest deblaze DIRB DirBuster fimap FunkLoad Grabber jboss-autopwn joomscan jSQL Maltego-Teeth PadBuster Paros Parsero plecost Powerfuzzer ProxyStrike Recon-ng Skipfish sqlmap Sqlninja sqlsus ua-tester Uniscan Vega w3af WebScarab Webshag WebSploit Wfuzz WPScan XSSer zaproxy BurpSuite DNSChef fiked hamster-sidejack HexInject iaxflood inviteflood iSMTP mitmproxy ohrwurm protos-sip rebind responder rtpbreak rtpinsertsound rtpmixsound sctpscan SIPArmyKnife SIPp SIPVicious SniffJoke SSLsplit sslstrip THC-IPV6 VoIPHopper WebScarab Wifi-Honey Wireshark xspy Yersinia zaproxy CryptCat Cymothoa dbd dns2tcp http-tunnel HTTPTunnel Intersect Nishang polenum PowerSploit pwnat RidEnum sbd U3-Pwn Webshells Weevely Winexe CaseFile CutyCapt dos2unix Dradis KeepNote MagicTree Metagoofil Nipper-ng pipal Armitage Backdoor-Factory cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch crackle jboss-autopwn Linux-Exploit-Suggester Maltego-Teeth SET ShellNoob sqlmap THC-IPV6 Yersinia beef-xss Armitage Backdoor-Factory cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch crackle jboss-autopwn Linux-Exploit-Suggester Maltego-Teeth SET ShellNoob sqlmap THC-IPV6 Yersinia DHCPig FunkLoad iaxflood inviteflood ipv6-toolkit mdk3 Reaver rtpflood SlowHTTPTest t50 Termineter THC-IPV6 THC-SSL-DOS acccheck BurpSuite CeWL chntpw cisco-auditing-tool CmosPwd creddump crunch findmyhash gpp-decrypt hash-identifier HexorBase John Johnny keimpx Maltego-Teeth Maskprocessor multiforcer Ncrack oclgausscrack PACK patator polenum RainbowCrack rcracki-mt RSMangler SQLdict Statsprocessor THC-pptp-bruter TrueCrack WebScarab wordlists zaproxy apktool dex2jar python-diStorm3 edb-debugger jad javasnoop JD OllyDbg smali Valgrind YARA android-sdk apktool Arduino dex2jar Sakis3G smali&& wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")	
						while opcion1 == "1":
							print '''
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
				 
						'''
							print "\033[1;32mInsert the number of the tool to install it .\033[1;m"
							print " "
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install acccheck")

							elif opcion2 == "2":
								cmd = os.system("apt-get install ace-voip")

							elif opcion2 == "3":
								cmd = os.system("apt-get install Amap")
							elif opcion2 == "4":
								cmd = os.system("apt-get install Automater")
							elif opcion2 == "5":
								cmd = os.system("wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")
							elif opcion2 == "6":
								cmd = os.system("apt-get install braa")
							elif opcion2 == "7":
								cmd = os.system("apt-get install CaseFile")
							elif opcion2 == "8":
								cmd = os.system("apt-get install CDPSnarf")
							elif opcion2 == "9":
								cmd = os.system("apt-get install cisco-torch")
							elif opcion2 == "10":
								cmd = os.system("apt-get install Cookie-Cadger")
							elif opcion2 == "11":
								cmd = os.system("apt-get install copy-router-config")
							elif opcion2 == "12":
								cmd = os.system("apt-get install DMitry")
							elif opcion2 == "13":
								cmd = os.system("apt-get install dnmap")
							elif opcion2 == "14":
								cmd = os.system("apt-get install dnsenum")
							elif opcion2 == "15":
								cmd = os.system("apt-get install dnsmap")
							elif opcion2 == "16":
								cmd = os.system("apt-get install DNSRecon")
							elif opcion2 == "17":
								cmd = os.system("apt-get install dnstracer")
							elif opcion2 == "18":
								cmd = os.system("apt-get install dnswalk")
							elif opcion2 == "19":
								cmd = os.system("apt-get install DotDotPwn")
							elif opcion2 == "20":
								cmd = os.system("apt-get install enum4linux")
							elif opcion2 == "21":
								cmd = os.system("apt-get install enumIAX")
							elif opcion2 == "22":
								cmd = os.system("apt-get install exploitdb")
							elif opcion2 == "23":
								cmd = os.system("apt-get install Fierce")
							elif opcion2 == "24":
								cmd = os.system("apt-get install Firewalk")
							elif opcion2 == "25":
								cmd = os.system("apt-get install fragroute")
							elif opcion2 == "26":
								cmd = os.system("apt-get install fragrouter")
							elif opcion2 == "27":
								cmd = os.system("apt-get install Ghost-Phisher")
							elif opcion2 == "28":
								cmd = os.system("apt-get install GoLismero")
							elif opcion2 == "29":
								cmd = os.system("apt-get install goofile")
							elif opcion2 == "30":
								cmd = os.system("apt-get install lbd")
							elif opcion2 == "31":
								cmd = os.system("apt-get install Maltego-Teeth")
							elif opcion2 == "32":
								cmd = os.system("apt-get install masscan")
							elif opcion2 == "33":
								cmd = os.system("apt-get install Metagoofil")
							elif opcion2 == "34":
								cmd = os.system("apt-get install Miranda")
							elif opcion2 == "35":
								cmd = os.system("apt-get install Nmap")
							elif opcion2 == "36":
								cmd = os.system("apt-get install ntop")
							elif opcion2 == "37":
								cmd = os.system("apt-get install p0f")
							elif opcion2 == "38":
								cmd = os.system("apt-get install Parsero")
							elif opcion2 == "39":
								cmd = os.system("apt-get install Recon-ng")
							elif opcion2 == "40":
								cmd = os.system("apt-get install SET")
							elif opcion2 == "41":
								cmd = os.system("apt-get install smtp-user-enum")
							elif opcion2 == "42":
								cmd = os.system("apt-get install snmpcheck")
							elif opcion2 == "43":
								cmd = os.system("apt-get install sslcaudit")
							elif opcion2 == "44":
								cmd = os.system("apt-get install SSLsplit")
							elif opcion2 == "45":
								cmd = os.system("apt-get install sslstrip")
							elif opcion2 == "46":
								cmd = os.system("apt-get install SSLyze")
							elif opcion2 == "47":
								cmd = os.system("apt-get install THC-IPV6")
							elif opcion2 == "48":
								cmd = os.system("apt-get install theHarvester")
							elif opcion2 == "49":
								cmd = os.system("apt-get install TLSSLed")
							elif opcion2 == "50":
								cmd = os.system("apt-get install twofi")
							elif opcion2 == "51":
								cmd = os.system("apt-get install URLCrazy")
							elif opcion2 == "52":
								cmd = os.system("apt-get install Wireshark")
							elif opcion2 == "53":
								cmd = os.system("apt-get install WOL-E")
							elif opcion2 == "54":
								cmd = os.system("apt-get install Xplico")
							elif opcion2 == "55":
								cmd = os.system("apt-get install iSMTP")
							elif opcion2 == "56":
								cmd = os.system("apt-get install InTrace")
							elif opcion2 == "57":
								cmd = os.system("apt-get install hping3")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()		
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y acccheck ace-voip Amap Automater braa CaseFile CDPSnarf Cisco-torch Cookie-Cadger copy-router-config DMitry dnmap dnsenum dnsmap DNSRecon dnstracer dnswalk DotDotPwn enum4linux enumIAX exploitdb Fierce Firewalk fragroute fragrouter Ghost-Phisher GoLismero goofile lbd Maltego-Teeth masscan Metagoofil Miranda Nmap ntop p0f Parsero Recon-ng SET smtp-user-enum snmpcheck sslcaudit SSLsplit sslstrip SSLyze THC-IPV6 theHarvester TLSSLed twofi URLCrazy Wireshark WOL-E Xplico iSMTP InTrace hping3 && wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")				
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")



						while opcion1 == "2":
							print '''
\033[1;36m=+[ Vulnerability Analysis\033[1;m

 1) BBQSQL				18) ohrwurm
 2) BED					19) openvas-administrator
 3) cisco-auditing-tool			20) openvas-cli
 4) cisco-global-exploiter		21) openvas-manager
 5) cisco-ocs				22) openvas-scanner
 6) cisco-torch				23) Oscanner
 7) copy-router-config			24) Powerfuzzer
 8) DBPwAudit				25) sfuzz
 9) Doona				26) SidGuesser
10) DotDotPwn				27) SIPArmyKnife
11) Greenbone Security Assistant	28) sqlmap
12) GSD					29) Sqlninja
13) HexorBase				30) sqlsus
14) Inguma				31) THC-IPV6
15) jSQL				32) tnscmd10g
16) Lynis				33) unix-privesc-check
17) Nmap				34) Yersinia

0) Install all Vulnerability Analysis tools
				 
						'''
							print "\033[1;32mInsert the number of the tool to install it .\033[1;m"
							print " "
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install BBQSQL")

							elif opcion2 == "2":
								cmd = os.system("apt-get install BED")

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
								cmd = os.system("echo 'Download page : http://www.cqure.net/wp/tools/database/dbpwaudit/'")
							elif opcion2 == "9":
								cmd = os.system("apt-get install Doona")
							elif opcion2 == "10":
								cmd = os.system("apt-get install DotDotPwn")
							elif opcion2 == "11":
								cmd = os.system("apt-get install Greenbone-Security-Assistant")
							elif opcion2 == "12":
								cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/gsd.git")
							elif opcion2 == "13":
								cmd = os.system("apt-get install HexorBase")
							elif opcion2 == "14":
								cmd = os.system("apt-get install Inguma")
							elif opcion2 == "15":
								cmd = os.system("apt-get install jSQL")
							elif opcion2 == "16":
								cmd = os.system("apt-get install Lynis")
							elif opcion2 == "17":
								cmd = os.system("apt-get install Nmap")
							elif opcion2 == "18":
								cmd = os.system("apt-get install ohrwurm")
							elif opcion2 == "19":
								cmd = os.system("apt-get install openvas-administrator")
							elif opcion2 == "20":
								cmd = os.system("apt-get install openvas-cli")
							elif opcion2 == "21":
								cmd = os.system("apt-get install openvas-manager")
							elif opcion2 == "22":
								cmd = os.system("apt-get install openvas-scanner")
							elif opcion2 == "23":
								cmd = os.system("apt-get install Oscanner")
							elif opcion2 == "24":
								cmd = os.system("apt-get install Powerfuzzer")
							elif opcion2 == "25":
								cmd = os.system("apt-get install sfuzz")
							elif opcion2 == "26":
								cmd = os.system("apt-get install SidGuesser")
							elif opcion2 == "27":
								cmd = os.system("apt-get install SIPArmyKnife")
							elif opcion2 == "28":
								cmd = os.system("apt-get install sqlmap")
							elif opcion2 == "29":
								cmd = os.system("apt-get install Sqlninja")
							elif opcion2 == "30":
								cmd = os.system("apt-get install sqlsus")
							elif opcion2 == "31":
								cmd = os.system("apt-get install THC-IPV6")
							elif opcion2 == "32":
								cmd = os.system("apt-get install tnscmd10g")
							elif opcion2 == "33":
								cmd = os.system("apt-get install unix-privesc-check")
							elif opcion2 == "34":
								cmd = os.system("apt-get install Yersinia")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()						
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y BBQSQL BED cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch copy-router-config Doona DotDotPwn Greenbone-Security-Assistant HexorBase Inguma jSQL Lynis Nmap ohrwurm openvas-cli openvas-manager openvas-scanner Oscanner Powerfuzzer sfuzz SidGuesser SIPArmyKnife sqlmap Sqlninja sqlsus THC-IPV6 tnscmd10g unix-privesc-check Yersinia")						
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")

						while opcion1 == "3":
							print '''
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
14) GISKismet				30) Wifi Honey
15) Gqrx				31) Wifitap
16) gr-scan				32) Wifite 

0) Install all Wireless Attacks tools
				 
						'''
							print "\033[1;32mInsert the number of the tool to install it .\033[1;m"
							print " "
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install Aircrack-ng")

							elif opcion2 == "2":
								cmd = os.system("apt-get install Asleap")

							elif opcion2 == "3":
								cmd = os.system("apt-get install Bluelog")
							elif opcion2 == "4":
								cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/bluemaho.git")
							elif opcion2 == "5":
								cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/bluepot.git")
							elif opcion2 == "6":
								cmd = os.system("apt-get install BlueRanger")
							elif opcion2 == "7":
								cmd = os.system("apt-get install Bluesnarfer")
							elif opcion2 == "8":
								cmd = os.system("apt-get install Bully")
							elif opcion2 == "9":
								cmd = os.system("apt-get install coWPAtty")
							elif opcion2 == "10":
								cmd = os.system("apt-get install crackle")
							elif opcion2 == "11":
								cmd = os.system("apt-get install eapmd5pass")
							elif opcion2 == "12":
								cmd = os.system("apt-get install Fern-Wifi-Cracker")
							elif opcion2 == "13":
								cmd = os.system("apt-get install Ghost-Phisher")
							elif opcion2 == "14":
								cmd = os.system("apt-get install GISKismet")
							elif opcion2 == "15":
								cmd = os.system("apt-get install Gqrx")
							elif opcion2 == "16":
								cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/gr-scan.git")
							elif opcion2 == "17":
								cmd = os.system("apt-get install kalibrate-rtl")
							elif opcion2 == "18":
								cmd = os.system("apt-get install KillerBee")
							elif opcion2 == "19":
								cmd = os.system("apt-get install Kismet")
							elif opcion2 == "20":
								cmd = os.system("apt-get install mdk3")
							elif opcion2 == "21":
								cmd = os.system("apt-get install mfcuk")
							elif opcion2 == "22":
								cmd = os.system("apt-get install mfoc")
							elif opcion2 == "23":
								cmd = os.system("apt-get install mfterm")
							elif opcion2 == "24":
								cmd = os.system("apt-get install Multimon-NG")
							elif opcion2 == "25":
								cmd = os.system("apt-get install PixieWPS")
							elif opcion2 == "26":
								cmd = os.system("apt-get install Reaver")
							elif opcion2 == "27":
								cmd = os.system("apt-get install redfang")
							elif opcion2 == "28":
								cmd = os.system("apt-get install RTLSDR-Scanner")
							elif opcion2 == "29":
								cmd = os.system("apt-get install Spooftooph")
							elif opcion2 == "30":
								cmd = os.system("apt-get install Wifi-Honey")
							elif opcion2 == "31":
								cmd = os.system("apt-get install Wifitap")
							elif opcion2 == "32":
								cmd = os.system("apt-get install Wifite")
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y Aircrack-ng Asleap Bluelog BlueRanger Bluesnarfer Bully coWPAtty crackle eapmd5pass Fern-Wifi-Cracker Ghost-Phisher GISKismet Gqrx kalibrate-rtl KillerBee Kismet mdk3 mfcuk mfoc mfterm Multimon-NG PixieWPS Reaver redfang Spooftooph Wifi-Honey Wifitap Wifite")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()						
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")
						while opcion1 == "4":
							print '''
\033[1;36m=+[ Web Applications\033[1;m

 1) apache-users				21) plecost
 2) Arachni					22) Powerfuzzer
 3) BBQSQL					23) ProxyStrike
 4) BlindElephant				24) Recon-ng
 5) Burp Suite					25) Skipfish
 6) CutyCapt					26) sqlmap
 7) DAVTest					27) Sqlninja
 8) deblaze					28) sqlsus
 9) DIRB 					29) ua-tester
10) DirBuster					30) Uniscan	
11) fimap					31) Vega
12) FunkLoad					32) w3af	 
13) Grabber					33) WebScarab
14) jboss-autopwn				34) Webshag
15) joomscan					35) WebSlayer	
16) jSQL					36) WebSploit
17) Maltego Teeth 				37) Wfuzz
18) PadBuster					38) WPScan
19) Paros 					39) XSSer
20) Parsero					40) zaproxy

0) Install all Web Applications tools
				 
						'''
							print "\033[1;32mInsert the number of the tool to install it .\033[1;m"

							print " "
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install apache-users")

							elif opcion2 == "2":
								cmd = os.system("apt-get install Arachni")

							elif opcion2 == "3":
								cmd = os.system("apt-get install BBQSQL")
							elif opcion2 == "4":
								cmd = os.system("apt-get install BlindElephant")
							elif opcion2 == "5":
								cmd = os.system("apt-get install BurpSuite")
							elif opcion2 == "6":
								cmd = os.system("apt-get install CutyCapt")
							elif opcion2 == "7":
								cmd = os.system("apt-get install DAVTest")
							elif opcion2 == "8":
								cmd = os.system("apt-get install deblaze")
							elif opcion2 == "9":
								cmd = os.system("apt-get install DIRB")
							elif opcion2 == "10":
								cmd = os.system("apt-get install DirBuster")
							elif opcion2 == "11":
								cmd = os.system("apt-get install fimap")
							elif opcion2 == "12":
								cmd = os.system("apt-get install FunkLoad")
							elif opcion2 == "13":
								cmd = os.system("apt-get install Grabber")
							elif opcion2 == "14":
								cmd = os.system("apt-get install jboss-autopwn")
							elif opcion2 == "15":
								cmd = os.system("apt-get install joomscan")
							elif opcion2 == "16":
								cmd = os.system("apt-get install jSQL")
							elif opcion2 == "17":
								cmd = os.system("apt-get install Maltego-Teeth")
							elif opcion2 == "18":
								cmd = os.system("apt-get install PadBuster")
							elif opcion2 == "19":
								cmd = os.system("apt-get install Paros")
							elif opcion2 == "20":
								cmd = os.system("apt-get install Parsero")
							elif opcion2 == "21":
								cmd = os.system("apt-get install plecost")
							elif opcion2 == "22":
								cmd = os.system("apt-get install Powerfuzzer")
							elif opcion2 == "23":
								cmd = os.system("apt-get install ProxyStrike")
							elif opcion2 == "24":
								cmd = os.system("apt-get install Recon-ng")
							elif opcion2 == "25":
								cmd = os.system("apt-get install Skipfish")
							elif opcion2 == "26":
								cmd = os.system("apt-get install sqlmap")
							elif opcion2 == "27":
								cmd = os.system("apt-get install Sqlninja")
							elif opcion2 == "28":
								cmd = os.system("apt-get install sqlsus")
							elif opcion2 == "29":
								cmd = os.system("apt-get install ua-tester")
							elif opcion2 == "30":
								cmd = os.system("apt-get install Uniscan")
							elif opcion2 == "31":
								cmd = os.system("apt-get install Vega")
							elif opcion2 == "32":
								cmd = os.system("apt-get install w3af")
							elif opcion2 == "33":
								cmd = os.system("apt-get install WebScarab")
							elif opcion2 == "34":
								cmd = os.system("apt-get install Webshag")
							elif opcion2 == "35":
								cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/webslayer.git")
							elif opcion2 == "36":
								cmd = os.system("apt-get install WebSploit")
							elif opcion2 == "37":
								cmd = os.system("apt-get install Wfuzz")
							elif opcion2 == "38":
								cmd = os.system("apt-get install WPScan")
							elif opcion2 == "39":
								cmd = os.system("apt-get install XSSer")
							elif opcion2 == "40":
								cmd = os.system("apt-get install zaproxy")										
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()	
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y apache-users Arachni BBQSQL BlindElephant BurpSuite CutyCapt DAVTest deblaze DIRB DirBuster fimap FunkLoad Grabber jboss-autopwn joomscan jSQL Maltego-Teeth PadBuster Paros Parsero plecost Powerfuzzer ProxyStrike Recon-ng Skipfish sqlmap Sqlninja sqlsus ua-tester Uniscan Vega w3af WebScarab Webshag WebSploit Wfuzz WPScan XSSer zaproxy")												
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")
						while opcion1 == "5":
							print '''
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
				 
						'''
							print "\033[1;32mInsert the number of the tool to install it .\033[1;m"
							print " "
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install BurpSuite")

							elif opcion2 == "2":
								cmd = os.system("apt-get install DNSChef")

							elif opcion2 == "3":
								cmd = os.system("apt-get install fiked")
							elif opcion2 == "4":
								cmd = os.system("apt-get install hamster-sidejack")
							elif opcion2 == "5":
								cmd = os.system("apt-get install HexInject")
							elif opcion2 == "6":
								cmd = os.system("apt-get install iaxflood")
							elif opcion2 == "7":
								cmd = os.system("apt-get install inviteflood")
							elif opcion2 == "8":
								cmd = os.system("apt-get install iSMTP")
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
								cmd = os.system("apt-get install SIPArmyKnife")
							elif opcion2 == "20":
								cmd = os.system("apt-get install SIPp")
							elif opcion2 == "21":
								cmd = os.system("apt-get install SIPVicious")
							elif opcion2 == "22":
								cmd = os.system("apt-get install SniffJoke")
							elif opcion2 == "23":
								cmd = os.system("apt-get install SSLsplit")
							elif opcion2 == "24":
								cmd = os.system("apt-get install sslstrip")
							elif opcion2 == "25":
								cmd = os.system("apt-get install THC-IPV6")
							elif opcion2 == "26":
								cmd = os.system("apt-get install VoIPHopper")
							elif opcion2 == "27":
								cmd = os.system("apt-get install WebScarab")
							elif opcion2 == "28":
								cmd = os.system("apt-get install Wifi-Honey")
							elif opcion2 == "29":
								cmd = os.system("apt-get install Wireshark")
							elif opcion2 == "30":
								cmd = os.system("apt-get install xspy")
							elif opcion2 == "31":
								cmd = os.system("apt-get install Yersinia")
							elif opcion2 == "32":
								cmd = os.system("apt-get install zaproxy")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()


							elif opcion2 == "0":
								cmd = os.system("apt-get install -y BurpSuite DNSChef fiked hamster-sidejack HexInject iaxflood inviteflood iSMTP mitmproxy ohrwurm protos-sip rebind responder rtpbreak rtpinsertsound rtpmixsound sctpscan SIPArmyKnife SIPp SIPVicious SniffJoke SSLsplit sslstrip THC-IPV6 VoIPHopper WebScarab Wifi-Honey Wireshark xspy Yersinia zaproxy")  
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")

						while opcion1 == "6":
							print '''
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
17) Winexe	

0) Install all Maintaining Access tools
				 
						'''
							print "\033[1;32mInsert the number of the tool to install it .\033[1;m"
							print " "
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install CryptCat")

							elif opcion2 == "2":
								cmd = os.system("apt-get install Cymothoa")

							elif opcion2 == "3":
								cmd = os.system("apt-get install dbd")
							elif opcion2 == "4":
								cmd = os.system("apt-get install dns2tcp")
							elif opcion2 == "5":
								cmd = os.system("apt-get install http-tunnel")
							elif opcion2 == "6":
								cmd = os.system("apt-get install HTTPTunnel")
							elif opcion2 == "7":
								cmd = os.system("apt-get install Intersect")
							elif opcion2 == "8":
								cmd = os.system("apt-get install Nishang")
							elif opcion2 == "9":
								cmd = os.system("apt-get install polenum")
							elif opcion2 == "10":
								cmd = os.system("apt-get install PowerSploit")
							elif opcion2 == "11":
								cmd = os.system("apt-get install pwnat")
							elif opcion2 == "12":
								cmd = os.system("apt-get install RidEnum")
							elif opcion2 == "13":
								cmd = os.system("apt-get install sbd")
							elif opcion2 == "14":
								cmd = os.system("apt-get install U3-Pwn")
							elif opcion2 == "15":
								cmd = os.system("apt-get install Webshells")
							elif opcion2 == "16":
								cmd = os.system("apt-get install Weevely")
							elif opcion2 == "17":
								cmd = os.system("apt-get install Winexe")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y CryptCat Cymothoa dbd dns2tcp http-tunnel HTTPTunnel Intersect Nishang polenum PowerSploit pwnat RidEnum sbd U3-Pwn Webshells Weevely Winexe")
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")
						while opcion1 == "7":
							print '''
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
				 
						'''
							print "\033[1;32mInsert the number of the tool to install it .\033[1;m"
							print " "
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install CaseFile")

							elif opcion2 == "2":
								cmd = os.system("apt-get install CutyCapt")

							elif opcion2 == "3":
								cmd = os.system("apt-get install dos2unix")
							elif opcion2 == "4":
								cmd = os.system("apt-get install Dradis")
							elif opcion2 == "5":
								cmd = os.system("apt-get install KeepNote")
							elif opcion2 == "6":
								cmd = os.system("apt-get install MagicTree")
							elif opcion2 == "7":
								cmd = os.system("apt-get install Metagoofil")
							elif opcion2 == "8":
								cmd = os.system("apt-get install Nipper-ng")
							elif opcion2 == "9":
								cmd = os.system("apt-get install pipal")
							elif opcion2 == "back":
								inicio()
		 					elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y CaseFile CutyCapt dos2unix Dradis KeepNote MagicTree Metagoofil Nipper-ng pipal")  
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")

						while opcion1 == "8":
							print '''
\033[1;36m=+[ Exploitation Tools\033[1;m

 1) Armitage
 2) Backdoor Factory
 3) BeEF
 4) cisco-auditing-tool
 5) cisco-global-exploiter	
 6) cisco-ocs
 7) cisco-torch
 8) crackle
 9) jboss-autopwn
10) Linux Exploit Suggester
11) Maltego Teeth
12) SET
13) ShellNoob
14) sqlmap
15) THC-IPV6
16) Yersinia

0) Install all Exploitation Tools
				 
						'''
							print "\033[1;32mInsert the number of the tool to install it .\033[1;m"
							print " "
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install Armitage")

							elif opcion2 == "2":
								cmd = os.system("apt-get install Backdoor-Factory")

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
								cmd = os.system("apt-get install crackle")
							elif opcion2 == "9":
								cmd = os.system("apt-get install jboss-autopwn")
							elif opcion2 == "10":
								cmd = os.system("apt-get install Linux-Exploit-Suggester")
							elif opcion2 == "11":
								cmd = os.system("apt-get install Maltego-Teeth")
							elif opcion2 == "12":
								cmd = os.system("apt-get install SET")
							elif opcion2 == "13":
								cmd = os.system("apt-get install ShellNoob")
							elif opcion2 == "14":
								cmd = os.system("apt-get install sqlmap")
							elif opcion2 == "15":
								cmd = os.system("apt-get install THC-IPV6")
							elif opcion2 == "16":
								cmd = os.system("apt-get install Yersinia")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y Armitage Backdoor-Factory cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch crackle jboss-autopwn Linux-Exploit-Suggester Maltego-Teeth SET ShellNoob sqlmap THC-IPV6 Yersinia beef-xss")  						
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")

						while opcion1 == "9":
							print '''
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
				 
						'''
							print "\033[1;32mInsert the number of the tool to install it .\033[1;m"
							print " "
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install Binwalk")

							elif opcion2 == "2":
								cmd = os.system("apt-get install bulk-extractor")

							elif opcion2 == "3":
								cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/capstone.git")
							elif opcion2 == "4":
								cmd = os.system("apt-get install chntpw")
							elif opcion2 == "5":
								cmd = os.system("apt-get install Cuckoo")
							elif opcion2 == "6":
								cmd = os.system("apt-get install dc3dd")
							elif opcion2 == "7":
								cmd = os.system("apt-get install ddrescue")
							elif opcion2 == "8":
								cmd = os.system("apt-get install DFF")
							elif opcion2 == "9":
								cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/distorm3.git")
							elif opcion2 == "10":
								cmd = os.system("apt-get install Dumpzilla")
							elif opcion2 == "11":
								cmd = os.system("apt-get install extundelete")
							elif opcion2 == "12":
								cmd = os.system("apt-get install Foremost")
							elif opcion2 == "13":
								cmd = os.system("apt-get install Galleta")
							elif opcion2 == "14":
								cmd = os.system("apt-get install Guymager")
							elif opcion2 == "15":
								cmd = os.system("apt-get install iPhone-Backup-Analyzer")
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
								cmd = os.system("apt-get install RegRipper")
							elif opcion2 == "22":
								cmd = os.system("apt-get install Volatility")
							elif opcion2 == "23":
								cmd = os.system("apt-get install Xplico")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y Binwalk bulk-extractor chntpw Cuckoo dc3dd ddrescue DFF Dumpzilla extundelete Foremost Galleta Guymager iPhone-Backup-Analyzer p0f pdf-parser pdfid pdgmail peepdf RegRipper Volatility Xplico")						
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")
						while opcion1 == "10":
							print '''
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
				 
						'''
							print "\033[1;32mInsert the number of the tool to install it .\033[1;m"
							print " "
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install DHCPig")

							elif opcion2 == "2":
								cmd = os.system("apt-get install FunkLoad")

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
								cmd = os.system("apt-get install Reaver")
							elif opcion2 == "9":
								cmd = os.system("apt-get install rtpflood")
							elif opcion2 == "10":
								cmd = os.system("apt-get install SlowHTTPTest")
							elif opcion2 == "11":
								cmd = os.system("apt-get install t50")
							elif opcion2 == "12":
								cmd = os.system("apt-get install Termineter")
							elif opcion2 == "13":
								cmd = os.system("apt-get install THC-IPV6")
							elif opcion2 == "14":
								cmd = os.system("apt-get install THC-SSL-DOS ")    				             										
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y DHCPig FunkLoad iaxflood inviteflood ipv6-toolkit mdk3 Reaver rtpflood SlowHTTPTest t50 Termineter THC-IPV6 THC-SSL-DOS")
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")
						while opcion1 == "11":
							print '''
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
				 
						'''
							print "\033[1;32mInsert the number of the tool to install it .\033[1;m"
							print " "
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install acccheck")

							elif opcion2 == "2":
								cmd = os.system("apt-get install BurpSuite")

							elif opcion2 == "3":
								cmd = os.system("apt-get install CeWL")
							elif opcion2 == "4":
								cmd = os.system("apt-get install chntpw")
							elif opcion2 == "5":
								cmd = os.system("apt-get install cisco-auditing-tool")
							elif opcion2 == "6":
								cmd = os.system("apt-get install CmosPwd")
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
								cmd = os.system("apt-get install HexorBase")
							elif opcion2 == "14":
								cmd = os.system("echo 'Please visit : https://www.thc.org/thc-hydra/' ")
							elif opcion2 == "15":
								cmd = os.system("apt-get install John")
							elif opcion2 == "16":
								cmd = os.system("apt-get install Johnny")
							elif opcion2 == "17":
								cmd = os.system("apt-get install keimpx")
							elif opcion2 == "18":
								cmd = os.system("apt-get install Maltego-Teeth")
							elif opcion2 == "19":
								cmd = os.system("apt-get install Maskprocessor")
							elif opcion2 == "20":
								cmd = os.system("apt-get install multiforcer")
							elif opcion2 == "21":
								cmd = os.system("apt-get install Ncrack")
							elif opcion2 == "22":
								cmd = os.system("apt-get install oclgausscrack")
							elif opcion2 == "23":
								cmd = os.system("apt-get install PACK")
							elif opcion2 == "24":
								cmd = os.system("apt-get install patator")
							elif opcion2 == "25":
								cmd = os.system("echo 'Please visit : http://www.leidecker.info/projects/phrasendrescher/index.shtml' ")
							elif opcion2 == "26":
								cmd = os.system("apt-get install polenum")
							elif opcion2 == "27":
								cmd = os.system("apt-get install RainbowCrack")
							elif opcion2 == "28":
								cmd = os.system("apt-get install rcracki-mt")
							elif opcion2 == "29":
								cmd = os.system("apt-get install RSMangler")
							elif opcion2 == "30":
								cmd = os.system("apt-get install SQLdict")
							elif opcion2 == "31":
								cmd = os.system("apt-get install Statsprocessor")
							elif opcion2 == "32":
								cmd = os.system("apt-get install THC-pptp-bruter")
							elif opcion2 == "33":
								cmd = os.system("apt-get install TrueCrack")
							elif opcion2 == "34":
								cmd = os.system("apt-get install WebScarab")
							elif opcion2 == "35":
								cmd = os.system("apt-get install wordlists")
							elif opcion2 == "36":
								cmd = os.system("apt-get install zaproxy")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y acccheck BurpSuite CeWL chntpw cisco-auditing-tool CmosPwd creddump crunch findmyhash gpp-decrypt hash-identifier HexorBase John Johnny keimpx Maltego-Teeth Maskprocessor multiforcer Ncrack oclgausscrack PACK patator polenum RainbowCrack rcracki-mt RSMangler SQLdict Statsprocessor THC-pptp-bruter TrueCrack WebScarab wordlists zaproxy")
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")
						while opcion1 == "12" :
							print '''
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
				 
						'''
							print "\033[1;32mInsert the number of the tool to install it .\033[1;m"
							print " "
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
							print '''
\033[1;36m=+[ Hardware Hacking\033[1;m

 1) android-sdk
 2) apktool
 3) Arduino
 4) dex2jar
 5) Sakis3G	
 6) smali

0) Install all Hardware Hacking tools
				 
						'''
							print "\033[1;32mInsert the number of the tool to install it .\033[1;m"
							print " "
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install android-sdk")

							elif opcion2 == "2":
								cmd = os.system("apt-get install apktool")

							elif opcion2 == "3":
								cmd = os.system("apt-get install Arduino")
							elif opcion2 == "4":
								cmd = os.system("apt-get install dex2jar")
							elif opcion2 == "5":
								cmd = os.system("apt-get install Sakis3G")
							elif opcion2 == "6":
								cmd = os.system("apt-get install smali")

							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y android-sdk apktool Arduino dex2jar Sakis3G smali")
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")
						while opcion1 == "14" :
							print '''
\033[1;36m=+[ Extra\033[1;m

1) Wifresti
2) Squid3
				'''
							print "\033[1;32mInsert the number of the tool to install it .\033[1;m"
							print " "
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("git clone https://github.com/LionSec/wifresti.git && cp wifresti/wifresti.py /usr/bin/wifresti && chmod +x /usr/bin/wifresti && wifresti")
								print " "
							elif opcion2 == "2":
								cmd = os.system("apt-get install squid3")
								print " "
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()

				inicio()
		inicio1()
	except KeyboardInterrupt:
		print "Shutdown requested...Goodbye..."
	except Exception:
		traceback.print_exc(file=sys.stdout)
	sys.exit(0)

if __name__ == "__main__":
    main()
