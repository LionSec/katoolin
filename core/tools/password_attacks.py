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
				elif int(option) in range(1,37):
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
	 1) acccheck            19) Maskprocessor
	 2) Burp Suite          20) multiforcer
	 3) CeWL                21) Ncrack
	 4) chntpw              22) oclgausscrack
	 5) cisco-auditing-tool 23) PACK
	 6) CmosPwd             24) patator
	 7) creddump            25) phrasendrescher
	 8) crunch              26) polenum
	 9) DBPwAudit           27) RainbowCrack
	10) findmyhash          28) rcracki-mt
	11) gpp-decrypt         29) RSMangler
	12) hash-identifier     30) SQLdict
	13) HexorBase           31) Statsprocessor
	14) THC-Hydra           32) THC-pptp-bruter
	15) John the Ripper     33) TrueCrack
	16) Johnny              34) WebScarab
	17) keimpx              35) wordlists
	18) Maltego Teeth       36) zaproxy \n
	99) ALL\n
%sInsert the number of the tool to install it%s""" %(load.Green,load.Reset)

	def install(self, option):
		if option == "1":
			cmd = os.system("sudo apt install acccheck")
		elif option == "2":
			cmd = os.system("sudo apt install burpsuite")
		elif option == "3":
			cmd = os.system("sudo apt install cewl")
		elif option == "4":
			cmd = os.system("sudo apt install chntpw")
		elif option == "5":
			cmd = os.system("sudo apt install cisco-auditing-tool")
		elif option == "6":
			cmd = os.system("sudo apt install cmospwd")
		elif option == "7":
			cmd = os.system("sudo apt install creddump")
		elif option == "8":
			cmd = os.system("sudo apt install crunch")
		elif option == "9":
			print "\nManual installation is required for: DBPwAudit"
			print "Please visit: http://www.cqure.net/wp/tools/database/dbpwaudit/\n"
		elif option == "10":
			cmd = os.system("sudo apt install findmyhash")
		elif option == "11":
			cmd = os.system("sudo apt install gpp-decrypt")
		elif option == "12":
			cmd = os.system("sudo apt install hash-identifier")
		elif option == "13":
			cmd = os.system("sudo apt install hexorbase")
		elif option == "14":
			cmd = os.system("sudo apt install hydra")
		elif option == "15":
			cmd = os.system("sudo apt install john")
		elif option == "16":
			cmd = os.system("sudo apt install johnny")
		elif option == "17":
			cmd = os.system("sudo apt install keimpx")
		elif option == "18":
			cmd = os.system("sudo apt install maltego-teeth")
		elif option == "19":
			cmd = os.system("sudo apt install maskprocessor")
		elif option == "20":
			cmd = os.system("sudo apt install multiforcer")
		elif option == "21":
			cmd = os.system("sudo apt install ncrack")
		elif option == "22":
			cmd = os.system("sudo apt install oclgausscrack")
		elif option == "23":
			cmd = os.system("sudo apt install pack")
		elif option == "24":
			cmd = os.system("sudo apt install patator")
		elif option == "25":
			print "\nManual installation is required for: phrasendrescher"
			print "Please visit: http://www.leidecker.info/projects/phrasendrescher/index.shtml\n"
		elif option == "26":
			cmd = os.system("sudo apt install polenum")
		elif option == "27":
			cmd = os.system("sudo apt install rainbowcrack")
		elif option == "28":
			cmd = os.system("sudo apt install rcracki-mt")
		elif option == "29":
			cmd = os.system("sudo apt install rsmangler")
		elif option == "30":
			print "SQLdict Not Available! :(\n"
		elif option == "31":
			cmd = os.system("sudo apt install statsprocessor")
		elif option == "32":
			cmd = os.system("sudo apt install thc-pptp-bruter")
		elif option == "33":
			cmd = os.system("sudo apt install truecrack")
		elif option == "34":
			cmd = os.system("sudo apt install webscarab")
		elif option == "35":
			cmd = os.system("sudo apt install wordlists")
		elif option == "36":
			cmd = os.system("sudo apt install zaproxy")
		elif option == "99":
			cmd = os.system("sudo apt install -y acccheck burpsuite cewl chntpw cisco-auditing-tool cmospwd creddump crunch")
			cmd = os.system("sudo apt install -y findmyhash gpp-decrypt hash-identifier hexorbase hydra john johnny keimpx maltego-teeth")
			cmd = os.system("sudo apt install -y maskprocessor multiforcer ncrack oclgausscrack pack patator polenum rainbowcrack rcracki-mt")
			cmd = os.system("sudo apt install -y rsmangler statsprocessor thc-pptp-bruter truecrack webscarab wordlists zaproxy")
			cmd = os.system("sudo apt -f install")