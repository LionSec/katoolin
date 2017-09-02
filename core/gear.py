#!/usr/bin/env python
from core.categories import *
import sys, os

# colors
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[33m"
cyan = "\033[1;36m"
reset = "\033[0m"

menu_list = {
	"1":"show_categories",
	"2":"update",
	"3":"help",
	"4":"exit",
	"show":"show_categories",
	"clear":"clean_screen",
	"update":"update",
	"help":"help",
	"exit":"exit",
	"load":"load_category"
}

def load(action):
	globals()[action]()

def show_categories():
	print "Categories:\n"
	for name in categories.items():
		category = name[1][0][0]
		category = category.replace('_', ' ')
		category = category.title()
		if name[0]%2 != 0:
			print " "+str(name[0]).rjust(2) + ")", category.ljust(23)[:23],
		else:
			print " "+str(name[0]).rjust(2) + ")", category
	print " "

def load_category(key):
	if int(key) in categories.keys():
		os.system('clear')
		category = categories[int(key)][0][0]
		category = category.replace('_', ' ')
		category = category.title()
		print ":: " + category + "\n"
		show_tools(categories[int(key)][1])
		tools = categories[int(key)][1]
		site = categories[int(key)][0][0]
		action = False
		while action == False:
			try:
				option = raw_input(": katoolin (%s) > " %(site))
			except KeyboardInterrupt:
				delete_repository()
				print "..."; break
			try:
				if option == 'back':
					delete_repository()
					break
				elif option == 'clear':
					os.system('clear')
				elif option == 'show':
					show_tools(categories[int(key)][1])
				elif option == 'help':
					help(True)
				elif option == '99':
					add_repository()
					for tool in tools:
						install_tool = "apt install -y " + tool
						os.system(install_tool)
				elif int(option) in range(1,len(tools)+1):
					add_repository()
					install_tool = "apt install -y " + tools[int(option)-1]
					os.system(install_tool)
			except:
				pass
	else:
		print red + "E: The command is invalid!" + reset

def show_tools(tools):
	for tool in enumerate(tools):
		if tool[0]%2 == 0:
			print " "+str(tool[0]+1).rjust(2) + ")", tool[1].ljust(23)[:23],
		else:
			print " "+str(tool[0]+1).rjust(2) + ")", tool[1]
	print "\n 99) ALL"

def add_repository():
	if os.path.exists("/etc/apt/sources.list.d/katoolin.list"):
		add_key()
	else:
		try:
			f = open("/etc/apt/sources.list.d/katoolin.list", "wb")
			f.write("#Katoolin\ndeb http://http.kali.org/kali kali-rolling main contrib non-free\n# For source package access, uncomment the following line\n# deb-src http://http.kali.org/kali kali-rolling main contrib non-free\n")
			f.close()
			print green + "\n[+] Add repository\n" + reset
			add_key()
		except IOError:
			print red+"E: Please run as root"+reset
			sys.exit()

def delete_repository():
	repository = "/etc/apt/sources.list.d/katoolin.list"
	if os.path.exists(repository):
		os.remove(repository)
		print green + "\n[+] Repository deleted\n" + reset

def add_key():
	tmp_key = "/tmp/key_katoolin.txt"
	if os.path.exists(tmp_key):
		pass
	else:
		os.system("apt-key adv --keyserver pgp.mit.edu --recv-keys ED444FF07D8D0BF6")
		f = open(tmp_key, "wb")
		f.write("katoolin\n")
		f.close()
		print green + "\n[+] Add keyserver\n" + reset
		os.system('apt-get update -o Dir::Etc::sourcelist="sources.list.d/katoolin.list" -o Dir::Etc::sourceparts="-" -o apt::Get::List-Cleanup="0"')
		print green + "\n[+] Update\n" + reset

def banner():
	version = "v1.3b"
	options = """
 1) View Categories
 2) Update Kalitools
 3) Help

 4) Exit
	"""
	print """
 $$\   $$\             $$\                         $$\ $$\           
 $$ | $$  |            $$ |                        $$ |\__|          
 $$ |$$  /  $$$$$$\  $$$$$$\    $$$$$$\   $$$$$$\  $$ |$$\ $$$$$$$\  
 $$$$$  /   \____$$\ \_$$  _|  $$  __$$\ $$  __$$\ $$ |$$ |$$  __$$\ 
 $$  $$<    $$$$$$$ |  %sKali linux tools installer%s |$$ |$$ |$$ |  $$ |%s
 $$ |\$$\  $$  __$$ |  $$ |$$\ $$ |  $$ |$$ |  $$ |$$ |$$ |$$ |  $$ |
 $$ | \$$\ \$$$$$$$ |  \$$$$  |\$$$$$$  |\$$$$$$  |$$ |$$ |$$ |  $$ |
 \__|  \__| \_______|   \____/  \______/  \______/ \__|\__|\__|  \__| %s%s""" %(cyan,reset,cyan,version,reset)
 	print options

def update():
 	try:
		os.system('git pull')
		print  yellow + "W: Please restart katoolin" + reset
	except:
		print red + "E: can't start update please use <git pull>"+reset

def help(x=False):
	if x != True:
		print """: load=<category>   Load category
: clear             Clean screen  
: 1, show           Show categories
: 2, update         Update katoolin (git pull)
: 3, help           Show help
: 4, exit           Exit katoolin"""
	else:
		print """: <option>  Install tool
: 99        Install all tools in the category
: back      Return to previous menu
: clear     Clean screen
: show      Show tools
: help      Show help"""

def clean_screen():
	os.system('clear')
	banner()

def exit():
	print "\nClosing, bye! - katoolin"
	sys.exit()