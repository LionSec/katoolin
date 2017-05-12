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
				elif int(option) in range(1,7):
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
	1) android-sdk
	2) apktool
	3) Arduino
	4) dex2jar
	5) Sakis3G
	6) smali\n 
	99) ALL\n
%sInsert the number of the tool to install it%s""" %(load.Green,load.Reset)

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