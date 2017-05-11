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
		self.title = "--=[Hardware Hacking:"

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
				elif int(option) in range(1,7):
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
	1) android-sdk
	2) apktool
	3) Arduino
	4) dex2jar
	5) Sakis3G
	6) smali\n 
	99) ALL\n
%sInsert the number of the tool to install it%s""" %(green,reset)

	def install(self, option):
		if option == "1":
			cmd = os.system("sudo apt install android-sdk")
		elif option == "2":
			cmd = os.system("sudo apt install apktool")
		elif option == "3":
			cmd = os.system("sudo apt install arduino")
		elif option == "4":
			cmd = os.system("sudo apt install dex2jar")
		elif option == "5":
			cmd = os.system("sudo apt install sakis3g")
		elif option == "6":
			cmd = os.system("sudo apt install smali")
		elif option == "99":
			cmd = os.system("sudo apt install -y android-sdk apktool arduino dex2jar sakis3g smali")
			cmd = os.system("sudo apt -f install")