#!/usr/bin/env	python
# -*- coding: utf-8 -*-

import sys,os
from core import mechanism,menu

cyan = "\033[1;36m"
reset = "\033[0m"

def user_put():
	os.system('clear')
	mechanism.banner()
	action = False
	mechanism.options()
	while action == False:
		try:
			user_input = raw_input("%skat›%s " %(cyan,reset))
		except KeyboardInterrupt:
			print "Closing, bye! - Kalitools"
			sys.exit()
		if user_input in menu.menu_list:
			mechanism.load(menu.menu_list[user_input])
