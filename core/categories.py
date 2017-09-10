#!/usr/bin/env python

categories = {
	1:['information_gathering', 
	['acccheck', 'ace-voip', 'amap', 'automater', 'braa', 'casefile', 'cdpsnarf', 'cisco-torch', 
	'cookie-cadger', 'copy-router-config', 'dmitry', 'dnmap', 'dnsenum', 'dnsmap', 'dnsrecon',
	'dnstracer', 'dnswalk', 'dotdotpwn', 'enum4linux', 'enumiax', 'fierce', 'firewalk', 'fragroute',
	'fragrouter', 'ghost-phisher', 'golismero', 'goofile', 'xplico', 'hping3', 'intrace', 'ismtp',
	'lbd', 'maltego-teeth', 'masscan', 'metagoofil', 'miranda', 'nbtscan-unixwiz', 'nmap', 'p0f',
	'parsero', 'recon-ng', 'set', 'smtp-user-enum', 'snmpcheck', 'sslcaudit', 'sslsplit', 'sslstrip',
	'sslyze', 'thc-ipv6', 'theharvester', 'tlssled', 'twofi', 'urlcrazy','wireshark', 'wol-e']
	],
	
	2:['vulnerability_analysis',
	['bbqsql', 'bed', 'cisco-auditing-tool', 'cisco-global-exploiter', 'cisco-ocs', 'cisco-torch',
	'copy-router-config', 'doona', 'dotdotpwn', 'greenbone-security-assistant', 'hexorbase', 'jsql',
	'lynis', 'nmap', 'ohrwurm', 'openvas-administrator', 'openvas-cli', 'openvas-manager', 'openvas-scanner',
	'oscanner', 'powerfuzzer', 'sfuzz', 'sidguesser', 'siparmyknife', 'sqlmap', 'sqlninja', 'sqlsus',
	'thc-ipv6', 'tnscmd10g', 'unix-privesc-check', 'yersinia']
	],

	3:['wireless_attacks',
	['aircrack-ng', 'asleap', 'bluelog', 'blueranger', 'bluesnarfer', 'bully', 'cowpatty', 'crackle', 
	'eapmd5pass', 'fern-wifi-cracker', 'ghost-phisher', 'giskismet', 'gqrx', 'hostapd-wpe', 'kalibrate-rtl',
	'killerbee', 'kismet', 'mdk3', 'mfcuk', 'mfoc', 'mfterm', 'multimon-ng', 'pixiewps', 'reaver', 'redfang',
	'rtlsdr-scanner', 'spooftooph', 'wifi-honey', 'wifiphisher', 'wifitap', 'wifite']
	],

	4:['web_applications',
	['apache-users', 'arachni', 'bbqsql', 'blindelephant', 'burpsuite', 'cutycapt', 'davtest', 'deblaze', 
	'dirb', 'dirbuster', 'fimap', 'funkload', 'gobuster', 'grabber', 'jboss-autopwn', 'joomscan', 'jsql',
	'maltego-teeth', 'padbuster', 'paros', 'parsero', 'plecost', 'powerfuzzer', 'proxystrike', 'recon-ng',
	'skipfish', 'sqlmap', 'sqlninja', 'sqlsus', 'ua-tester', 'uniscan', 'vega', 'w3af', 'webscarab',
	'websploit', 'wfuzz', 'wpscan', 'xsser', 'zaproxy']
	],

	5:['sniffing_spoofing',
	['burpsuite', 'dnschef', 'fiked', 'hamster-sidejack', 'hexinject', 'iaxflood', 'inviteflood', 'ismtp',
	'isr-evilgrade', 'mitmproxy', 'ohrwurm', 'protos-sip', 'rebind', 'responder', 'rtpbreak', 'rtpinsertsound',
	'rtpmixsound', 'sctpscan', 'siparmyknife', 'sipp', 'sipvicious', 'sniffjoke', 'sslsplit', 'sslstrip',
	'thc-ipv6', 'voiphopper', 'webscarab', 'wifi-honey', 'wireshark', 'xspy', 'yersinia', 'zaproxy']
	],

	6:['maintaining_access',
	['cryptcat', 'cymothoa', 'dbd', 'dns2tcp', 'http-tunnel', 'httptunnel', 'intersect', 'nishang', 'polenum',
	'powersploit', 'pwnat', 'ridenum', 'sbd', 'u3-pwn', 'webshells', 'weevely', 'winexe']
	],

	7:['reporting_tools',
	['casefile', 'cutycapt', 'dos2unix', 'dradis', 'keepnote', 'magictree', 'metagoofil', 'nipper-ng', 'pipal']
	],

	8:['exploitation_tools',
	['armitage', 'backdoor-factory', 'beef-xss', 'cisco-auditing-tool', 'cisco-global-exploiter', 'cisco-ocs', 
	'cisco-torch', 'crackle', 'exploitdb', 'jboss-autopwn', 'linux-exploit-suggester', 'maltego-teeth', 'set', 
	'shellnoob', 'sqlmap', 'thc-ipv6', 'yersinia']
	],

	9:['forensics_tools',
	['binwalk', 'bulk-extractor', 'chntpw', 'cuckoo', 'dc3dd', 'ddrescue', 'python-distorm3', 'dumpzilla', 
	'volatility', 'xplico', 'foremost', 'galleta', 'guymager', 'iphone-backup-analyzer', 'p0f', 'pdf-parser', 
	'pdfid', 'pdgmail', 'peepdf', 'extundelete']
	],

	10:['stress_testing',
	['dhcpig', 'funkload', 'iaxflood', 'inviteflood', 'ipv6-toolkit', 'mdk3', 'reaver', 'rtpflood', 
	'slowhttptest', 't50', 'termineter', 'thc-ipv6', 'thc-ssl-dos']
	],

	11:['password_attacks',
	['acccheck', 'burpsuite', 'cewl', 'chntpw', 'cisco-auditing-tool', 'cmospwd', 'creddump', 'crunch', 
	'findmyhash', 'gpp-decrypt', 'hash-identifier', 'hexorbase', 'hydra', 'john', 'johnny', 'keimpx', 
	'maltego-teeth', 'maskprocessor', 'multiforcer', 'ncrack', 'oclgausscrack', 'pack', 'patator', 'polenum', 
	'rainbowcrack', 'rcracki-mt', 'rsmangler', 'statsprocessor', 'thc-pptp-bruter', 'truecrack', 'webscarab', 
	'wordlists', 'zaproxy']
	],

	12:['reverse_engineering',
	['apktool', 'dex2jar', 'python-distorm3', 'edb-debugger', 'jad', 'javasnoop', 'smali', 'valgrind', 'yara']
	],

	13:['hardware_hacking',
	[	'android-sdk', 'apktool', 'arduino', 'dex2jar', 'sakis3g', 'smali']
	],

	14:['extra',
	['kali-linux', 'kali-linux-full', 'kali-linux-all', 'kali-linux-top10', 'kali-linux-forensic', 
	'kali-linux-gpu', 'kali-linux-pwtools', 'kali-linux-rfid', 'kali-linux-sdr', 'kali-linux-voip', 
	'kali-linux-web', 'kali-linux-wireless', 'squid3']
	]
}
