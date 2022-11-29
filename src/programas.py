from functools import reduce


# all programs that are commented out are not in the repository

programas_2_1_information_gathering = {
    'amap',
    'braa', 'casefile', 'cisco-torch',
    'copy-router-config', 'dmitry', 'dnsenum',
    'dnsmap', 'dnsrecon', 'dnstracer', 'dnswalk', 'dotdotpwn', 'enum4linux',
    'enumiax', 'exploitdb', 'fierce', 'firewalk', 'fragrouter',
    'goofile', 'lbd', 'maltego-teeth',
    'masscan', 'metagoofil', 'nmap', 'p0f', 'parsero',
    'recon-ng', 'set', 'smtp-user-enum', 'snmpcheck',
    'sslsplit', 'sslstrip', 'sslyze', 'thc-ipv6', 'theharvester', 'tlssled',
    'twofi', 'urlcrazy', 'wireshark', 'xplico', 'ismtp', 'intrace',
    'hping3'
}
# cdpsnarf, miranda, acccheck, ghost-phisher, wol-e, fragroute,
# ace-voip, golismero, sslcaudit, cookie-cadger, automater,
# dnmap


programas_2_2_vulnerability_analysis = {
    'bed', 'cisco-auditing-tool',
    'cisco-global-exploiter', 'cisco-ocs', 'cisco-torch', 'copy-router-config',
    'doona', 'dotdotpwn', 'greenbone-security-assistant', 'jsql',
    'lynis', 'nmap', 'ohrwurm',
    'openvas-scanner', 'oscanner', 'sidguesser',
    'siparmyknife', 'sqlmap', 'sqlninja', 'sqlsus', 'thc-ipv6', 'tnscmd10g',
    'unix-privesc-check', 'yersinia'
}
# bbqsql, powerfuzzer, hexorbase, stuzz, openvas-manager, openvas-cli


programas_2_3_wireless_attacks = {
    'aircrack-ng', 'asleap', 'bluelog', 'blueranger',
    'bluesnarfer', 'bully', 'cowpatty', 'crackle', 'eapmd5pass',
    'fern-wifi-cracker', 'kalibrate-rtl',
    'kismet', 'mdk3', 'mfcuk', 'mfoc', 'mfterm', 'multimon-ng',
    'pixiewps', 'reaver', 'redfang', 'spooftooph', 'wifi-honey'
}
# ghost-phisher, giskismet, gqrx, killerbee
# wifite -> this program throws an error when downloading it


programas_2_4_web_applications = {
    'apache-users',
    'burpsuite', 'cutycapt', 'davtest', 'dirb', 'dirbuster',
    'jboss-autopwn', 'joomscan', 'jsql', 'maltego-teeth',
    'padbuster', 'paros', 'parsero', 'plecost',
    'recon-ng', 'skipfish', 'sqlmap', 'sqlninja', 'sqlsus',
    'uniscan', 'webscarab', 'websploit', 'wfuzz', 'wpscan',
    'xsser', 'zaproxy'
}
# ua-tester, bbqsql, powerfuzzer, blindelephant, arachni, vega, w3af,
# funkload, fimap, proxystrike, grabber, deblaze


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
    'httptunnel', 'nishang', 'polenum',
    'powersploit', 'pwnat', 'ridenum', 'sbd', 'webshells', 'weevely'
}
# u3-pwn, http-tunnel, intersect

programas_2_7_reporting_tools = {
    'casefile', 'cutycapt', 'dos2unix', 'dradis',
    'metagoofil', 'nipper-ng', 'pipal'
}
# keepnote, magictree

programas_2_8_exploitation_tools = {
    'armitage', 'backdoor-factory', 'cisco-auditing-tool',
    'cisco-global-exploiter', 'cisco-ocs', 'cisco-torch', 'crackle',
    'jboss-autopwn', 'linux-exploit-suggester', 'maltego-teeth', 'set',
    'shellnoob', 'sqlmap', 'thc-ipv6', 'yersinia', 'beef-xss'
}

programas_2_9_forensics_tools = {
    'binwalk', 'bulk-extractor', 'chntpw',
    'dc3dd', 'ddrescue', 'dumpzilla', 'extundelete', 'foremost', 'galleta',
    'guymager', 'p0f', 'pdf-parser', 'pdfid',
    'xplico'
}
# volatility, pdgmail, iphone-backup-analyzer, peepdf, cuckoo

programas_2_10_stress_testing = {
    'dhcpig', 'iaxflood', 'inviteflood',
    'ipv6-toolkit', 'mdk3', 'reaver', 'rtpflood', 'slowhttptest', 't50',
    'termineter', 'thc-ipv6', 'thc-ssl-dos'
}
# funkload

programas_2_11_password_attacks = {
    'burpsuite', 'cewl', 'chntpw',
    'cisco-auditing-tool', 'cmospwd', 'crunch',
    'gpp-decrypt', 'hash-identifier', 'john', 'johnny',
    'maltego-teeth', 'maskprocessor', 'multiforcer', 'ncrack', 'oclgausscrack',
    'pack', 'patator', 'polenum', 'rainbowcrack', 'rcracki-mt', 'rsmangler',
    'statsprocessor', 'thc-pptp-bruter', 'truecrack', 'webscarab', 'wordlists',
    'zaproxy'
}
# findmyhash, creddump, hexorbase, acccheck, keimpx

programas_2_12_reverse_engine = {
    'apktool', 'dex2jar',
    'edb-debugger', 'javasnoop', 'ollydbg', 'smali', 'valgrind',
    'yara'
}
# jad, jd, python-distorm3

programas_2_13_hardware_hacking = {
    'android-sdk', 'apktool', 'arduino', 'dex2jar',
    'sakis3g', 'smali'
}

programas_2_14_extra = {}
# squid3


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