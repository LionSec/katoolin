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
				elif int(option) in range(1,10):
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
	1) CaseFile
	2) CutyCapt
	3) dos2unix
	4) Dradis
	5) KeepNote
	6) MagicTree
	7) Metagoofil
	8) Nipper-ng
	9) pipal \n
	99) ALL\n
%sInsert the number of the tool to install it%s""" %(gload.Green,load.Reset)
	
	def install(self, option):
		if option == "1":
			cmd = os.system("sudo apt install casefile")
		elif option == "2":
			cmd = os.system("sudo apt install cutycapt")
		elif option == "3":
			cmd = os.system("sudo apt install dos2unix")
		elif option == "4":
			cmd = os.system("sudo apt install dradis")
		elif option == "5":
			cmd = os.system("sudo apt install keepnote")
		elif option == "6":
			cmd = os.system("sudo apt install magictree")
		elif option == "7":
			cmd = os.system("sudo apt install metagoofil")
		elif option == "8":
			cmd = os.system("sudo apt install nipper-ng")
		elif option == "9":
			cmd = os.system("sudo apt install pipal")
		elif option == "99":
			cmd = os.system("apt install -y casefile cutycapt dos2unix dradis keepnote magictree metagoofil nipper-ng pipal")
			cmd = os.system("apt -f install")