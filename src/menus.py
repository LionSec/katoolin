from .ferramentas import formatar_texto
from .programas import (
    programas_2_1_information_gathering, programas_2_2_vulnerability_analysis,
    programas_2_3_wireless_attacks, programas_2_4_web_applications,
    programas_2_5_sniffing_and_spoofing, programas_2_6_maintaining_access,
    programas_2_7_reporting_tools, programas_2_8_exploitation_tools,
    programas_2_9_forensics_tools, programas_2_10_stress_testing,
    programas_2_11_password_attacks, programas_2_12_reverse_engine,
    programas_2_13_hardware_hacking, programas_2_14_extra
)


def main_menu():
    menu = """
    1) Add Kali repositories & Update
    2) View Categories
    3) Install classicmenu indicator
    4) Install Kali menu
    5) Help

    >>> """.replace('    ', '')
    return menu


def menu_1():
    menu = """
    1) Add kali linux repositories
    2) Update
    3) Remove all kali linux repositories
    type back to return

    >>> """.replace('    ', '')
    return menu


def menu_2():
    menu = """
    1) Information Gathering			8) Exploitation Tools
    2) Vulnerability Analysis			9) Forensics Tools
    3) Wireless Attacks				    10) Stress Testing
    4) Web Applications				    11) Password Attacks
    5) Sniffing & Spoofing				12) Reverse Engineering
    6) Maintaining Access				13) Hardware Hacking
    7) Reporting Tools 				    14) Extra

    0) All
    type back to return

    >>> """.replace('    ', '')
    return menu


def menu_2_1():
    texto = formatar_texto(programas_2_1_information_gathering)
    texto += '\n\ntype back to return\n>>> '
    return texto


def menu_2_2():
    texto = formatar_texto(programas_2_2_vulnerability_analysis)
    texto += '\n\ntype back to return\n>>> '
    return texto


def menu_2_3():
    texto = formatar_texto(programas_2_3_wireless_attacks)
    texto += '\n\ntype back to return\n>>> '
    return texto


def menu_2_4():
    texto = formatar_texto(programas_2_4_web_applications)
    texto += '\n\ntype back to return\n>>> '
    return texto


def menu_2_5():
    texto = formatar_texto(programas_2_5_sniffing_and_spoofing)
    texto += '\n\ntype back to return\n>>> '
    return texto


def menu_2_6():
    texto = formatar_texto(programas_2_6_maintaining_access)
    texto += '\n\ntype back to return\n>>> '
    return texto


def menu_2_7():
    texto = formatar_texto(programas_2_7_reporting_tools)
    texto += '\n\ntype back to return\n>>> '
    return texto


def menu_2_8():
    texto = formatar_texto(programas_2_8_exploitation_tools)
    texto += '\n\ntype back to return\n>>> '
    return texto


def menu_2_9():
    texto = formatar_texto(programas_2_9_forensics_tools)
    texto += '\n\ntype back to return\n>>> '
    return texto


def menu_2_10():
    texto = formatar_texto(programas_2_10_stress_testing)
    texto += '\n\ntype back to return\n>>> '
    return texto


def menu_2_11():
    texto = formatar_texto(programas_2_11_password_attacks)
    texto += '\n\ntype back to return\n>>> '
    return texto


def menu_2_12():
    texto = formatar_texto(programas_2_12_reverse_engine)
    texto += '\n\ntype back to return\n>>> '
    return texto


def menu_2_13():
    texto = formatar_texto(programas_2_13_hardware_hacking)
    texto += '\n\ntype back to return\n>>> '
    return texto


def menu_2_14():
    texto = formatar_texto(programas_2_14_extra)
    texto += '\n\ntype back to return\n>>> '
    return texto
