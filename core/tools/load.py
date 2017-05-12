#!/usr/bin/env	python
# -*- coding: utf-8 -*-

import os,sys

Green = "\033[1;32m"
Red = "\033[1;31m"
Reset = "\033[0m"
Cyan = "\033[1;36m"
Yellow = "\033[33m"

def help():
	print """ <option>	Select option
 back		Go back
 view 		See list of tools
 clear		Clean screen"""

def title(name):
	name = name.replace("_", " ")
	name = name.title()
	print Green+"--=["+name+Reset

def input(name):
	kat = "%skat(%s%s%s)›%s " %(Cyan,Reset,name,Cyan,Reset)
	return kat
	
def error():
	print Red+"Sorry, that was an invalid command!"+Reset