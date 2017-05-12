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
				elif int(option) in range(1,11):
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
%sInsert the number of the tool to install it%s""" %(load.Green,load.Reset)

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