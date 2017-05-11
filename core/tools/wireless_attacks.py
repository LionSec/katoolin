#!/usr/bin/env	python
# -*- coding: utf-8 -*-

import os,sys

#colors
green = "\033[1;32m"
red = "\033[1;31m"
reset = "\033[0m"
yellow = "\033[33m"

class category_element(object):

	def __init__(self):
		self.title = "--=[Wireless Attacks:"

	def set_agv(self, argv):
		self.argv = argv

	def main(self, name):
		name = name.replace('core/tools/', "")
		self.view_tools()
		action = False
		while action == False:
			try:
				option = raw_input("--=[kat(%s%s%s)› " %(yellow,name,reset))
			except KeyboardInterrupt:
				print "Closing, bye! - Kalitools"
			try:
				if option == "back":
					break
				elif option == "clear":
					os.system('clear')
				elif option == "help":
					print """ Help
	 <option>	Select option
	 back		Go back
	 view 		See list of tools
	 clear		Clean screen
					"""
				elif option == "view":
					self.view_tools()
				elif int(option) in range(1,35):
					self.install(option)
				elif option == "99":
					self.install(option)
				else:
					print red+"Sorry, that was an invalid command!"+reset
			except ValueError:
				pass
					
	def view_tools(self):
		os.system('clear')
		print green+self.title+reset
		print """
	 1) Aircrack-ng       18) kalibrate-rtl
	 2) Asleap            19) KillerBee
	 3) Bluelog           20) Kismet
	 4) BlueMaho          21) mdk3
	 5) Bluepot           22) mfcuk
	 6) BlueRanger        23) mfoc
	 7) Bluesnarfer       24) mfterm
	 8) Bully             25) Multimon-N
	 9) coWPAtty          26) PixieWPS
	10) crackle           27) Reaver
	11) eapmd5pass        28) redfang
	12) Fern Wifi Cracker 29) RTLSDR Scanner
	13) Ghost Phisher     30) Spooftooph
	14) GISKismet         31) Wifi Honey
	15) Gqrx              32) wifiphisher
	16) gr-scan           33) Wifitap
	17) hostapd-wpe       34) Wifite\n
	99) ALL\n
%sInsert the number of the tool to install it%s""" %(green,reset)

	def install(self, option):
		if option == "1":
			cmd = os.system("sudo apt install aircrack-ng")
		elif option == "2":
			cmd = os.system("sudo apt install asleap")
		elif option == "3":
			cmd = os.system("sudo apt install bluelog")
		elif option == "4":
			print "\nManual installation is required for: BlueMaho"
			print "Please visit: https://wiki.thc.org/BlueMaho\n"
		elif option == "5":
			print "\nManual installation is required for: Bluepot"
			print "Please visit: https://github.com/andrewmichaelsmith/bluepot/\n"
		elif option == "6":
			cmd = os.system("sudo apt install blueranger")
		elif option == "7":
			cmd = os.system("sudo apt install bluesnarfer")
		elif option == "8":
			cmd = os.system("sudo apt install bully")
		elif option == "9":
			cmd = os.system("sudo apt install cowpatty")
		elif option == "10":
			cmd = os.system("sudo apt install crackle")
		elif option == "11":
			cmd = os.system("sudo apt install eapmd5pass")
		elif option == "12":
			cmd = os.system("sudo apt install fern-wifi-cracker")
		elif option == "13":
			cmd = os.system("sudo apt install ghost-phisher")
		elif option == "14":
			cmd = os.system("sudo apt install giskismet")
		elif option == "15":
			cmd = os.system("sudo apt install gqrx")
		elif option == "16":
			print "\nManual installation is required for: Gr-Scan"
			print "Please visit: http://www.techmeology.co.uk/gr-scan/\n"
		elif option == "17":
			cmd = os.system("sudo apt install hostapd-wpe")
		elif option == "18":
			cmd = os.system("sudo apt install kalibrate-rtl")
		elif option == "19":
			cmd = os.system("sudo apt install killerbee")
		elif option == "20":
			cmd = os.system("sudo apt install kismet")
		elif option == "21":
			cmd = os.system("sudo apt install mdk3")
		elif option == "22":
			cmd = os.system("sudo apt install  mfcuk")
		elif option == "23":
			cmd = os.system("sudo apt install mfoc")
		elif option == "24":
			cmd = os.system("sudo apt install mfterm")
		elif option == "25":
			cmd = os.system("sudo apt install multimon-ng")
		elif option == "26":
			cmd = os.system("sudo apt install pixiewps")
		elif option == "27":
			cmd = os.system("sudo apt install reaver")
		elif option == "28":
			cmd = os.system("sudo apt install redfang")
		elif option == "29":
			cmd = os.system("sudo apt install rtlsdr-scanner")
		elif option == "30":
			cmd = os.system("sudo apt install spooftooph")
		elif option == "31":
			cmd = os.system("sudo apt install wifi-honey")
		elif option == "32":
			cmd = os.system("sudo apt install wifiphisher")
		elif option == "33":
			cmd = os.system("sudo apt install wifitap")
		elif option == "34":
			cmd = os.system("sudo apt install wifite")
		elif option == "99":
			cmd = os.system("sudo apt -y install aircrack-ng asleap bluelog blueranger bluesnarfer bully cowpatty crackle")
			cmd = os.system("sudo apt install -y eapmd5pass fern-wifi-cracker ghost-phisher giskismet gqrx hostapd-wpe kalibrate-rtl")
			cmd = os.system("sudo apt install -y killerbee kismet mdk3 mfcuk mfoc mfterm multimon-ng pixiewps reaver redfang rtlsdr-scanner")
			cmd = os.system("sudo apt install -y spooftooph wifi-honey wifiphisher wifitap wifite")
			cmd = os.system("sudo apt -f install")