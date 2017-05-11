#!/usr/bin/env	python
# -*- coding: utf-8 -*-

import sys,os
import glob
from core import menu

#colors
red = "\033[1;31m"
yellow = "\033[33m"
green = "\033[1;32m"
cyan = "\033[1;36m"
reset = "\033[0m"

def options():
	print """
 1) View Categories
 2) Install classicmenu indicator
 3) Install Kali menu
"""

def banner():
	version = "v1.2b"
	print """
 $$\   $$\             $$\                         $$\ $$\           
 $$ | $$  |            $$ |                        $$ |\__|          
 $$ |$$  /  $$$$$$\  $$$$$$\    $$$$$$\   $$$$$$\  $$ |$$\ $$$$$$$\  
 $$$$$  /   \____$$\ \_$$  _|  $$  __$$\ $$  __$$\ $$ |$$ |$$  __$$\ 
 $$  $$<    $$$$$$$ |  %sKali linux tools installer%s |$$ |$$ |$$ |  $$ |%s
 $$ |\$$\  $$  __$$ |  $$ |$$\ $$ |  $$ |$$ |  $$ |$$ |$$ |$$ |  $$ |
 $$ | \$$\ \$$$$$$$ |  \$$$$  |\$$$$$$  |\$$$$$$  |$$ |$$ |$$ |  $$ |
 \__|  \__| \_______|   \____/  \______/  \______/ \__|\__|\__|  \__| %s%s""" %(cyan,reset,cyan,version,reset)
 	print """
%s + -- -- +=[ Author: LionSec | Homepage: www.lionsec.net
 + -- -- +=[ 332 Tools%s""" %(green,reset)

def load(action):
 	globals()[action]()

def exit_katoolin():
	sys.exit()

def show_help():
	print """ Help katoolin\n
 quit		exit katoolin
 clear 		clear screen
 update 	update katoolin
 options	See options
 """

def update_katoolin():
	try:
		os.system('git pull')
		print  yellow+"[W] Please restart katoolin"+reset
	except:
		print red+"[E] can't start update please use <git pull>"+reset

def clear_screen():
	os.system('clear')

def classicmenu():
	print""" 
ClassicMenu Indicator is a notification area applet (application indicator) for the top panel of Ubuntu's Unity desktop environment
It provides a simple way to get a classic GNOME-style application menu for those who prefer this over the Unity dash menu
Like the classic GNOME menu, it includes Wine games and applications if you have those installed
For more information , please visit : http://www.florian-diesch.de/software/classicmenu-indicator"""
	repo = raw_input("%sDo you want to install classicmenu indicator ? [y/n]>%s " %(green,reset))
	if repo == "y" or repo == "Y":
		os.system("add-apt-repository ppa:diesch/testing && apt-get update")
		os.system("sudo apt-get install classicmenu-indicator")
	else:
		print "Installation canceled"

def kalimenu():
	repo = raw_input("%sDo you want to install Kali menu ? [y/n]>%s " %(green,reset))
	if repo == "y" or repo == "Y":
		os.system("apt-get install kali-menu")
	else: 
		print "Installation canceled"


def view_categories():
	os.system('clear')
	print """
%s**************************** All Categories *****************************%s

 1) Information Gathering			 8) Exploitation Tools
 2) Vulnerability Analysis			 9) Forensics Tools
 3) Wireless Attacks				10) Stress Testing
 4) Web Applications				11) Password Attacks
 5) Sniffing & Spoofing				12) Reverse Engineering
 6) Maintaining Access				13) Hardware Hacking
 7) Reporting Tools 				14) Extra\n""" %(cyan,reset)
	print "%s Select a category:%s\n" %(green,reset)
	action = False
	while action == False:
		try:
			option = raw_input("--=[kat(%scategories%s)› " %(yellow,reset))
		except:
			pass
		if option == "back":
			delete_repository()
			break
		elif option == "clear":
			os.system('clear')
		elif option == "quit":
			delete_repository()
			sys.exit()
		elif option in menu.categories:
			add_repository()
			load_category(menu.categories[option])
		elif option == "view":
			view_categories()
		elif option == "help":
				print """ Help
 <option>	Select option
 back		Go back
 quit		Exit Katoolin
 view 		View categories
 clear		Clean screen
 """

def load_category(name):
	name = "core/tools/" + name + ".py"
	if os.path.exists(name):
		get_in(name)
	else:
		print red + "Category not found" + reset

def get_in(category, argv=False):
	category_class = ""
	category_name = category.split(".py")[0]
	if category_class == "":
		category_path = category_name.replace("/",".")
		cate = __import__(category_path, fromlist=['category_element'])
		category_class = cate.category_element()
	if argv != False:
		category_class.set_agv(argv)
	category_class.main(category_name)

def add_repository():
	print yellow+"Checking kali linux repository [...]"+reset
	try:
		f = open("/etc/apt/sources.list.d/katoolin.list", "wb")
		f.write("#Katoolin\ndeb http://http.kali.org/kali kali-rolling main contrib non-free\n# For source package access, uncomment the following line\n# deb-src http://http.kali.org/kali kali-rolling main contrib non-free\n")
		f.close()
	except IOError:
		print red+"[E] Please run as root!"+reset
		sys.exit()
	if os.path.exists("/etc/apt/sources.list.d/katoolin.list"):
		print " [%s+%s] Added repositorie" %(green, reset)
		add_key()

def add_key():
	print yellow+"Checking Kali Linux repository key [...]"+reset
	tmp_key = "/tmp/key_katoolin.txt"
	if os.path.exists(tmp_key):
		print " [%s+%s] The key has already been added" %(green,reset)
	else:
		os.system("apt-key adv --keyserver pgp.mit.edu --recv-keys ED444FF07D8D0BF6")
		f = open(tmp_key, "wb")
		f.write("katoolin\n")
		f.close()
		print " [%s+%s] Aggregate key" %(green,reset)
	
	os.system("sudo apt update -m")

def delete_repository():
	repository = "/etc/apt/sources.list.d/katoolin.list"
	if os.path.exists(repository):
		os.remove(repository)
		print " [%s+%s] Repository deleted" %(green,reset)