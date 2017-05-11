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
		self.title = "--=[Reverse Engineering:"

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
				elif int(option) in range(1,12):
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
	11) YARA \n
	99) ALL\n
%sInsert the number of the tool to install it%s""" %(green,reset)

	def install(self, option):
		if option == "1":
			cmd = os.system("sudo apt install apktool")
		elif option == "2":
			cmd = os.system("sudo apt install dex2jar")
		elif option == "3":
			cmd = os.system("sudo apt install python-distorm3")
		elif option == "4":
			cmd = os.system("sudo apt install edb-debugger")
		elif option == "5":
			cmd = os.system("sudo apt install jad")
		elif option == "6":
			cmd = os.system("sudo apt install javasnoop")
		elif option == "7":
			print "JD-GUI Not Available! :(\n"
		elif option == "8":
			print "\nManual installation is required for: OllyDbgn"
			print "Please visit:  http://www.ollydbg.de/\n"
		elif option == "9":
			cmd = os.system("sudo apt install smali")
		elif option == "10":
			cmd = os.system("sudo apt install valgrind")
		elif option == "11":
			cmd = os.system("sudo apt install yara")
		elif option == "99":
			cmd = os.system("sudo apt install -y apktool dex2jar python-distorm3 edb-debugger jad javasnoop smali valgrind yara")
			cmd = os.system("sudo apt -f install")