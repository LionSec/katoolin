#!/usr/bin/env	python

import sys

menu_list = {
	"quit":"exit_katoolin",
	"exit":"exit_katoolin",
	"help":"show_help",
	"options":"options",
    "update":"update_katoolin",
	"clear":"clear_screen",
	"version":"banner",
	"1":"view_categories",
	"2":"classicmenu",
	"3":"kalimenu",
}

categories = {
		"1":"information_gathering",
		"2":"vulnerability_analysis",
		"3":"wireless_attacks",
		"4":"web_applications",
		"5":"sniffing_spoofing",
		"6":"maintaining_access",
		"7":"reporting_tools",
		"8":"exploitation_tools",
		"9":"forensics_tools",
		"10":"stress_testing",
		"11":"password_attacks",
		"12":"reverse_engineering",
		"13":"hardware_hacking",
		"14":"extra",
}