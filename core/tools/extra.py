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
		self.title = "--=[Extra:"

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
				elif int(option) in range(1,15):
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
	Kali Linux Metapackages:
	1) kali-linux         
	2) kali-linux-full    
	3) kali-linux-all     
	4) kali-linux-top10   
	5) kali-linux-forensic
	6) kali-linux-gpu     
	7) kali-linux-pwtools 
	8) kali-linux-rfid    
	9) kali-linux-sdr     
	10) kali-linux-voip    
	11) kali-linux-web     
	12) kali-linux-wireless

	Extra:
	13) Wifresti
	14) Squid3\n
%sInsert the number of the tool to install it%s""" %(green,reset)

	def install(self, option):
		if option == "1":
			cmd = os.system("sudo apt install kali-linux")
		elif option == "2":
			cmd = os.system("sudo apt install kali-linux-full")
		elif option == "3":
			cmd = os.system("sudo apt install kali-linux-all")
		elif option == "4":
			cmd = os.system("sudo apt install kali-linux-top10")
		elif option == "5":
			cmd = os.system("sudo apt install kali-linux-forensic")
		elif option == "6":
			cmd = os.system("sudo apt install kali-linux-gpu")
		elif option == "7":
			cmd = os.system("sudo apt install kali-linux-pwtools")
		elif option == "8":
			cmd = os.system("sudo apt install kali-linux-rfid")
		elif option == "9":
			cmd = os.system("sudo apt install kali-linux-sdr")
		elif option == "10":
			cmd = os.system("sudo apt install kali-linux-voip")
		elif option == "11":
			cmd = os.system("sudo apt install kali-linux-web")
		elif option == "12":
			cmd = os.system("sudo apt install kali-linux-wireless")
		elif option == "13":
			cmd = os.system("git clone https://github.com/LionSec/wifresti.git && cp wifresti/wifresti.py /usr/bin/wifresti && chmod +x /usr/bin/wifresti && wifresti")
		elif option == "14":
			cmd = os.system("sudo apt install squid3")