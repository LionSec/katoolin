import curses, os
from apt import cache

from .menus import (
    main_menu, menu_1, menu_2, menu_2_1, menu_2_2, menu_2_3, menu_2_4,
    menu_2_5, menu_2_6, menu_2_7, menu_2_8, menu_2_9, menu_2_10, menu_2_11,
    menu_2_12, menu_2_13, menu_2_14
)
from .ferramentas import (
    mostrar_menus, verificar_root, mostrar_banner, mostrar_texto, terminado,
    gerenciar_pacotes
)
from .comandos import (
    adicionar_kali_repositorio, remover_kali_repositorio,
    adicionar_diesch_repositorio
)
from .apt_install import instalar
from .programas import (
    programas_2_1_information_gathering, programas_2_2_vulnerability_analysis,
    programas_2_3_wireless_attacks, programas_2_4_web_applications,
    programas_2_5_sniffing_and_spoofing, programas_2_6_maintaining_access,
    programas_2_7_reporting_tools, programas_2_8_exploitation_tools,
    programas_2_9_forensics_tools, programas_2_10_stress_testing,
    programas_2_11_password_attacks, programas_2_12_reverse_engine,
    programas_2_13_hardware_hacking, programas_2_14_extra
)


def opcoes_menu_1(tela):
    while True:
        opcoes = ['1','2','3','4', 'back']
        tecla = mostrar_menus(tela, menu_1, opcoes)
        if tecla == '1':
            adicionar_kali_repositorio()
            # executar(add_apt_key)
            terminado(tela)
        elif tecla == '2':
            mostrar_texto(tela, 'wait for the command to finish running.')
            cache_ = cache.Cache()
            cache_.update()
            terminado(tela)
        elif tecla == '3':
            remover_kali_repositorio()
            terminado(tela)
        elif tecla == 'back':
            break


def opcoes_menu_2(tela):
    opcoes = list(map(str, range(15)))
    opcoes.append('back')
    while True:
        tecla = mostrar_menus(tela, menu_2, opcoes)
        if tecla == '0':
            pass
        elif tecla == '1':
            gerenciar_pacotes(tela, menu_2_1, programas_2_1_information_gathering)
        elif tecla == '2':
            gerenciar_pacotes(tela, menu_2_2, programas_2_2_vulnerability_analysis)
        elif tecla == '3':
            gerenciar_pacotes(tela, menu_2_3, programas_2_3_wireless_attacks)
        elif tecla == '4':
            gerenciar_pacotes(tela, menu_2_4, programas_2_4_web_applications)
        elif tecla == '5':
            gerenciar_pacotes(tela, menu_2_5, programas_2_5_sniffing_and_spoofing)
        elif tecla == '6':
            gerenciar_pacotes(tela, menu_2_6, programas_2_6_maintaining_access)
        elif tecla == '7':
            gerenciar_pacotes(tela, menu_2_7, programas_2_7_reporting_tools)
        elif tecla == '8':
            gerenciar_pacotes(tela, menu_2_8, programas_2_8_exploitation_tools)
        elif tecla == '9':
            gerenciar_pacotes(tela, menu_2_9, programas_2_9_forensics_tools)
        elif tecla == '10':
            gerenciar_pacotes(tela, menu_2_10, programas_2_10_stress_testing)
        elif tecla == '11':
            gerenciar_pacotes(tela, menu_2_11, programas_2_11_password_attacks)
        elif tecla == '12':
            gerenciar_pacotes(tela, menu_2_12, programas_2_12_reverse_engine)
        elif tecla == '13':
            gerenciar_pacotes(tela, menu_2_13, programas_2_13_hardware_hacking)
        elif tecla == '14':
            gerenciar_pacotes(tela, menu_2_14, programas_2_14_extra)
        elif tecla == 'back':
            break
        terminado(tela)


def katoolin_main(tela):
    try:
        colunas, linhas = os.get_terminal_size()
        curses.initscr()
        # tela = curses.newwin(linhas + 1, colunas + 1)
        curses.echo()
        verificar_root(tela)
        mostrar_banner(tela)
        while True:
            tecla = mostrar_menus(tela, main_menu, ['1','2','3','4','5'])
            if tecla == '1':
                opcoes_menu_1(tela)
            elif tecla == '2':
                opcoes_menu_2(tela)
            elif tecla == '3':
                adicionar_diesch_repositorio()
                cache_ = cache.Cache()
                cache_.update()
                instalar('classicmenu-indicator')
                terminado(tela)
            elif tecla == '4':
                install('kali-menu')
            elif tecla == 'back':
                pass
    finally:
        curses.endwin()
