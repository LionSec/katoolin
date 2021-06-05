from .menus import (
    menu_2_1, menu_2_2, menu_2_3, menu_2_4, menu_2_5, menu_2_6, menu_2_7,
    menu_2_8, menu_2_9, menu_2_10, menu_2_11, menu_2_12, menu_2_13, menu_2_14
)

from .programas import (
    programas_2_1_information_gathering, programas_2_2_vulnerability_analysis,
    programas_2_3_wireless_attacks, programas_2_4_web_applications,
    programas_2_5_sniffing_and_spoofing, programas_2_6_maintaining_access,
    programas_2_7_reporting_tools, programas_2_8_exploitation_tools,
    programas_2_9_forensics_tools, programas_2_10_stress_testing,
    programas_2_11_password_attacks, programas_2_12_reverse_engine,
    programas_2_13_hardware_hacking, programas_2_14_extra
)

argumentos_pacotes = [
    (menu_2_1, programas_2_1_information_gathering),
    (menu_2_2, programas_2_2_vulnerability_analysis),
    (menu_2_3, programas_2_3_wireless_attacks),
    (menu_2_4, programas_2_4_web_applications),
    (menu_2_5, programas_2_5_sniffing_and_spoofing),
    (menu_2_6, programas_2_6_maintaining_access),
    (menu_2_7, programas_2_7_reporting_tools),
    (menu_2_8, programas_2_8_exploitation_tools),
    (menu_2_9, programas_2_9_forensics_tools),
    (menu_2_10, programas_2_10_stress_testing),
    (menu_2_11, programas_2_11_password_attacks),
    (menu_2_12, programas_2_12_reverse_engine),
    (menu_2_13, programas_2_13_hardware_hacking),
    (menu_2_14, programas_2_14_extra)
]

_numeros = map(str, range(1, len(argumentos_pacotes) + 1))
argumentos_pacotes = dict(zip(_numeros, argumentos_pacotes))
