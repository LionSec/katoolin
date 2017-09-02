#!/usr/bin/env	python
# -*- coding: utf-8 -*-

import sys,os
from core import gear

def user_put():
	os.system('clear')
	gear.banner()
	action = False
	while action == False:
		try:
			user_input = raw_input(": katoolin > ")
		except KeyboardInterrupt:
			print "\nClosing, bye! - katoolin"
			sys.exit()
		if user_input in gear.menu_list:
			gear.load(gear.menu_list[user_input])
		elif "=" in user_input:
			user_input = user_input.split('=')
			if "load" == user_input[0]:
				gear.load_category(user_input[1])

if __name__ == '__main__':
	user_put()