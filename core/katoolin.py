#!/usr/bin/env	python
# -*- coding: utf-8 -*-

import sys,os
from core import mechanism,menu

def user_put():
	os.system('clear')
	mechanism.banner()
	action = False
	mechanism.options()
	while action == False:
		try:
			user_input = raw_input("--=[kat› ")
		except KeyboardInterrupt:
			print "Closing, bye! - Kalitools"
			sys.exit()
		if user_input in menu.menu_list:
			mechanism.load(menu.menu_list[user_input])
