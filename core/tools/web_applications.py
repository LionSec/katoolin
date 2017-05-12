#!/usr/bin/env	python
# -*- coding: utf-8 -*-

import os,sys
from core.tools import load

class category_element(object):

	def set_agv(self, argv):
		self.argv = argv

	def main(self, name):
		name = name.replace('core/tools/', "")
		self.view_tools(name)
		action = False
		while action == False:
			try:
				option = raw_input(load.input(name))
			except KeyboardInterrupt:
				os.system('clear')
				break
			try:
				if option == "back":
					break
				elif option == "clear":
					os.system('clear')
				elif option == "help":
					load.help()
				elif option == "view":
					self.view_tools(name)
				elif int(option) in range(1,42):
					self.install(option)
				elif option == "99":
					self.install(option)
				else:
					load.error()
			except ValueError:
				pass
			
	def view_tools(self,name):
		os.system('clear')
		load.title(name)
		print """
	 1) apache-users  22) plecost
	 2) Arachni       23) Powerfuzzer
	 3) BBQSQL        24) ProxyStrike
	 4) BlindElephant 25) Recon-ng
	 5) Burp Suite    26) Skipfish
	 6) CutyCapt      27) sqlmap
	 7) DAVTest       28) Sqlninja
	 8) deblaze       29) sqlsus
	 9) DIRB          30) ua-tester
	10) DirBuster     31) Uniscan
	11) fimap         32) Vega
	12) FunkLoad      33) w3af
	13) Gobuster      34) WebScarab
	14) Grabber       35) Webshag
	15) jboss-autopwn 36) WebSlayer
	16) joomscan      37) WebSploit
	17) jSQL          38) Wfuzz
	18) Maltego Teeth 39) WPScan
	19) PadBuster     40) XSSer
	20) Paros         41) zaproxy 
	21) Parsero\n
	99) ALL\n
%sInsert the number of the tool to install it%s""" %(load.Green,load.Reset)
	
	def install(self, option):
		if option == "1":
			cmd = os.system("sudo apt install apache-users")
		elif option == "2":
			cmd = os.system("sudo apt install arachni")      
		elif option == "3":
			cmd = os.system("sudo apt install bbqsql")      
		elif option == "4":
			cmd = os.system("sudo apt install blindelephant")      
		elif option == "5":
			cmd = os.system("sudo apt install burpsuite")      
		elif option == "6":
			cmd = os.system("sudo apt install cutycapt")      
		elif option == "7":
			cmd = os.system("sudo apt install davtest")      
		elif option == "8":
			cmd = os.system("sudo apt install deblaze")      
		elif option == "9":
			cmd = os.system("sudo apt install dirb")      
		elif option == "10":
			cmd = os.system("sudo apt install dirbuster")
		elif option == "11":
			cmd = os.system("sudo apt install fimap")
		elif option == "12":
			cmd = os.system("sudo apt install funkload")
		elif option == "13":
			cmd = os.system("sudo apt install gobuster")
		elif option == "14":
			cmd = os.system("sudo apt install grabber")
		elif option == "15":
			cmd = os.system("sudo apt install jboss-autopwn")
		elif option == "16":
			cmd = os.system("sudo apt install joomscan")
		elif option == "17":
			cmd = os.system("sudo apt install jsql")
		elif option == "18":
			cmd = os.system("sudo apt install maltego-teeth")
		elif option == "19":
			cmd = os.system("sudo apt install padbuster")
		elif option == "20":
			cmd = os.system("sudo apt install paros")
		elif option == "21":
			cmd = os.system("sudo apt install parsero")
		elif option == "22":
			cmd = os.system("sudo apt install plecost")
		elif option == "23":
			cmd = os.system("sudo apt install powerfuzzer")
		elif option == "24":
			cmd = os.system("sudo apt install proxystrike")
		elif option == "25":
			cmd = os.system("sudo apt install recon-ng")
		elif option == "26":
			cmd = os.system("sudo apt install skipfish")
		elif option == "27":
			cmd = os.system("sudo apt install sqlmap")
		elif option == "28":
			cmd = os.system("sudo apt install sqlninja")
		elif option == "29":
			cmd = os.system("sudo apt install sqlsus")
		elif option == "30":
			cmd = os.system("sudo apt install ua-tester")
		elif option == "31":
			cmd = os.system("sudo apt install uniscan")
		elif option == "32":
			cmd = os.system("sudo apt install vega")
		elif option == "33":
			cmd = os.system("sudo apt install w3af")
		elif option == "34":
			cmd = os.system("sudo apt install webscarab")
		elif option == "35":
			print "\nManual installation is required for: Webshag"
			print "Please visit: https://www.scrt.ch/en/attack/downloads/webshag\n"
		elif option == "36":
			print "\nManual installation is required for: WebSlayer"
			print "Please visit: http://www.edge-security.com/webslayer.php\n"
		elif option == "37":
			cmd = os.system("sudo apt install websploit")
		elif option == "38":
			cmd = os.system("sudo apt install wfuzz")
		elif option == "39":
			cmd = os.system("sudo apt install wpscan")
		elif option == "40":
			cmd = os.system("sudo apt install xsser")
		elif option == "41":
			cmd = os.system("sudo apt install zaproxy")
		elif option == "99":
			cmd = os.system("sudo apt install -y apache-users arachni bbqsql blindelephant burpsuite cutycapt davtest deblaze")
			cmd = os.system("sudo apt install -y dirb dirbuster fimap funkload gobuster grabber jboss-autopwn joomscan jsql maltego-teeth")
			cmd = os.system("sudo apt install -y padbuster paros parsero plecost powerfuzzer proxystrike recon-ng skipfish sqlmap sqlninja")
			cmd = os.system("sudo apt install -y sqlsus ua-tester uniscan vega w3af webscarab websploit wfuzz wpscan xsser zaproxy")
			cmd = os.system("sudo apt -f install")