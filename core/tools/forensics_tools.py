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
				elif int(option) in range(1,24):
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
	 1) Binwalk        13) Foremost
	 2) bulk-extractor 14) Galleta
	 3) Capstone       15) Guymager
	 4) chntpw         16) iPhone Backup Analyzer
	 5) Cuckoo         17) p0f
	 6) dc3dd          18) pdf-parser
	 7) ddrescue       19) pdfid
	 8) DFF            20) pdgmail
	 9) diStorm3       21) peepdf
	10) Dumpzilla      22) RegRippe
	11) Volatility     23) extundelete
	12) Xplico\n
	99) ALL\n
%sInsert the number of the tool to install it%s""" %(load.Green,load.Reset)
	
	def install(self, option):
		if option == "1":
			cmd = os.system("sudo apt install binwalk")
		elif option == "2":
			cmd = os.system("sudo apt install bulk-extractor")
		elif option == "3":
			print "\nManual installation is required for: Capstone"
			print "Please visit: http://www.capstone-engine.org/index.html\n"
		elif option == "4":
			cmd = os.system("sudo apt install chntpw")
		elif option == "5":
			cmd = os.system("sudo apt install cuckoo")
		elif option == "6":
			cmd = os.system("sudo apt install dc3dd")
		elif option == "7":
			cmd = os.system("sudo apt install ddrescue")
		elif option == "8":
			print "\nManual installation is required for: DFF"
			print "Please visit: http://www.arxsys.fr/\n"
		elif option == "9":
			cmd = os.system("sudo apt install python-distorm3")
		elif option == "10":
			cmd = os.system("sudo apt install dumpzilla")
		elif option == "11":
			cmd = os.system("sudo apt install volatility")
		elif option == "12":
			cmd = os.system("sudo apt install xplico")
		elif option == "13":
			cmd = os.system("sudo apt install foremost")
		elif option == "14":
			cmd = os.system("sudo apt install galleta")
		elif option == "15":
			cmd = os.system("sudo apt install guymager")
		elif option == "16":
			cmd = os.system("sudo apt install iphone-backup-analyzer")
		elif option == "17":
			cmd = os.system("sudo apt install p0f")
		elif option == "18":
			cmd = os.system("sudo apt install pdf-parser")
		elif option == "19":
			cmd = os.system("sudo apt install pdfid")
		elif option == "20":
			cmd = os.system("sudo apt install pdgmail")
		elif option == "21":
			cmd = os.system("sudo apt install peepdf")
		elif option == "22":
			print "\nManual installation is required for: RegRipper"
			print "Please visit: https://code.google.com/archive/p/regripper/\n"
		elif option == "23":
			cmd = os.system("sudo apt install extundelete")
		elif option == "99":
			cmd = os.system("sudo apt install -y binwalk bulk-extractor chntpw cuckoo dc3dd ddrescue dumpzilla volatility xplico foremost")
			cmd = os.system("sudo apt install -y galleta guymager iphone-backup-analyzer p0f pdf-parser pdfid pdgmail peepdf extundelete")
			cmd = os.system("sudo apt -f install")
