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
		self.title = "--=[Maintaining Access:"

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
				elif int(option) in range(1,18):
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
	1) CryptCat    10) PowerSploit
	2) Cymothoa    11) pwnat
	3) dbd         12) RidEnum
	4) dns2tcp     13) sbd
	5) http-tunnel 14) U3-Pwn
	6) HTTPTunnel  15) Webshells
	7) Intersect   16) Weevely
	8) Nishang     17) Winexe 
	9) polenum\n
	99) ALL\n
%sInsert the number of the tool to install it%s""" %(green,reset)
	
	def install(self, option):
		if option == "1":
			cmd = os.system("sudo apt install cryptcat")
		elif option == "2":
			cmd = os.system("sudo apt install cymothoa")      
		elif option == "3":
			cmd = os.system("sudo apt install dbd")      
		elif option == "4":
			cmd = os.system("sudo apt install dns2tcp")      
		elif option == "5":
			cmd = os.system("sudo apt install http-tunnel")      
		elif option == "6":
			cmd = os.system("sudo apt install httptunnel")      
		elif option == "7":
			cmd = os.system("sudo apt install intersect")      
		elif option == "8":
			cmd = os.system("sudo apt install nishang")      
		elif option == "9":
			cmd = os.system("sudo apt install polenum")      
		elif option == "10":
			cmd = os.system("sudo apt install powersploit")
		elif option == "11":
			cmd = os.system("sudo apt install pwnat")
		elif option == "12":
			cmd = os.system("sudo apt install ridenum")
		elif option == "13":
			cmd = os.system("sudo apt install sbd")
		elif option == "14":
			cmd = os.system("sudo apt install u3-pwn")
		elif option == "15":
			cmd = os.system("sudo apt install webshells")
		elif option == "16":
			cmd = os.system("sudo apt install weevely")
		elif option == "17":
			cmd = os.system("sudo apt install winexe")
		elif option == "99":
			cmd = os.system("sudo apt install -y cryptcat cymothoa dbd dns2tcp http-tunnel httptunnel intersect nishang")
			cmd = os.system("apt install -y polenum powersploit pwnat ridenum sbd u3-pwn webshells weevely winexe")
			cmd = os.system("apt -f install")