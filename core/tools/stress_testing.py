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
				elif int(option) in range(1,15):
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
	14) THC-SSL-DOS \n
	99) ALL\n
%sInsert the number of the tool to install it%s""" %(load.Green,load.Reset)

	def install(self, option):
		if option == "1":
			cmd = os.system("sudo apt install dhcpig")
		elif option == "2":
			cmd = os.system("sudo apt install funkload")
		elif option == "3":
			cmd = os.system("sudo apt install iaxflood")
		elif option == "4":
			print "\nManual installation is required for: Inundator"
			print "Please visit: http://inundator.sourceforge.net/\n"
		elif option == "5":
			cmd = os.system("sudo apt install inviteflood")
		elif option == "6":
			cmd = os.system("sudo apt install ipv6-toolkit")
		elif option == "7":
			cmd = os.system("sudo apt install mdk3")
		elif option == "8":
			cmd = os.system("sudo apt install reaver")
		elif option == "9":
			cmd = os.system("sudo apt install rtpflood")
		elif option == "10":
			cmd = os.system("sudo apt install slowhttptest")
		elif option == "11":
			cmd = os.system("sudo apt install t50")
		elif option == "12":
			cmd = os.system("sudo apt install termineter")
		elif option == "13":
			cmd = os.system("sudo apt install thc-ipv6")
		elif option == "14":
			cmd = os.system("sudo apt install thc-ssl-dos")
		elif option == "99":
			cmd = os.system("sudo apt install -y dhcpig funkload iaxflood inviteflood ipv6-toolkit mdk3 reaver rtpflood slowhttptest")
			cmd = os.system("sudo apt install -y t50 termineter thc-ipv6 thc-ssl-dos")
			cmd = os.system("sudo apt -f install")