from functools import reduce


programas_2_1_information_gathering = {
    'acccheck', 'ace-voip', 'amap', 'automater',
    'braa', 'casefile', 'cdpsnarf', 'cisco-torch',
    'cookie-cadger', 'copy-router-config', 'dmitry', 'dnmap', 'dnsenum',
    'dnsmap', 'dnsrecon', 'dnstracer', 'dnswalk', 'dotdotpwn', 'enum4linux',
    'enumiax', 'exploitdb', 'fierce', 'firewalk', 'fragroute', 'fragrouter',
    'ghost-phisher', 'golismero', 'goofile', 'lbd', 'maltego-teeth',
    'masscan', 'metagoofil', 'miranda', 'nmap', 'p0f', 'parsero',
    'recon-ng', 'set', 'smtp-user-enum', 'snmpcheck', 'sslcaudit',
    'sslsplit', 'sslstrip', 'sslyze', 'thc-ipv6', 'theharvester', 'tlssled',
    'twofi', 'urlcrazy', 'wireshark', 'wol-e', 'xplico', 'ismtp', 'intrace',
    'hping3'
}


# 'install all items' no inicio e 'done' no final
programas_2_2_vulnerability_analysis = {
    'bbqsql', 'bed', 'cisco-auditing-tool',
    'cisco-global-exploiter', 'cisco-ocs', 'cisco-torch', 'copy-router-config',
    'doona', 'dotdotpwn', 'greenbone-security-assistant', 'hexorbase', 'jsql',
    'lynis', 'nmap', 'ohrwurm', 'openvas-cli', 'openvas-manager',
    'openvas-scanner', 'oscanner', 'powerfuzzer', 'stuzz', 'sidguesser',
    'siparmyknife', 'sqlmap', 'sqlninja', 'sqlsus', 'thc-ipv6', 'tnscmd10g',
    'unix-privesc-check', 'yersinia'
}


programas_2_3_wireless_attacks = {
    'aircrack-ng', 'asleap', 'bluelog', 'blueranger',
    'bluesnarfer', 'bully', 'cowpatty', 'crackle', 'eapmd5pass',
    'fern-wifi-cracker', 'ghost-phisher', 'giskismet', 'gqrx', 'kalibrate-rtl',
    'killerbee', 'kismet', 'mdk3', 'mfcuk', 'mfoc', 'mfterm', 'multimon-ng',
    'pixiewps', 'reaver', 'redfang', 'spooftooph', 'wifi-honey',
    'wifitap wifite'
}


programas_2_4_web_applications = {
    'apache-users', 'arachni', 'bbqsql', 'blindelephant',
    'burpsuite', 'cutycapt', 'davtest', 'deblaze', 'dirb', 'dirbuster', 'fimap',
    'funkload', 'grabber', 'jboss-autopwn', 'joomscan', 'jsql', 'maltego-teeth',
    'padbuster', 'paros', 'parsero', 'plecost', 'powerfuzzer', 'proxystrike',
    'recon-ng', 'skipfish', 'sqlmap', 'sqlninja', 'sqlsus', 'ua-tester',
    'uniscan', 'vega', 'w3af', 'webscarab', 'websploit', 'wfuzz', 'wpscan',
    'xsser', 'zaproxy'
}

programas_2_5_sniffing_and_spoofing = {
    'burpsuite', 'dnschef', 'fiked', 'hamster-sidejack',
    'hexinject', 'iaxflood', 'inviteflood', 'ismtp', 'mitmproxy', 'ohrwurm',
    'protos-sip', 'rebind', 'responder', 'rtpbreak', 'rtpinsertsound',
    'rtpmixsound', 'sctpscan', 'siparmyknife', 'sipp', 'sipvicious',
    'sniffjoke', 'sslsplit', 'sslstrip', 'thc-ipv6', 'voiphopper', 'webscarab',
    'wifi-honey', 'wireshark', 'xspy', 'yersinia', 'zaproxy'
}

programas_2_6_maintaining_access = {
    'cryptcat', 'cymothoa', 'dbd', 'dns2tcp',
    'http-tunnel', 'httptunnel', 'intersect', 'nishang', 'polenum',
    'powersploit', 'pwnat', 'ridenum', 'sbd', 'u3-pwn', 'webshells', 'weevely'
}

programas_2_7_reporting_tools = {
    'casefile', 'cutycapt', 'dos2unix', 'dradis',
    'keepnote', 'magictree', 'metagoofil', 'nipper-ng', 'pipal'
}

programas_2_8_exploitation_tools = {
    'armitage', 'backdoor-factory', 'cisco-auditing-tool',
    'cisco-global-exploiter', 'cisco-ocs', 'cisco-torch', 'crackle',
    'jboss-autopwn', 'linux-exploit-suggester', 'maltego-teeth', 'set',
    'shellnoob', 'sqlmap', 'thc-ipv6', 'yersinia', 'beef-xss'
}

programas_2_9_forensics_tools = {
    'binwalk', 'bulk-extractor', 'chntpw', 'cuckoo',
    'dc3dd', 'ddrescue', 'dumpzilla', 'extundelete', 'foremost', 'galleta',
    'guymager', 'iphone-backup-analyzer', 'p0f', 'pdf-parser', 'pdfid',
    'pdgmail', 'peepdf', 'volatility', 'xplico'
}

programas_2_10_stress_testing = {
    'dhcpig', 'funkload', 'iaxflood', 'inviteflood',
    'ipv6-toolkit', 'mdk3', 'reaver', 'rtpflood', 'slowhttptest', 't50',
    'termineter', 'thc-ipv6', 'thc-ssl-dos'
}

programas_2_11_password_attacks = {
    'acccheck', 'burpsuite', 'cewl', 'chntpw',
    'cisco-auditing-tool', 'cmospwd', 'creddump', 'crunch', 'findmyhash',
    'gpp-decrypt', 'hash-identifier', 'hexorbase', 'john', 'johnny', 'keimpx',
    'maltego-teeth', 'maskprocessor', 'multiforcer', 'ncrack', 'oclgausscrack',
    'pack', 'patator', 'polenum', 'rainbowcrack', 'rcracki-mt', 'rsmangler',
    'statsprocessor', 'thc-pptp-bruter', 'truecrack', 'webscarab', 'wordlists',
    'zaproxy'
}

programas_2_12_reverse_engine = {
    'apktool', 'dex2jar', 'python-diStorm3',
    'edb-debugger', 'jad', 'javasnoop', 'JD', 'OllyDbg', 'smali', 'Valgrind',
    'YARA'
}

programas_2_13_hardware_hacking = {
    'android-sdk', 'apktool', 'arduino', 'dex2jar',
    'sakis3g', 'smali'
}

programas_2_14_extra = {
    'squid3'
}


tudo = reduce(
    lambda x, y: x.union(y),
    [programas_2_1_information_gathering, programas_2_2_vulnerability_analysis,
    programas_2_3_wireless_attacks, programas_2_4_web_applications,
    programas_2_5_sniffing_and_spoofing, programas_2_6_maintaining_access,
    programas_2_7_reporting_tools, programas_2_8_exploitation_tools,
    programas_2_9_forensics_tools, programas_2_10_stress_testing,
    programas_2_11_password_attacks, programas_2_12_reverse_engine,
    programas_2_13_hardware_hacking, programas_2_14_extra]
)