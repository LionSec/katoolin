#!/usr/bin/env	python
# -*- coding: utf-8 -*-

import os,sys

#colors
green = "\033[1;32m"
red = "\033[1;31m"
reset = "\033[0m"
yellow = "\033[33m"

class category_element(object):

	def __init__(self):
		self.title = "--=[Information Gathering:"

	def set_agv(self, argv):
		self.argv = argv

	def main(self, name):
		name = name.replace('core/tools/', "")
		self.view_tools()
		action = False
		while action == False:
			try:
				option = raw_input("--=[kat(%s%s%s)› " %(yellow,name,reset))
			except KeyboardInterrupt:
				print "Closing, bye! - Kalitools"
			try:
				if option == "back":
					break
				elif option == "clear":
					os.system('clear')
				elif option == "help":
					print """ Help
	 <option>	Select option
	 back		Go back
	 view 		See list of tools
	 clear		Clean screen
					"""
				elif option == "view":
					self.view_tools()
				elif int(option) in range(1,58):
					self.install(option)
				elif option == "99":
					self.install(option)
				else:
					print red+"Sorry, that was an invalid command!"+reset
			except ValueError:
				pass
			
	def view_tools(self):
		os.system('clear')
		print green+self.title+reset
		print """	
	1) acccheck            30) hping3
	2) ace-voip            31) InTrace
	3) Amap                32) iSMTP
	4) Automater           33) lbd
	5) bing-ip2hosts       34) Maltego Teeth
	6) braa                35) masscan
	7) CaseFile            36) Metagoofil
	8) CDPSnarf            37) Miranda
	9) cisco-torch         38) nbtscan-unixwiz
	10) Cookie Cadger      39) Nmap
	11) copy-router-config 40) ntop
	12) DMitry             41) p0f
	13) dnmap              42) Parsero
	14) dnsenum            43) Recon-ng
	15) dnsmap             44) SET
	16) DNSRecon           45) smtp-user-enum
	17) dnstracer          46) snmp-check
	18) dnswalk            47) sslcaudit
	19) DotDotPwn          48) SSLsplit
	20) enum4linux         49) sslstrip
	21) enumIAX            50) SSLyze
	22) Fierce             51) THC-IPV6
	23) Firewalk           52) theHarvester
	24) fragroute          53) TLSSLed
	25) fragrouter         54) twofi
	26) Ghost Phisher      55) URLCrazy
	27) GoLismero          56) Wireshark
	28) goofile            57) WOL-E
	29) Xplico\n
	99) ALL\n
%sInsert the number of the tool to install it%s""" %(green,reset)
	
	def install(self, option):
		if option == "1":
			cmd = os.system("sudo apt install acccheck")
		elif option == "2":
			cmd = os.system("sudo apt install ace-voip")
		elif option == "3":
			cmd = os.system("sudo apt install amap")
		elif option == "4":
			cmd = os.system("sudo apt install automater")
		elif option == "5":
			print"\nManual installation is required for: %sbing-ip2hosts%s\n"
			print"Please visit: http://www.morningstarsecurity.com/research/bing-ip2hosts\n"
		elif option == "6":	
			cmd = os.system("sudo apt install braa")
		elif option == "7":		
			cmd = os.system("sudo apt install casefile")
		elif option == "8":
			cmd = os.system("sudo apt install cdpsnarf")
		elif option == "9":
			cmd = os.system("sudo apt install cisco-torch")
		elif option == "10":
			cmd = os.system("sudo apt install cookie-cadger")
		elif option == "11":
			cmd = os.system("sudo apt install copy-router-config")
		elif option == "12":
			cmd = os.system("sudo apt install dmitry")
		elif option == "13":
			cmd = os.system("sudo apt install dnmap")
		elif option == "14":
			cmd = os.system("sudo apt install dnsenum")
		elif option == "15":
			cmd = os.system("sudo apt install dnsmap")
		elif option == "16":
			cmd = os.system("sudo apt install dnsrecon")
		elif option == "17":
			cmd = os.system("sudo apt install dnstracer")
		elif option == "18":
			cmd = os.system("sudo apt install dnswalk")
		elif option == "19":
			cmd = os.system("sudo apt install dotdotpwn")
		elif option == "20":
			cmd = os.system("sudo apt install enum4linux")
		elif option == "21":
			cmd = os.system("sudo apt install enumiax")
		elif option == "22":
			cmd = os.system("sudo apt install fierce")
		elif option == "23":
			cmd = os.system("sudo apt install firewalk")
		elif option == "24":
			cmd = os.system("sudo apt install fragroute")
		elif option == "25":
			cmd = os.system("sudo apt install fragrouter")
		elif option == "26":
			cmd = os.system("sudo apt install ghost-phisher")
		elif option == "27":
			cmd = os.system("sudo apt install golismero")
		elif option == "28":
			cmd = os.system("sudo apt install goofile")
		elif option == "29":
			cmd = os.system("sudo apt install xplico")
		elif option == "30":
			cmd = os.system("sudo apt install hping3")
		elif option == "31":
			cmd = os.system("sudo apt install intrace")
		elif option == "32":
			cmd = os.system("sudo apt install ismtp")
		elif option == "33":
			cmd = os.system("sudo apt install lbd")
		elif option == "34":
			cmd = os.system("sudo apt install maltego-teeth")
		elif option == "35":
			cmd = os.system("sudo apt install masscan")
		elif option == "36":
			cmd = os.system("sudo apt install metagoofil")
		elif option == "37":
			cmd = os.system("sudo apt install miranda")
		elif option == "38":
			cmd = os.system("sudo apt install nbtscan-unixwiz")
		elif option == "39":
			cmd = os.system("sudo apt install nmap")
		elif option == "40":
			print"\nManual installation is required for: %sntop%s\n"
			print"Please visit: http://www.ntop.org/\n"
		elif option == "41":
			cmd = os.system("sudo apt install p0f")
		elif option == "42":
			cmd = os.system("sudo apt install parsero")
		elif option == "43":
			cmd = os.system("sudo apt install recon-ng")
		elif option == "44":
			cmd = os.system("sudo apt install set")
		elif option == "45":
			cmd = os.system("sudo apt install smtp-user-enum")
		elif option == "46":
			cmd = os.system("sudo apt install snmpcheck")
		elif option == "47":
			cmd = os.system("sudo apt install sslcaudit")
		elif option == "48":
			cmd = os.system("sudo apt install sslsplit")
		elif option == "49":
			cmd = os.system("sudo apt install sslstrip")
		elif option == "50":
			cmd = os.system("sudo apt install sslyze")
		elif option == "51":
			cmd = os.system("sudo apt install thc-ipv6")
		elif option == "52":
			cmd = os.system("sudo apt install theharvester")
		elif option == "53":
			cmd = os.system("sudo apt install tlssled")
		elif option == "54":
			cmd = os.system("sudo apt install twofi")
		elif option == "55":
			cmd = os.system("sudo apt install urlcrazy")
		elif option == "56":
			cmd = os.system("sudo apt install wireshark")
		elif option == "56":
			cmd = os.system("sudo apt install wol-e")
		elif option == "99":
			cmd = os.system("sudo apt install -y acccheck ace-voip amap automater braa casefile cdpsnarf cisco-torch cookie-cadger")
			cmd = os.system("sudo apt install -y copy-router-config dmitry dnmap dnsenum dnsmap dnsrecon dnstracer dnswalk dotdotpwn")
			cmd = os.system("sudo apt install -y enum4linux enumiax fierce firewalk fragroute fragrouter ghost-phisher golismero goofile")
			cmd = os.system("sudo apt install -y xplico hping3 intrace ismtp lbd maltego-teeth masscan metagoofil miranda nbtscan-unixwiz")
			cmd = os.system("sudo apt install -y nmap p0f parsero recon-ng set smtp-user-enum snmpcheck sslcaudit sslsplit sslstrip sslyze")
			cmd = os.system("sudo apt install -y thc-ipv6 theharvester tlssled twofi urlcrazy wireshark wol-e")
			cmd = os.system("sudo apt install -f install")